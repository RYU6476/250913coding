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
    random.shuffle(nums)
    return nums[0], nums[1], nums[2], sum(nums)

def make10_hint(a, b, c):
    nums = [a, b, c]
    for i in range(3):
        for j in range(i+1, 3):
            if nums[i] + nums[j] == 10:   # 👈 반드시 콜론(:) 있어야 함
                rest = [n for k, n in enumerate(nums) if k not in [i, j]][0]
                return f"👉 {nums[i]} + {nums[j]} = 10, 그리고 10 + {rest} = {10+rest}"
    return "👉 두 수를 먼저 더해서 10을 만들어 보세요!"

# ===== 세션 상태 초기화 =====
if "problems" not in st.session_state:
    st.session_state["problems"] = [generate_problem() for _ in range(4)]
if "answers" not in st.session_state:
    st.session_state["answers"] = [""] * 4
if "checked" not in st.session_state:
    st.session_state["checked"] = False
if "round" not in st.session_state:
    st.session_state["round"] = 0
if "results" not in st.session_state:
    st.session_state["results"] = {}   # 학생별 결과 저장 dict

# ===== 문제 표시 =====
for i, (a, b, c, answer) in enumerate(st.session_state["problems"]):
    st.markdown(f
