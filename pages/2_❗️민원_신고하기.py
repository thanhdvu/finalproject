import streamlit as st
from streamlit_folium import st_folium
import folium
from datetime import date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import submit_complaint

st.set_page_config(page_title="민원 신고하기")

st.title("❗️ 민원 신고하기")
st.markdown("지도를 클릭해서 민원 위치를 선택하고, 아래 양식을 작성해 주세요.")

# 기본 지도 위치 (서울 시청)
default_lat, default_lon = 37.5665, 126.9780

# 지도 클릭 상태 저장
if "clicked_latlon" not in st.session_state:
    st.session_state.clicked_latlon = (default_lat, default_lon)

# 지도 생성
m = folium.Map(location=[default_lat, default_lon], zoom_start=12)
m.add_child(folium.LatLngPopup())

clicked = st_folium(m, height=400, width="100%")

if clicked and clicked["last_clicked"]:
    lat = clicked["last_clicked"]["lat"]
    lon = clicked["last_clicked"]["lng"]
    st.session_state.clicked_latlon = (lat, lon)

# 현재 좌표 표시
lat, lon = st.session_state.clicked_latlon
st.info(f"선택된 위치: 위도 {lat:.5f}, 경도 {lon:.5f}")

        

# 민원 내용 입력 
st.markdown("---")
st.subheader("✍️ 민원 내용 입력")

writer = st.text_input("작성자 이름")
content = st.text_area("민원 내용")
written_date = st.date_input("작성일", value=date.today())
complaint_type=st.selectbox("민원 유형", ["생활환경", "시설/안전", "소음/교통"])

#미리보기 
if st.button("민원 미리보기"):
    if writer and content:
        st.success("✅ 민원 미리보기")
        st.write(f"**작성자:** {writer}")
        st.write(f"**내용:** {content}")
        st.write(f"**작성일:** {written_date}")
        st.write(f"**위치:** 위도 {st.session_state.clicked_latlon[0]:.6f}, 경도 {st.session_state.clicked_latlon[1]:.6f}")
    else:
        st.warning("작성자와 내용을 모두 입력하세요.")

#민원 등록  
if st.button("민원 등록"):
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
            st.success("✅ 민원이 등록되었습니다")
        except Exception as e:
            st.error(f"❌ 민원 등록 실패: {e}")
    else:
        st.warning("작성자와 내용을 모두 입력하세요.")