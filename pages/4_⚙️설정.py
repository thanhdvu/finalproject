import streamlit as st

st.set_page_config(page_title="설정")

st.title("⚙️ 설정")

# -----------------------------
# 언어 설정
# -----------------------------
st.subheader("🌐 언어 설정")

language = st.radio(
    "언어를 선택하세요:",
    ("한국어", "English"),
    horizontal=True
)

st.info(f"현재 선택된 언어는: **{language}** 입니다.")
# 실제 적용은 이후 다국어 처리 로직이 필요함 (예: st.session_state['lang'])

# -----------------------------
# 다크/라이트 모드 설정 (디자인 목적, 기능은 제한됨)
# -----------------------------
st.subheader("🌓 다크 / 라이트 모드")

theme_choice = st.selectbox(
    "화면 테마를 선택하세요:",
    ["기본 설정 (시스템)", "라이트 모드", "다크 모드"]
)

st.info(f"현재 선택된 테마: **{theme_choice}**")

st.markdown("---")

# -----------------------------
# 안내 메시지
# -----------------------------
st.markdown("🔔 *설정은 현재 세션에만 적용되며, 기능 구현은 시각적 안내용입니다.*")
