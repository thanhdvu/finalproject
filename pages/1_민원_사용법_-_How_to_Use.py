import streamlit as st

st.set_page_config(page_title="👀 민원 사용법 | How to Use", layout="wide")

lang = st.session_state.get('lang', 'Korean')

if lang == 'Korean':

    st.title("👀 민원 사용법")
    st.markdown("민원 신고 플랫폼의 각 기능을 아래와 같이 사용할 수 있어요! 사이드바와 버튼 클릭을 통해 각 페이지로 이동하세요!")
    
    st.markdown("---")

    st.subheader("❗️민원 신고하기")
    st.markdown("""
    - **지도 클릭**을 통해 민원 위치를 위도/경도로 지정할 수 있어요.
    - 작성자의 **이름**, **내용**, **날짜**를 입력하면 민원이 등록되어요.
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
    - **언어 설정**: 홈페이지에서 언어를 선택할 수 있어요. 
    - **화면 모드**: 우측 상단 점 세개를 누르고 설정(*Setting*)에 들어가면 다크모드/라이트모드를 선택할 수 있어요. 
    """)
    
    st.markdown("---")

    st.subheader("🔘 버튼 사용하기")
    st.markdown("""
    - 각 페이지 하단에 있는 **버튼**을 클릭하면 다른 페이지로 이동이 가능해요. 
    - 민원 신고 플랫폼에서 다양한 기능을 사용해 보세요!
    """)

    st.markdown("---") 
    st.subheader("다른 페이지로 이동 👉🏻")

    st.page_link("Home.py", label="홈 페이지", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="플랫폼 사용법", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="민원 신고하기", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="민원 검색하기", icon="🔍")

else:
    st.title("👀 How to Use")
    st.markdown("You can use each feature of the Complaint Reporting Platform as follows! Navigate to each page via the sidebar!")

    st.markdown("---")

    st.subheader("❗️ Report a Complaint")
    st.markdown("""
    - You can specify the location of the complaint using **map clicks** with latitude/longitude.
    - Enter **author's name**, **details**, and **date** to submit a complaint.
    - All these features are available on the **'Report a Complaint' page**.
    """)

    st.markdown("---")

    st.subheader("🔍 Search Complaints")
    st.markdown("""
    - You can **search by author name** to find complaints submitted by a specific user.
    - All complaints are **displayed on the map as markers**, and you can click to view details.
    - **Complaint statistics by date** are also available for analysis.
    """)

    st.markdown("---")

    st.subheader("⚙️ Settings")
    st.markdown("""
    - **Language Setting**: You can select the language on the 'Home' page. Please note that the language will reset to Korean (default) when you return to the homepage or refresh the page.
    - **Display Mode**: Click the three dots at the top right and go to *Settings* to switch between Dark Mode and Light Mode.
    """)

    st.markdown("---")

    st.subheader("🔘 Using Buttons")
    st.markdown("""
    - You can click the **buttons** at the bottom of each page to navigate to other sections.
    - Explore the various features of the Civil Complaint Platform!
    """)

    #버튼 
    st.markdown("---")
    st.subheader("Go to other pages 👉🏻")
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/1_민원_사용법_-_How_to_Use.py", label="How to Use", icon="👀")
    st.page_link("pages/2_민원_신고하기_-_Report_a_Complaint.py", label="Report Complaint", icon="❗")
    st.page_link("pages/3_민원_검색하기_-_Search_Complaints.py", label="Search Complaints", icon="🔍")

