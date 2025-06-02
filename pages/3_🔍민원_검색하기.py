import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import date
from sheets_oauth import load_all_complaints, filter_by_author, count_by_date

st.set_page_config(page_title="민원 검색하기")
st.title("🔎 민원 검색하기")

#데이터 불러오기 (구글 시트에서)
raw_data = load_all_complaints()

if raw_data:
    df = pd.DataFrame(raw_data, columns=["작성자", "내용", "위도", "경도", "작성일", "제출 시간", "민원 종류"])
    df["작성일"] = pd.to_datetime(df["작성일"])
    df["위도"] = df["위도"].astype(float)
    df["경도"] = df["경도"].astype(float)
else:
    df = pd.DataFrame()

# ----------------------------
# 1️ 작성자별 민원 검색
# ----------------------------
st.subheader("1️⃣ 작성자별 민원 검색")
writer_query = st.text_input("검색할 작성자 이름")

if writer_query:
    filtered = df[df["user"] == writer_query]
    if not filtered.empty:
        st.success(f"'{writer_query}'님의 민원 {len(filtered)}건이 검색되었습니다.")
        st.dataframe(filtered[["날짜", "내용", "유형", "위도", "경도"]])
    else:
        st.warning("해당 작성자의 민원이 없습니다.")

# ----------------------------
# 2️ 날짜별 민원 수 통계
# ----------------------------
st.markdown("---")
st.subheader("2️⃣ 날짜별 민원 접수 수")
if not df.empty:
    count_dict = count_by_date()
    count_series = pd.Series(count_dict)
    count_series.index = pd.to_datetime(count_series.index)
    count_series = count_series.sort_index()
    st.bar_chart(count_series)
else:
    st.info("표시할 민원이 없습니다")

# ----------------------------
# 3 전체 민원 지도 표시
# ----------------------------
st.markdown("---")
st.subheader("3️⃣ 전체 민원 지도 보기")

if not df.empty:
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)


    for _, row in df.iterrows():
        shortened = row["내용"][:20] + "..." if len(row["내용"]) > 20 else row["내용"]
        popup_text = f"""
        <b>{shortened}</b><br>
        {row['작성자']} / {row['유형']}
        """
        popup_html = folium.Popup(popup_text, max_width=300)

        folium.Marker(
            location=[row["위도"], row["경도"]],
            popup=popup_html,
            icon=folium.Icon(icon="info-sign", color="blue")
        ).add_to(m)


    st_folium(m, height=400, width=700)
else:
    st.info("표시할 민원이 없습니다.")

# 나중에 sample_data가 처리될 부분 
# from backend import load_all_complaints
# df = load_all_complaints()

