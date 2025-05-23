import streamlit as st
from frontend import show_main_page

st.set_page_config(page_title="민원 신고 플랫폼", layout="wide")

def main():
    st.title("📌 우리 동네 민원 신고 플랫폼")
    show_main_page()

if __name__ == "__main__":
    main()
