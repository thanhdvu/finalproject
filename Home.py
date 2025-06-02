import streamlit as st

st.set_page_config(
    page_title="민원 플랫폼 홈",
    page_icon="📌",
    layout="wide"
)

st.title("📌 민원 신고 플랫폼")
st.markdown("""
### 주민의 불편함을 손쉽게 신고하고, 함께 해결해요!
아래 버튼을 눌러 민원 신고를 시작해보세요!.
""")

st.page_link("pages/1_👀민원_사용법.py", label="민원 사용법", icon="👀")
st.page_link("pages/2_❗️민원_신고하기.py", label="민원 신고하기", icon="❗️")
st.page_link("pages/3_🔍민원_검색하기.py", label="민원 검색하기", icon="🔍")
st.page_link("pages/4_⚙️설정.py", label="설정", icon="⚙️")

# import streamlit as st
# from frontend_kr import show_main_page_kr
# from frontend_en import show_main_page_en

# col1, col2 = st.columns([8,2])
# with col2:
#     lang_option = st.selectbox("", ["한국어", "English"], index=0)
#     lang = "한국어" if "한국어" in lang_option else "English"
# with col1:
#     title_text = "✍️ 민원 접수를 시작해보세요!" if lang == "한국어" else "✍️  Submit Civil Complaints!"
#     st.markdown(f"<h2>{title_text}</h2>", unsafe_allow_html=True)

# if lang == "한국어":
#     show_main_page_kr()
# elif lang == "English":
#     show_main_page_en()
