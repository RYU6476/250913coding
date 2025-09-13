import streamlit as st
import pandas as pd
import altair as alt
import os

# 앱 제목
st.title("🌍 MBTI 유형별 국가 Top 10 시각화")

# 기본 파일 경로
file_path = "countriesMBTI_16types.csv"

# 데이터 불러오기
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.success("기본 데이터 파일을 불러왔습니다.")
else:
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("업로드한 파일을 불러왔습니다.")
    else:
        st.info("CSV 파일을 업로드하거나 기본 데이터를 같은 폴더에 두세요.")
        st.stop()

# MBTI 유형 선택
mbti_types = [col for col in df.columns if col != "Country"]
selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# Top 10 추출
top10 = df.sort_values(by=selected_type, ascending=False).head(10)

# Altair 차트 생성
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title="비율", scale=alt.Scale(domain=[0, top10[selected_type].max() * 1.1])),
        y=alt.Y("Country", sort="-x", title="국가"),
        tooltip=["Country", selected_type]
    )
    .properties(width=600, height=400, title=f"{selected_type} 유형 비율 Top 10 국가")
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

# 데이터프레임도 함께 표시
st.dataframe(top10.reset_index(drop=True))
