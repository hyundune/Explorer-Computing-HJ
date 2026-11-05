import streamlit as st
import pandas as pd
import pydeck as pdk

# 삿포로 위치 데이터
data = pd.DataFrame({
    'place': ['Sapporo'],
    'lat': [43.0618],
    'lon': [141.3545]
})

st.write("📍 내가 가보고 싶은 장소: 일본 삿포로")

# 기본 지도
st.map(data)

# PyDeck Chart
st.subheader("삿포로 위치 (st.pydeck_chart)")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[lon, lat]",
    get_radius=3000,
    get_color=[255, 0, 0],
    pickable=True
)

# 마우스를 올렸을 때 표시될 정보
tooltip = {
    "text": "장소: {place}",
    "style": {"color": "white"}
}

# 삿포로를 지도의 중심으로 설정
view_state = pdk.ViewState(
    latitude=43.0618,
    longitude=141.3545,
    zoom=9,
    pitch=0
)

st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip
    )
)
