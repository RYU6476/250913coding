import streamlit as st
st.title('나의 첫 웹앱!')
st.write('이걸 내가 만들었다고?!')
import streamlit as st
import random

st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚", layout="centered")

# 제목
st.markdown("""
# 📚✨ MBTI 공부법 추천기 🎉
어떤 **MBTI 유형**인지 선택하면, 당신에게 딱 맞는 공부법을 알려줄게요! 🔮
""")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 공부법 추천 딕셔너리
study_tips = {
    "ISTJ": "체계적인 계획표 📅 를 만들어 두고 차근차근 공부하는 게 효과적이에요!", 
    "ISFJ": "안정적인 환경 🏡 에서 혼자 집중하는 공부법이 좋아요.",
    "INFJ": "깊이 있는 이해 🧠 를 중시하니, 개념을 스스로 정리해보세요.",
    "INTJ": "장기 목표 🎯 를 세우고 전략적으로 접근하면 효율 최고!",
    "ISTP": "실습 🛠️ 위주의 학습법이 잘 맞아요.",
    "ISFP": "감각적인 자료 🎨 (그림, 색깔 등)로 공부하면 집중이 잘 돼요.",
    "INFP": "자신만의 의미 ✨ 를 부여하면서 공부할 때 몰입도가 높아져요.",
    "INTP": "호기심 🔍 이 끌리는 주제부터 파고드는 방식이 효과적이에요.",
    "ESTP": "게임처럼 🎮 문제를 풀며 속도감 있게 공부하면 좋아요.",
    "ESFP": "친구들과 함께 👯‍♀️ 즐겁게 공부하면 집중이 잘 돼요.",
    "ENFP": "다양한 방법 🌈 으로 공부해야 지루하지 않아요.",
    "ENTP": "토론 💬 하면서 배우는 게 큰 도움이 돼요.",
    "ESTJ": "정해진 시간표 ⏰ 를 따라가는 게 제일 잘 맞아요.",
    "ESFJ": "스터디 그룹 👨‍👩‍👧‍👦 으로 함께 공부하는 게 효과적이에요.",
    "ENFJ": "사람들에게 설명 🗣️ 하면서 공부하면 가장 잘 배워요.",
    "ENTJ": "목표 달성 🔥 을 위한 효율적인 전략 세우기가 핵심이에요."
}

# 사용자 선택
selected = st.selectbox("👉 당신의 MBTI를 선택하세요:", mbti_types)

# 추천 버튼
if st.button("✨ 나의 공부법 추천받기 ✨"):
    tip = study_tips.get(selected, "아직 준비 중인 유형이에요! 🌱")
    st.success(f"{selected}에게 어울리는 공부법은...\n\n💡 {tip}")

    # 재미있는 랜덤 효과: 명언 추가
    quotes = [
        "🚀 작은 한 걸음이 모여 큰 변화를 만든다!",
        "🌟 오늘의 노력은 내일의 나를 만든다.",
        "🔥 시작이 반이다! 지금 바로 책을 펼쳐봐요.",
        "💪 할 수 있다고 믿는 순간 절반은 이룬 거예요."
    ]
    st.balloons()
    st.info(random.choice(quotes))
