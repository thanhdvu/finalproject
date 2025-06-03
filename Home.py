import streamlit as st

st.set_page_config(
    page_title="민원 플랫폼 홈",
    page_icon="📌",
    layout="wide"
)

st.markdown("""Home""")
st.title ("📌 민원 신고 플랫폼에 오신 것을 환영합니다!")
st.markdown("""
### 1. 언어를 선택해주세요/ Select Language. 
""")

lang = st.selectbox('Select Language / 언어 선택', ('Korean', 'English'))
st.session_state['lang'] = lang  

st.markdown ("---")

if lang == 'Korean':
    st.markdown("""
    ### 2. 버튼을 눌러 민원 신고 플랫폼을 이용해주세요 
    """)
    st.page_link("Home.py", label="홈 페이지", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="플랫폼 사용법", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="민원 신고하기", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="민원 검색하기", icon="🔍")

else:
    st.markdown("""
    ### Click the buttons below to start reporting!
    """)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="How to Use", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="Report Complaint", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="Search Complaints", icon="🔍")

