import streamlit as st
import random

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

st.markdown('<p class="big-font">🔟 10을 만들고 더하기 연습</p>', unsafe_allow_html=True)
st.write("두 수를 먼저 더해서 10을 만든 뒤, 남은 수를 더해 보아요! 🌈✨")

# ===== 문제 생성 함수 (반드시 두 수가 10) =====
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
st.session_state.setdefault("round", 0)  # 새 문제 시도할 때마다 증가

# ===== 문제 표시 =====
for i, (a, b, c, answer) in enumerate(st.session_state.problems):
    st.markdown(f'<p class="problem-font">{i+1}: {a} + {b} + {c} = ?</p>', unsafe_allow_html=True)
    st.session_state.answers[i] = st.text_input(
        f"{i+1}번 답",
        value=st.session_state.answers[i],
        key=f"q{i}_{st.session_state.round}"  # round를 키에 추가해서 초기화 효과
    )

# ===== 채점하기 =====
if st.button("✅ 채점하기"):
    st.session_state.checked = True

if st.session_state.checked:
    score = 0
    for i, (a, b, c, answer) in enumerate(st.session_state.problems):
        user_ans = st.session_state.answers[i]
        if user_ans.strip().isdigit() and int(user_ans) == answer:
            st.success(f"{i+1}: 정답! 🎉 ({a}+{b}+{c}={answer})")
            score += 1
        else:
            st.error(f"{i+1}: 틀렸어요 😢 (정답: {answer})")
        st.info(make10_hint(a, b, c))

    st.markdown(f'<p class="big-font">👉 총점: {score} / 4</p>', unsafe_allow_html=True)

    if st.button("🔄 새 문제 풀기"):
        st.session_state.problems = [generate_problem() for _ in range(4)]
        st.session_state.answers = [""] * 4
        st.session_state.checked = False
        st.session_state.round += 1  # 라운드 증가 → 입력창 초기화
        st.rerun()
