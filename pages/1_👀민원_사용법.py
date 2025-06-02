import streamlit as st

st.set_page_config(page_title="민원 사용법")

st.title("👀 민원 사용법")
st.markdown("민원 신고 플랫폼의 각 기능을 아래와 같이 사용할 수 있어요! 사이드바를 통해 각 페이지로 이동하세요!")

st.markdown("---")

st.subheader("❗️민원 신고하기")
st.markdown("""
- **지도 클릭**을 통해 민원 위치를 위도/경도로 지정할 수 있어요.
- 작성자의 **이름**, **내용**, **날짜**를 입력하면 민원이 등록됩니다.
- **'민원 신고하기' 페이지**에서 이 모든 기능을 사용할 수 있어요.
""")

st.markdown("---")

st.subheader("🔍 민원 검색하기")
st.markdown("""
- 민원 **작성자 이름을 입력하면** 해당 사용자가 작성한 민원을 검색할 수 있어요.
- 전체 민원들이 **지도에 마커로 표시**되며, 클릭하면 내용을 확인할 수 있어요.
- **날짜별 민원 통계**도 함께 제공되어 분석이 가능해요.
""")

st.markdown("---")

st.subheader("⚙️ 설정")
st.markdown("""
- 플랫폼의 **언어 설정**을 변경할 수 있어요.
- **다크 모드 / 라이트 모드** 전환도 이 페이지에서 가능합니다.
""")


st.markdown("---") 
st.subheader("다른 페이지로 이동 👉🏻")


st.page_link("Home.py", label="민원 사용법", icon="🏠")
st.page_link("pages/2_❗️민원_신고하기.py", label="민원 신고하기", icon="❗️")
st.page_link("pages/3_🔍민원_검색하기.py", label="민원 검색하기", icon="🔍")
st.page_link("pages/4_⚙️설정.py", label="설정", icon="⚙️")
