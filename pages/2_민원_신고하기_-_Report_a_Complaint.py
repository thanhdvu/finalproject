import streamlit as st
from streamlit_folium import st_folium
import folium
from datetime import date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import submit_complaint, civil_complaint

st.set_page_config(page_title="❗️ 민원 신고하기 | Report a Complaint", layout="wide")

lang = st.session_state.get('lang', 'Korean')

if lang == 'Korean':
    st.title("❗️ 민원 신고하기",)
    st.markdown("지도를 클릭해서 민원 위치를 선택하고, 아래 양식을 작성해 주세요.")
else:
    st.title("❗️ Report a Complaint")
    st.markdown("Click on the map to select the complaint location, and fill out the form below.")

# 기본 지도 위치 (서울 시청)
default_lat, default_lon = 37.5665, 126.9780

# 지도 클릭 상태 저장
if "clicked_latlon" not in st.session_state:
    st.session_state.clicked_latlon = (default_lat, default_lon)

# 지도를 보여준다. 
m = folium.Map(location=[default_lat, default_lon], zoom_start=12)
m.add_child(folium.LatLngPopup())


clicked = st_folium(m, height=400, width="100%")

info_box = st.empty()

if clicked and clicked.get("last_clicked"):
    lat = clicked["last_clicked"]["lat"]
    lon = clicked["last_clicked"]["lng"]
    st.session_state.clicked_latlon = (lat, lon)
    if lang == 'Korean':
        st.info(f"선택된 위치: 위도 {lat:.5f}, 경도 {lon:.5f}")
    else:
        st.info(f"Selected location: Latitude {lat:.5f}, Longitude {lon:.5f}")

# 현재 좌표 표시
lat, lon = st.session_state.clicked_latlon

# 민원 내용 입력 
st.markdown("---")
if lang == 'Korean':
    st.subheader("✍️ 민원 내용 입력")
    writer = st.text_input("작성자 이름")
    content = st.text_area("민원 내용")
    written_date = st.date_input("작성일", value=date.today())
    complaint_type = st.selectbox("민원 유형", ["생활환경", "시설/안전", "소음/교통"])
    preview_button = "민원 미리보기"
    submit_button = "민원 등록"
    preview_success = "✅ 민원 미리보기"
    preview_warning = "작성자와 내용을 모두 입력하세요."
    submit_success = "✅ 민원이 등록되었습니다"
    submit_fail = "❌ 민원 등록 실패"
else:
    st.subheader("✍️ Enter Complaint Details")
    writer = st.text_input("Author's Name")
    content = st.text_area("Complaint Content")
    written_date = st.date_input("Date of Submission", value=date.today())
    complaint_type = st.selectbox("Type of Complaint", ["Living Environment", "Facilities/Safety", "Noise/Traffic"])
    preview_button = "Preview Complaint"
    submit_button = "Submit Complaint"
    preview_success = "✅ Complaint Preview"
    preview_warning = "Please enter both the author's name and the content."
    submit_success = "✅ Complaint submitted successfully"
    submit_fail = "❌ Failed to submit complaint"

#미리보기 
if st.button(preview_button):
    if writer and content:
        st.success(preview_success)
        st.write(f"**작성자 / Author:** {writer}")
        st.write(f"**내용 / Content:** {content}")
        st.write(f"**작성일 / Date:** {written_date}")
        st.write(f"**위치 / Location:** 위도 {lat:.6f}, 경도 {lon:.6f}")

        preview = civil_complaint(
            user=writer,
            content=content,
            latitude=st.session_state.clicked_latlon[0],
            longitude=st.session_state.clicked_latlon[1],
            complaint_type=complaint_type,
            created_date=written_date
        )
        st.text(str(preview))

    else:
        st.warning(preview_warning)

#민원 등록  
if st.button(submit_button):
    if writer and content:
        try:
            submit_complaint(
                user=writer,
                content=content,
                latitude=lat,
                longitude=lon,
                complaint_type=complaint_type,
                created_date=written_date
            )
            st.success(submit_success)
        except Exception as e:
            st.error(f"{submit_fail}: {e}")
    else:
        st.warning(preview_warning)



if lang == 'Korean':
    st.markdown("---") 
    st.subheader("다른 페이지로 이동 👉🏻")
    st.page_link("Home.py", label="홈 페이지", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="플랫폼 사용법", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="민원 신고하기", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="민원 검색하기", icon="🔍")

else:
    st.markdown("---")
    st.subheader("Go to other pages 👉🏻")
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="How to Use", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="Report Complaint", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="Search Complaints", icon="🔍")