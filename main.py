import streamlit as st
import random

st.set_page_config(page_title="세 수의 덧셈 연습", page_icon="🧮", layout="centered")

st.title("🧮 세 수의 덧셈 연습")
st.write("초등학교 1학년을 위한 **세 수 덧셈 연습** 페이지예요! ✨")

# 문제 생성 함수
def generate_problem():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    return a, b, c, a + b + c

# 4문제 생성
if "problems" not in st.session_state:
    st.session_state.problems = [generate_problem() for _ in range(4)]
    st.session_state.answers = [""] * 4
    st.session_state.checked = False

# 문제 보여주기
for i, (a, b, c, answer) in enumerate(st.session_state.problems):
    st.subheader(f"문제 {i+1}")
    st.write(f"{a} + {b} + {c} = ?")
    st.session_state.answers[i] = st.text_input(f"답 입력 (문제 {i+1})", 
                                                value=st.session_state.answers[i], 
                                                key=f"q{i}")

# 채점 버튼
if st.button("✅ 채점하기"):
    st.session_state.checked = True

# 채점 결과 표시
if st.session_state.checked:
    score = 0
    for i, (a, b, c, answer) in enumerate(st.session_state.problems):
        user_ans = st.session_state.answers[i]
        if user_ans.strip().isdigit() and int(user_ans) == answer:
            st.success(f"문제 {i+1}: 정답! 🎉 ({a}+{b}+{c}={answer})")
            score += 1
        else:
            st.error(f"문제 {i+1}: 틀렸어요 😢 (정답: {answer})")

    st.subheader(f"👉 총점: {score} / 4")

    # 새로운 문제 생성 버튼
    if st.button("🔄 새 문제 풀기"):
        st.session_state.problems = [generate_problem() for _ in range(4)]
        st.session_state.answers = [""] * 4
        st.session_state.checked = False
        st.experimental_rerun()
