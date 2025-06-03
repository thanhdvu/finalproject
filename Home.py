import streamlit as st

st.set_page_config(
    page_title="민원 플랫폼 홈",
    page_icon="📌",
    layout="wide"
)

st.markdown("""Home""")
st.title ("📌 민원 신고 플랫폼에 오신 것을 환영합니다!")
st.markdown("""언어를 먼저 선택하고, 아래 버튼을 눌러 민원 신고를 시작해보세요!""")

lang = st.selectbox('Select Language / 언어 선택', ('Korean', 'English'))
st.session_state['lang'] = lang  

st.markdown ("---")

if lang == 'Korean':
    st.markdown("""
    ### 버튼을 눌러 민원 신고 플랫폼 이용하기! 
    """)
    st.page_link("pages/1_👀_How_To_Use.py", label="👀 플랫폼 사용법")
    st.page_link("pages/2_❗️_Submit_Complaint.py", label="❗ 민원 신고하기")
    st.page_link("pages/3_🔍_Search_Complaints.py", label="🔍 민원 검색하기")

else:
    st.markdown("""
    ### Click the buttons below to start reporting!
    """)
    st.page_link("pages/1_👀_How_To_Use.py", label="👀 How to Use")
    st.page_link("pages/2_❗️_Submit_Complaint.py", label="❗ Report Complaint")
    st.page_link("pages/3_🔍_Search_Complaints.py", label="🔍 Search Complaints")
