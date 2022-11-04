# python -m streamlit run C:\Users\USER\Documents\GitHub\optimizer\streamlit_app.py
import streamlit as st
import pandas as pd
import pydeck as pdk
st.set_page_config(layout='wide')

st.title('시니어 프렌드')
st.header('This is header')
st.balloons()

# 데이터 받아오기
dolbom = pd.read_csv("./data/노인맞춤돌봄서비스_수행기관현황.csv")
chimae = pd.read_csv("./data/전국치매센터표준데이터.csv")
job = pd.read_csv("./data/일자리끝.csv")


# 홈
def home():
    # 데이터 처리
    sido = dolbom["시도"].unique().tolist()
    sido2 = chimae["시도"].unique().tolist()
    sido3 = job["시도"].unique().tolist()
    sido = list(set.union(set(sido), set(sido2), set(sido3)))
    region = st.sidebar.selectbox("지역을 선택하세요: ", sido )
    dolbom_cond = dolbom["시도"] == region
    chimae_cond = chimae["시도"] == region
    job_cond = job["시도"] == region

    sigoongoo = dolbom[dolbom_cond]["시군구"].unique().tolist()
    sigoongoo2 = chimae[chimae_cond]["시군구"].unique().tolist()
    sigoongoo3 = job[job_cond]["시군구"].unique().tolist()
    sigoongoo = list(set.union(set(sigoongoo), set(sigoongoo2), set(sigoongoo3)))
    region_detail = st.sidebar.selectbox("세부지역을 선택하세요: ", sigoongoo )

    dolbom_cond2 = dolbom["시군구"] == region_detail
    chimae_cond2 = chimae["시군구"] == region_detail
    job_cond2 = job["시군구"] == region_detail

    dolbom_cond3 = dolbom_cond&dolbom_cond2
    chimae_cond3 = chimae_cond&chimae_cond2
    job_cond3 = job_cond&job_cond2

    if st.button("실행"):
        dolbom[dolbom_cond3].to_csv("./tempor/dolbom.csv")
        chimae[chimae_cond3].to_csv("./tempor/chimae.csv")
        job[job_cond3].to_csv("./tempor/job.csv")

# 노인맞춤돌봄서비스 수행기관현황
def dolbom_ft():
    st.markdown("#### 노인맞춤돌봄서비스 수행기관")
    df = pd.read_csv("./tempor/dolbom.csv", index_col=0)
    st.dataframe(df)

# 전국치매센터 현황
def chimae_ft():
    st.markdown("#### 전국 치매센터 표준데이터")
    df = pd.read_csv("./tempor/chimae.csv", index_col=0)
    st.dataframe(df)

# 노인일자리 현황
def job_ft():
    st.markdown("#### 노인 일자리 정보")
    df = pd.read_csv("./tempor/job.csv", index_col=0)
    st.dataframe(df)

# 위치정보 상세
def location_detail():
    DATA_URL = "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/biergartens.json"
    ICON_URL = "https://cdn-icons-png.flaticon.com/512/1141/1141117.png"
    data = pd.read_json(DATA_URL)[:10]
    icon_data = {
    # Icon from Wikimedia, used the Creative Commons Attribution-Share Alike 3.0
    # Unported, 2.5 Generic, 2.0 Generic and 1.0 Generic licenses
    "url": ICON_URL,
    "width": 242,
    "height": 242,
    "anchorY": 242,
}

    data["icon_data"] = None
    for i in data.index:
        data["icon_data"][i] = icon_data

    st.pydeck_chart(pdk.Deck(map_style=None, initial_view_state=pdk.ViewState(longitude=122.4, latitude=37, zoom=11, pitch=50), 
    layers= [pdk.Layer(type="IconLayer",data= data,get_icon="icon_data", get_size=4, size_scale=15 ,get_position='[lon, lat]', pickable=True)] ), use_container_width=True)



home()
page = st.sidebar.selectbox('페이지 선택: ', ['노인맞춤돌봄서비스', '전국치매센터', '노인일자리', '위치정보 상세'])

if page == '노인맞춤돌봄서비스':
    dolbom_ft()
elif page == '전국치매센터':
    chimae_ft()
elif page == '노인일자리':
    job_ft()
elif page == '위치정보 상세':
    location_detail()






