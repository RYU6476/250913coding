import streamlit as st
import random

st.set_page_config(page_title="10을 만들고 더하기 연습", page_icon="🔟", layout="centered")

# ===== 스타일 지정 =====
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #a8e6ff, #ffffff);
    }
    .big-font {
        font-size: 36px !important;
        font-weight: bold;
    }
    .problem-font {
        font-size: 30px !important;
    }
    .stTextInput>div>div>input {
        font-size: 28px !important;
        height: 60px;
        text-align: center;
    }
    .stButton>button {
        font-size: 24px !important;
        padding: 12px 24px;
        border-radius: 12px;
        background-color: #ffd93d;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ===== 제목 =====
st.markdown('<p class="big-font">🔟 10을 만들고 더하기 연습</p>', unsafe_allow_html=True)
st.write("세 수를 더할 때, **10을 먼저 만들고 더하는 방법**을 연습해 보아요! 🌈✨")

# ===== 문제 생성 함수 =====
def generate_problem():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    return a, b, c, a+b+c

def make10_hint(a, b, c):
    nums = [a, b, c]
    for i in range(3):
        for j in range(i+1, 3):
            if nums[i] + nums[j] == 10:
                rest = [n for k, n in enumerate(nums) if k not in [i, j]][0]
                return f"👉 {nums[i]} + {nums[j]} = 10, 그리고 10 + {rest} = {10+rest}"
    return "👉 가까운 수끼리 더해서 10을 먼저 만들어 보세요!"

# ===== 문제 준비 =====
if "problems" not in st.session_state:
    st.session_state.problems = [generate_problem() for _ in range(4)]
    st.session_state.answers = [""] * 4
    st.session_state.checked = False

# ===== 문제 표시 =====
for i, (a, b, c, answer) in enumerate(st.session_state.problems):
    st.markdown(f'<p class="problem-font">문제 {i+1}: {a} + {b} + {c} = ?</p>', unsafe_allow_html=True)
    st.session_state.answers[i] = st.text_input(
        f"답 입력 (문제 {i+1})", 
        value=st.session_state.answers[i], 
        key=f"q{i}"
    )

# ===== 채점하기 =====
if st.button("✅ 채점하기"):
    st.session_state.checked = True

if st.session_state.checked:
    score = 0
    for i, (a, b, c, answer) in enumerate(st.session_state.problems):
        user_ans = st.session_state.ans
