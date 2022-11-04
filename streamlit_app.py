# python -m streamlit run C:\Users\USER\Documents\GitHub\optimizer\streamlit_app.py
import streamlit as st
import pandas as pd


st.title('시니어 프렌드!!!')

st.header('This is header')


# st.balloons()
# 데이터 받아오기
tab1, tab2, tab3 = st.tabs(['ex1', 'ex2', 'ex3'])
with tab1:
    dolbom = pd.read_csv("./data/노인맞춤돌봄서비스_수행기관현황.csv")
    chimae = pd.read_csv("./data/전국치매센터표준데이터.csv")
    job = pd.read_csv("./data/일자리끝.csv")


    sido = dolbom["시도"].unique().tolist()
    sido2 = chimae["시도"].unique().tolist()
    sido3 = job["시도"].unique().tolist()
    sido = list(set.union(set(sido), set(sido2), set(sido3)))
    region = st.selectbox("지역을 선택하세요: ", sido )

    dolbom_cond = dolbom["시도"] == region
    chimae_cond = chimae["시도"] == region
    job_cond = job["시도"] == region

    sigoongoo = dolbom[dolbom_cond]["시군구"].unique().tolist()
    sigoongoo2 = chimae[chimae_cond]["시군구"].unique().tolist()
    sigoongoo3 = job[job_cond]["시군구"].unique().tolist()
    sigoongoo = list(set.union(set(sigoongoo), set(sigoongoo2), set(sigoongoo3)))
    region_detail = st.selectbox("세부지역을 선택하세요: ", sigoongoo )

    dolbom_cond2 = dolbom["시군구"] == region_detail
    chimae_cond2 = chimae["시군구"] == region_detail
    job_cond2 = job["시군구"] == region_detail

    dolbom_cond3 = dolbom_cond&dolbom_cond2
    chimae_cond3 = chimae_cond&chimae_cond2
    job_cond3 = job_cond&job_cond2
    if st.button("실행"):
        st.markdown("#### 노인맞춤돌봄서비스 수행기관")
        st.dataframe(dolbom[dolbom_cond3])
        st.markdown("#### 전국 치매센터 표준데이터")
        st.dataframe(chimae[chimae_cond3])
        st.markdown("#### 노인 일자리 정보")
        st.dataframe(job[job_cond3])

with tab2:
    # map = folium.Map(location=[37,126], zoom_start=6)
    # st_map = st_folium(map, width=700, height=450)

    st.pydeck_chart()