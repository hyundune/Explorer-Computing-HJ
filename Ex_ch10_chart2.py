import streamlit as st
import pandas as pd
import pydeck as pdk

# 위도, 경도 데이터 준비
data = pd.DataFrame({
    'city': ['Seoul', 'Daejeon', 'Gwangju', 'Mokpo', 'Busan', 'Daegu'],
    'lat': [37.5665, 36.3504, 35.1595, 34.8110, 35.1796, 35.8714],
    'lon': [126.9780, 127.3845, 126.8526, 126.3925, 129.0756, 128.6014],
    'population': [9700000, 1500000, 1500000, 240000, 3400000, 2400000]    
})

st.write("📍 한국 주요 도시 위치")
st.map(data) 

# 3. Pydeck Chart
st.subheader("PyDeck Chart (st.pydeck_chart)")
layer = pdk.Layer(
    "ScatterplotLayer",  #점(원형 마커)을 표시
    data=data,
    get_position="[lon, lat]",
    get_radius=5000,  #점(원의 반지름)을 미터 단위로 지정. 5000이면 지상에서 약 5km 반경의 원으로 보임
    get_color=[255, 0, 0],
    pickable=True  #마우스로 점을 클릭했을 때 툴팁(정보창) 을 표시
)

# 툴팁 설정
tooltip = {
    "text": "도시: {city}\n인구: {population}",
    "style": {"color": "white"}
}

# 대한민국 전체가 보이는 위치로 설정
view_state = pdk.ViewState(
    latitude=36.5,  #지도의 중심 위도(lat), 36.5는 한반도의 대략적인 중앙 위도
    longitude=127.8, #지도의 중심 경도(lon), 127.8은 한국의 대략적인 중앙 경도
    zoom=6,
    pitch=0  # 지도를 기울이는 각도 0은 정면
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))
