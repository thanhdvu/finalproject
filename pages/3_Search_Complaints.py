import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import date
from sheets_oauth import load_all_complaints, filter_by_author, count_by_date

st.set_page_config(page_title="🔍 민원 검색하기 | Search Complaints")

lang = st.session_state.get('lang', 'Korean')

if lang == 'Korean':
    st.title("🔍 민원 검색하기")
else:
    st.title("🔍 Search Complaints")

#데이터 불러오기 (구글 시트에서)
raw_data = load_all_complaints()

if raw_data:
    df = pd.DataFrame(raw_data, columns=["작성자", "내용", "위도", "경도", "작성일", "제출 시간", "민원 종류"])
    df["작성일"] = pd.to_datetime(df["작성일"])
    df["위도"] = df["위도"].str.replace(",", ".").astype(float)
    df["경도"] = df["경도"].str.replace(",", ".").astype(float)
else:
    df = pd.DataFrame()

# ----------------------------
# 1️ 작성자별 민원 검색
# ----------------------------
if lang == 'Korean':
    st.subheader("1️⃣ 작성자별 민원 검색")
    writer_query = st.text_input("검색할 작성자 이름")
else:
    st.subheader("1️⃣ Search by Author")
    writer_query = st.text_input("Enter author name to search")

if writer_query:
    filtered = df[df["작성자"] == writer_query]
    if not filtered.empty:
        if lang == 'Korean':
            st.success(f"'{writer_query}'님의 민원 {len(filtered)}건이 검색되었습니다.")
        else:
            st.success(f"{len(filtered)} complaints found for '{writer_query}'.")
        st.dataframe(filtered[["작성일", "내용", "민원 종류", "위도", "경도"]])
    else:
        st.warning("해당 작성자의 민원이 없습니다." if lang == 'Korean' else "No complaints found for this author.")

# ----------------------------
# 2️ 날짜별 민원 수 통계
# ----------------------------
st.markdown("---")
st.subheader("2️⃣ 날짜별 민원 접수 수" if lang == 'Korean' else "2️⃣ Number of Complaints by Date")
if not df.empty:
    count_dict = count_by_date()
    count_series = pd.Series(count_dict)
    count_series.index = pd.to_datetime(count_series.index)
    count_series = count_series.sort_index()
    st.bar_chart(count_series)
else:
    st.info("표시할 민원이 없습니다." if lang == 'Korean' else "No complaints to display.")

# ----------------------------
# 3 전체 민원 지도 표시
# ----------------------------
st.markdown("---")
st.subheader("3️⃣ 전체 민원 지도 보기" if lang == 'Korean' else "3️⃣ View All Complaints on Map")

info_box = st.empty()

if not df.empty:
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)


    for _, row in df.iterrows():
        shortened = row["내용"][:20] + "..." if len(row["내용"]) > 20 else row["내용"]
        popup_text = f"""
        <b>{shortened}</b><br>
        {row['작성자']} / {row['민원 종류']}
        """
        popup_html = folium.Popup(popup_text, max_width=300)

        folium.Marker(
            location=[row["위도"], row["경도"]],
            popup=popup_html,
            icon=folium.Icon(icon="info-sign", color="blue")
        ).add_to(m)


    st_folium(m, height=400, width=700)
else:
    st.info("표시할 민원이 없습니다." if lang == 'Korean' else "No complaints to display.")

if lang == 'Korean':
    st.markdown("---") 
    st.subheader("다른 페이지로 이동 👉🏻")
    st.page_link("Home.py", label="홈 페이지", icon="🏠")
    st.page_link("pages/1_How_To_Use.py", label="플랫폼 사용법", icon="👀")
    st.page_link("pages/2_Submit_Complaint.py", label="민원 신고하기", icon="❗")
    st.page_link("pages/3_Search_Complaints.py", label="민원 검색하기", icon="🔍")

else:
    st.markdown("---")
    st.subheader("Go to other pages 👉🏻")
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/1_How_To_Use.py", label="How to Use", icon="👀")
    st.page_link("pages/2_Submit_Complaint.py", label="Report Complaint", icon="❗")
    st.page_link("pages/3_Search_Complaints.py", label="Search Complaints", icon="🔍")