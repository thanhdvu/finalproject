import streamlit as st

st.set_page_config(
    page_title="민원 플랫폼 홈",
    page_icon="📌",
    layout="wide"
)

lang = st.sidebar.selectbox('Select Language / 언어 선택', ('Korean', 'English'))
st.session_state['lang'] = lang  

if lang == 'Korean':
    st.title("📌 민원 신고 플랫폼")
    st.markdown("""
    ### 주민의 불편함을 손쉽게 신고하고, 함께 해결해요!
    아래 버튼을 눌러 민원 신고를 시작해보세요!
    """)
    st.page_link("pages/1_👀민원_사용법_-_How_to_Use.py", label="👀 민원 사용법 - How to Use")
    st.page_link("pages/2_❗️민원_신고하기_-_Report_a_Complaint.py", label="❗ 민원 신고하기 - Report a Complaint")
    st.page_link("pages/3_🔍민원_검색하기_-_Search_Complaints.py", label="🔍 민원 검색하기 - Search Complaints")

else:
    st.title("📌 Complaint Reporting Platform")
    st.markdown("""
    ### Easily report residents' inconveniences and solve them together!
    Click the buttons below to start reporting!
    """)
    st.page_link("pages/1_👀민원_사용법_-_How_to_Use.py", label="👀 민원 사용법 - How to Use")
    st.page_link("pages/2_❗️민원_신고하기_-_Report_a_Complaint.py", label="❗ 민원 신고하기 - Report a Complaint")
    st.page_link("pages/3_🔍민원_검색하기_-_Search_Complaints.py", label="🔍 민원 검색하기 - Search Complaints")
