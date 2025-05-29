import streamlit as st
import pydeck as pdk
from datetime import date, datetime
from backend import civil_complaint, submit_complaint
import pandas as pd
from collections import Counter
import pytz

def show_main_page_en():

    default_lat, default_lon = 37.5665, 126.9780

    if "clicked_latlon" not in st.session_state:
        st.session_state.clicked_latlon = (default_lat, default_lon)
    
    if "civil_list" not in st.session_state:
        st.session_state.civil_list=[]

    map_data = [{
    "lat": c.latitude,
    "lon": c.longitude,
    "text": c.content[:20] + "..."
    } for c in st.session_state.civil_list]
    
    st.subheader("🗺️ Map of Complaint Locations")
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
                pickable=True
            )
        ],
        tooltip={"text": "{text}"}
    ))

    lat = st.number_input("📍 Latitude", value=st.session_state.clicked_latlon[0], format="%.6f")
    lon = st.number_input("📍 Longitude", value=st.session_state.clicked_latlon[1], format="%.6f")

    if st.button("Select this Location"):
        st.session_state.clicked_latlon = (lat, lon)
        st.success(f"Selected Location: Latitude {lat:.6f}, Longitude {lon:.6f}")

    st.markdown("---")
    st.subheader("✍️ Enter Complaint Details")

    writer = st.text_input("Writer's Name")
    content = st.text_area("Complaint Content")
    written_date = st.date_input("Date of Submission", value=date.today())

    if st.button("Preview Complaint"):
        if writer and content:
            st.success("✅ Complaint Preview")
            st.write(f"**Writer:** {writer}")
            st.write(f"**Content:** {content}")
            st.write(f"**Date:** {written_date}")
            st.write(f"**Location:** Latitude {st.session_state.clicked_latlon[0]:.6f}, Longitude {st.session_state.clicked_latlon[1]:.6f}")
        else:
            st.warning("Please enter both writer and content.")

    if st.button("Submit Complaint"):
        if writer and content:
            try:
                complaint = civil_complaint(writer, content, lat, lon, written_date)
                st.session_state.civil_list.append(complaint)
                submit_complaint(writer, content, lat, lon, written_date)
                seoul_tz = pytz.timezone('Asia/Seoul')
                submit_time = datetime.now(seoul_tz).strftime('%Y-%m-%d %H:%M:%S')
                st.success(f"✅ Complaint submitted successfully. (Submission Time: {submit_time})")
            except Exception as e:
                st.error(f"❎ Submission failed. Please try again.")
        else:
            st.warning("Please enter both writer and content.")

    st.markdown("---")
    st.subheader("📋 List of Registered Complaints")
    if st.session_state.civil_list:
        for c in st.session_state.civil_list:
            st.write(str(c))
        map_data = [{"lat": c.latitude, "lon": c.longitude} for c in st.session_state.civil_list]
        st.subheader("🗺️ Map of Complaint Locations")
        st.pydeck_chart(pdk.Deck(
            map_style='light',
            initial_view_state=pdk.ViewState(latitude=default_lat, longitude=default_lon, zoom=11),
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
        st.info("No complaints have been registered yet.")

    st.markdown("---")
    st.subheader("🔍 Search Complaints by Writer")
    query_user = st.text_input("Enter writer's name to search")
    if st.button("Search"):
        filtered = [c for c in st.session_state.civil_list if c.user == query_user]
        if filtered:
            st.success(f"✅ {len(filtered)} complaints found for '{query_user}'")
            for c in filtered:
                st.write(str(c))
        else:
            st.info("No complaints found for this writer.")

    st.markdown("---")
    st.subheader("📊 Complaint Trends by Date")
    date_list = [c.created_date for c in st.session_state.civil_list]
    date_counts = Counter(date_list)
    chart_data = pd.DataFrame(date_counts.items(), columns=["Date", "Number of Complaints"]).sort_values("Date")
    if not chart_data.empty:
        st.bar_chart(chart_data.set_index("Date"))
    else:
        st.info("No data available for visualization.")