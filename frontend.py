import streamlit as st
import pydeck as pdk
from datetime import date 
from backend import civil_complaint, submit_complaint
import pandas as pd
from collections import Counter

def show_main_page():
    st.subheader("민원 접수를 시작해보세요!")

    # 기본 위치: 서울
    default_lat, default_lon = 37.5665, 126.9780

    # 좌표 상태 초기화
    if "clicked_latlon" not in st.session_state:
        st.session_state.clicked_latlon = (default_lat, default_lon)
    
    if "civil_list" not in st.session_state:
        st.session_state.civil_list=[]

    # 선택된 위치를 지도에 표시할 데이터로 구성
    marker_data = [{
        "lat": st.session_state.clicked_latlon[0],
        "lon": st.session_state.clicked_latlon[1]
    }]

    # 지도 표시 (마커 포함)
    map_data = [{
    "lat": c.latitude,
    "lon": c.longitude,
    "text": c.content[:20] + "..." 
    } for c in st.session_state.civil_list]
    
    st.subheader("🗺️ 민원 위치 지도")
    st.pydeck_chart(pdk.Deck(
        map_style='light',
        initial_view_state=pdk.ViewState(
            latitude=default_lat,
            longitude=default_lon,
            zoom=11
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=map_data,
                get_position='[lon, lat]',
                get_fill_color='[0, 0, 255, 160]',
                get_radius=120,
                pickable=True  # ✅ 툴팁 활성화 위해 꼭 필요
            )
        ],
        tooltip={"text": "{text}"}  # ✅ text 필드를 툴팁으로 지정
    ))

    # 수동 입력 받기
    lat = st.number_input("📍 위도 (Latitude)", value=st.session_state.clicked_latlon[0], format="%.6f")
    lon = st.number_input("📍 경도 (Longitude)", value=st.session_state.clicked_latlon[1], format="%.6f")

    # 좌표 선택 버튼
    if st.button("이 위치로 선택"):
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"선택된 위치: 위도 {lat:.6f}, 경도 {lon:.6f}")

    st.markdown("---")
    st.subheader("✍️ 민원 내용 입력")

    # 민원 작성 폼
    writer = st.text_input("작성자 이름")
    content = st.text_area("민원 내용")
    written_date = st.date_input("작성일", value=date.today())

    # 제출 후 미리보기 출력
    if st.button("민원 미리보기"):
        if writer and content:
            st.success("✅ 민원 미리보기")
            st.write(f"**작성자:** {writer}")
            st.write(f"**내용:** {content}")
            st.write(f"**작성일:** {written_date}")
            st.write(f"**위치:** 위도 {st.session_state.clicked_latlon[0]:.6f}, 경도 {st.session_state.clicked_latlon[1]:.6f}")
        else:
            st.warning("작성자와 내용을 모두 입력하세요.")
            
    if st.button("민원 등록"):
        if writer and content:
            try: 
                complaint = civil_complaint(writer, content, lat, lon, written_date)
                st.session_state.civil_list.append(complaint) 
                submit_complaint(user=writer, content=content, latitude=lat, longitude=lon, created_date=written_date)
                st.success("✅ 민원이 등록되었습니다.")
            except Exception as e: 
                st.error(f"❎ 민원 등록 실패 - 다시 입력해주세요")
        else:
            st.warning("작성자와 내용을 모두 입력하세요.")
            
        st.markdown("---")
        st.subheader("📋 등록된 민원 목록")

        if st.session_state.civil_list:
            for c in st.session_state.civil_list:
                st.write(str(c))

            # 지도에 모든 민원 위치 마커 표시
            map_data = [{"lat": c.latitude, "lon": c.longitude} for c in st.session_state.civil_list]

            st.subheader("🗺️ 민원 위치 지도")
            st.pydeck_chart(pdk.Deck(
                map_style='light',
                initial_view_state=pdk.ViewState(
                    latitude=default_lat, longitude=default_lon, zoom=11),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_data,
                        get_position='[lon, lat]',
                        get_color='[0, 0, 255, 160]',
                        get_radius=120,
                    ),
                ]
            ))
        else:
            st.info("아직 등록된 민원이 없습니다.")

    #민원 조회
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



    # 각 날짜별 민원 수 
    st.markdown("---")
    st.subheader("📊 날짜별 민원 접수 추이")

    date_list = [c.created_date for c in st.session_state.civil_list]

    date_counts = Counter(date_list)

    chart_data = pd.DataFrame(date_counts.items(), columns=["날짜", "민원수"]).sort_values("날짜")

    if not chart_data.empty:
        st.bar_chart(chart_data.set_index("날짜"))
    else:
        st.info("시각화할 민원이 없습니다.")

