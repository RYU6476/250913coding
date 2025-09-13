import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="10을 만들고 더하기 연습", page_icon="🔟", layout="centered")

# ===== 스타일 =====
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #a8e6ff, #ffffff);
    }
    .big-font {
        font-size: 40px !important;
        font-weight: bold;
    }
    .problem-font {
        font-size: 34px !important;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        font-size: 32px !important;
        height: 80px;
        width: 280px;
        text-align: center;
        border: 3px solid #555;
        border-radius: 10px;
    }
    .stButton>button {
        font-size: 26px !important;
        padding: 14px 28px;
        border-radius: 12px;
        background-color: #ffd93d;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ===== 학생 번호 입력 =====
student_id = st.text_input("🧑‍🎓 학생 번호를 입력하세요:", key="student_id")

st.markdown('<p class="big-font">🔟 10을 만들고 더하기 연습</p>', unsafe_allow_html=True)
st.write("두 수를 먼저 더해서 10을 만든 뒤, 남은 수를 더해 보아요! 🌈✨")

# ===== 문제 생성 함수 =====
def generate_problem():
    x = random.randint(1, 9)
    y = 10 - x
    z = random.randint(1, 9)
    nums = [x, y, z]
    random.shuffle(nums)  # 위치 섞기
    return nums[0], nums[1], nums[2], sum(nums)

def make10_hint(a, b, c):
    nums = [a, b, c]
    for i in range(3):
        for j in range(i+1, 3):
            if nums[i] + nums[j] == 10:
                rest = [n for k, n in enumerate(nums) if k not in [i, j]][0]
                return f"👉 {nums[i]} + {nums[j]} = 10, 그리고 10 + {rest} = {10+rest}"
    return "👉 두 수를 먼저 더해서 10을 만들어 보세요!"

# ===== 세션 상태 초기화 =====
st.session_state.setdefault("problems", [generate_problem() for _ in range(4)])
st.session_state.setdefault("answers", [""] * 4)
st.session_state.setdefault("checked", False)
st.session_state.setdefault("round", 0)  
st.session_state.setdefault("results", {})  # 학생별 결과 저장 dict

# ===== 문제 표시 =====
for i, (a, b, c, answer) in enumerate(st.session_state.problems):
    st.markdown(f'<p class="problem-font">{i+1}: {a} + {b} + {c} = ?</p>', unsafe_allow_html=True)
    st.session_state.answers[i] = st.text_input(
        f"{i+1}번 답",
        value=st.session_state.answers[i],
        key=f"q{i}_{st.session_state.round}"
    )

# ===== 채점하기 =====
if st.button("✅ 채점하기") and student_id.strip() != "":
    st.session_state.checked = True

if st.session_state.checked and student_id.strip() != "":
    score = 0
    attempt_results = []

    for i, (a, b, c, answer) in enumerate(st.session_state.problems):
        user_ans = st.session_state.answers[i]
        correct = user_ans.strip().isdigit() and int(user_ans) == answer

        if correct:
            st.success(f"{i+1}: 정답! 🎉 ({a}+{b}+{c}={answer})")
            score += 1
        else:
            st.error(f"{i+1}: 틀렸어요 😢 (정답: {answer})")

        st.info(make10_hint(a, b, c))

        # 시도 기록 저장
        attempt_results.append({
            "문제번호": i+1,
            "문제": f"{a}+{b}+{c}",
            "학생답": user_ans,
            "정답": answer,
            "채점": "O" if correct else "X"
        })

    st.markdown(f'<p class="big-font">👉 총점: {score} / 4</p>', unsafe_allow_html=True)

    # 학생별 기록 저장
    if student_id not in st.session_state.results:
        st.session_state.results[student_id] = []

    st.session_state.re_
