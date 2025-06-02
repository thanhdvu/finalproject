import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import date
from collections import Counter

st.set_page_config(page_title="민원 검색하기")
st.title("🔎 민원 검색하기")

# 📌 임시 샘플 데이터 (나중에 load_all_complaints()로 대체)
sample_data = [
    {"작성자": "홍길동", "내용": "도로 파손", "위도": 37.5665, "경도": 126.9780, "유형": "시설/안전", "날짜": "2025-06-01"},
    {"작성자": "김민지", "내용": "소음 문제", "위도": 37.565, "경도": 126.977, "유형": "소음/교통", "날짜": "2025-06-01"},
    {"작성자": "홍길동", "내용": "쓰레기 방치", "위도": 37.564, "경도": 126.979, "유형": "생활환경", "날짜": "2025-06-02"},
]
df = pd.DataFrame(sample_data)
df["날짜"] = pd.to_datetime(df["날짜"])

# ----------------------------
# 1️⃣ 작성자별 민원 검색
# ----------------------------
st.subheader("1️⃣ 작성자별 민원 검색")
writer_query = st.text_input("검색할 작성자 이름")

if writer_query:
    filtered = df[df["작성자"] == writer_query]
    if not filtered.empty:
        st.success(f"'{writer_query}'님의 민원 {len(filtered)}건이 검색되었습니다.")
        st.dataframe(filtered[["날짜", "내용", "유형", "위도", "경도"]])
    else:
        st.warning("해당 작성자의 민원이 없습니다.")

# ----------------------------
# 2️⃣ 날짜별 민원 수 통계
# ----------------------------
st.markdown("---")
st.subheader("2️⃣ 날짜별 민원 접수 수")
if not df.empty:
    count_by_date = df["날짜"].value_counts().sort_index()
    st.bar_chart(count_by_date)
else:
    st.info("표시할 데이터가 없습니다.")

# ----------------------------
# 3️⃣ 전체 민원 지도 표시
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

