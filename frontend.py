import streamlit as st
import pydeck as pdk

def show_main_page():
    st.subheader("민원 접수를 시작해보세요!")

    # 기본 위치: 서울
    default_lat, default_lon = 37.5665, 126.9780

    # 좌표 상태 초기화
    if "clicked_latlon" not in st.session_state:
        st.session_state.clicked_latlon = (default_lat, default_lon)

    # 선택된 위치를 지도에 표시할 데이터로 구성
    marker_data = [{
        "lat": st.session_state.clicked_latlon[0],
        "lon": st.session_state.clicked_latlon[1]
    }]

    # 지도 표시 (마커 포함)
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',  # 스타일은 light 또는 None으로
        initial_view_state=pdk.ViewState(
            latitude=st.session_state.clicked_latlon[0],
            longitude=st.session_state.clicked_latlon[1],
            zoom=15,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=marker_data,
                get_position='[lon, lat]',
                get_color='[255, 0, 0, 160]',
                get_radius=100,
            ),
        ],
        tooltip={"text": "선택한 위치입니다."},
    ))
    # 수동 입력 받기
    lat = st.number_input("📍 위도 (Latitude)", value=st.session_state.clicked_latlon[0], format="%.6f")
    lon = st.number_input("📍 경도 (Longitude)", value=st.session_state.clicked_latlon[1], format="%.6f")

    # 좌표 선택 버튼
    if st.button("이 위치로 선택"):
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"선택된 위치: 위도 {lat:.6f}, 경도 {lon:.6f}")