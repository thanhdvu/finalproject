import streamlit as st
from datetime import date, datetime
from backend import civil_complaint, submit_complaint
import pandas as pd
from collections import Counter
import pytz
import folium
from streamlit_folium import st_folium

#기본 사항 
default_lat, default_lon = 37.5665, 126.9780 #서울 
tooltip_max_length = 20 

def initialize_location(): 
    if "clicked_latlon" not in st.session_state:
        st.session_state.clicked_latlon = (default_lat, default_lon)
    
    if "civil_list" not in st.session_state:
        st.session_state.civil_list=[]

def get_selected_coordinates (output): 
    if output and output["last_clicked"]:
        lat = output["last_clicked"]["lat"]
        lon = output["last_clicked"]["lng"]
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"📍 선택된 위치: 위도 {lat:.6f}, 경도 {lon:.6f}")
    else:
        lat, lon = st.session_state.clicked_latlon
    return st.session_state.clicked_latlon 

def select_map(): 
    m = folium.Map(location=[default_lat, default_lon], zoom_start=13)
    m.add_child(folium.LatLngPopup())
    return st_folium(m, width="100%", height=500)

def show_map (): 
    st.subheader("📋 등록된 민원 목록")
    map_data = [
        {
            "lat": c.latitude,
            "lon": c.longitude,
            "tooltip": c.content[:tooltip_max_length] + "..."
        } for c in st.session_state.civil_list
    ]
    map_m = folium.Map(location=[default_lat, default_lon], zoom_start=11)
    for item in map_data:
        folium.Marker(
            location=[item["lat"], item["lon"]],
            tooltip=item["tooltip"]
        ).add_to(map_m)
    st_folium(map_m, width="100%", height=500)    

def show_main_page_kr():
    # 지도 표시 
    st.subheader("민원 접수를 시작해보세요!")

    initialize_location ()
    output = select_map ()
    lat, lon = get_selected_coordinates(output) 
    default_lat, default_lon = 37.5665, 126.9780

    lat = st.number_input("📍 위도 (Latitude)", value=st.session_state.clicked_latlon[0], format="%.6f")
    lon = st.number_input("📍 경도 (Longitude)", value=st.session_state.clicked_latlon[1], format="%.6f")

    #위치 선택 
    if st.button("이 위치로 선택"):
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"선택된 위치: 위도 {lat:.6f}, 경도 {lon:.6f}")

    # 민원 내용 입력 
    st.markdown("---")
    st.subheader("✍️ 민원 내용 입력")

    writer = st.text_input("작성자 이름")
    content = st.text_area("민원 내용")
    written_date = st.date_input("작성일", value=date.today())

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
                complaint = civil_complaint(writer, content, lat, lon, written_date)
                st.session_state.civil_list.append(complaint) 
                submit_complaint(user=writer, content=content, latitude=lat, longitude=lon, created_date=written_date)
                seoul_tz = pytz.timezone('Asia/Seoul')
                submit_time = datetime.now(seoul_tz).strftime('%Y-%m-%d %H:%M:%S') # 현재 시간을 한국 표준시로 가져오기
                st.success(f"✅ 민원이 등록되었습니다. (제출 시간: {submit_time})")
            except Exception as e: 
                st.error(f"❎ 민원 등록 실패 - 다시 입력해주세요")
        else:
            st.warning("작성자와 내용을 모두 입력하세요.")
            
    #등록된 민원 지도로 보기  
    st.markdown("---")
    st.subheader("📋 등록된 민원 목록")

    if st.session_state.civil_list:
        for c in st.session_state.civil_list:
            st.write(str(c))
        show_map ()
    else:
        st.info("아직 등록된 민원이 없습니다.")

    #작성자별 민원 조회
    st.markdown("---")
    st.subheader("🔍 작성자별 민원 조회")

    query_user = st.text_input("조회할 작성자 이름 입력")

    if st.button("조회"):
        filtered = [c for c in st.session_state.civil_list if c.user == query_user]
        if filtered:
            st.success(f"✅ '{query_user}'님의 민원 {len(filtered)}건")
            for c in filtered:
                st.write(str(c))
        else:
            st.info("해당 작성자의 민원이 없습니다.")

    #날짜별 민원 조회 
    st.markdown("---")
    st.subheader("📊 날짜별 민원 접수 추이")
    date_list = [c.created_date for c in st.session_state.civil_list]
    date_counts = Counter(date_list)
    chart_data = pd.DataFrame(date_counts.items(), columns=["날짜", "민원수"]).sort_values("날짜")

    if not chart_data.empty:
        st.bar_chart(chart_data.set_index("날짜"))
    else:
        st.info("시각화할 민원이 없습니다.")

