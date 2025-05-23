import streamlit as st
import pydeck as pdk

def show_main_page():
    st.subheader("민원 접수를 시작해보세요!")

    # 처음 지도 위치 잡기 (서울임)
    default_lat, default_lon = 37.5665, 126.9780  

    st.markdown("지도를 클릭해 민원을 제보할 위치를 선택하세요.")
    clicked_location = st.empty()

    if "clicked_latlon" not in st.session_state:
        st.session_state.clicked_latlon = None

    # 지도 표시
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=pdk.ViewState(
            latitude=default_lat,
            longitude=default_lon,
            zoom=11,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=[],
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
        tooltip={"text": "지도에서 좌표를 선택하세요"},
    ))

    # 좌표 입력하기 
    lat = st.number_input("위도 (lat)", value=default_lat, format="%.6f")
    lon = st.number_input("경도 (lon)", value=default_lon, format="%.6f")

    if st.button("이 위치로 선택"):
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"선택된 위치: {lat:.6f}, {lon:.6f}")

    # 클릭된 좌표 보여주기
    if st.session_state.clicked_latlon:
        clicked_location.info(f"📍 현재 선택된 좌표: {st.session_state.clicked_latlon}")
