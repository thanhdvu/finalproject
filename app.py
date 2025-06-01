import streamlit as st
from frontend_kr import show_main_page_kr
from frontend_en import show_main_page_en

col1, col2 = st.columns([8,2])
with col2:
    lang_option = st.selectbox("", ["한국어", "English"], index=0)
    lang = "한국어" if "한국어" in lang_option else "English"
with col1:
    title_text = "✍️ 민원 접수를 시작해보세요!" if lang == "한국어" else "✍️  Submit Civil Complaints!"
    st.markdown(f"<h2>{title_text}</h2>", unsafe_allow_html=True)

if lang == "한국어":
    show_main_page_kr()
elif lang == "English":
    show_main_page_en()