import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (프로필 정보 입력/표시)
st.sidebar.header("😎 프로필")
# 이미지 주소가 있다면 넣을 수 있습니다 (없으면 샘플 이미지 사용)
st.sidebar.image("https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", width=150)

name = st.sidebar.text_input("이름", "홍길동")
job = st.sidebar.text_input("직무/역할", "파이썬 웹 개발자")
mbti = st.sidebar.selectbox("MBTI", ["ENFP", "INFJ", "INTJ", "ENTP", "기타"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Contact**")
st.sidebar.markdown("📧 email@example.com")
st.sidebar.markdown("🔗 [GitHub](https://github.com)")

# 3. 메인 화면 구성
st.title(f"안녕하세요! {name}입니다. 👋")
st.subheader(f"✨ {job} | MBTI: {mbti}")

st.write("") # 공백 추가

# --- 자기소개 섹션 ---
st.header("📝 About Me")
st.info("""
    안녕하세요! 데이터와 웹 기술을 활용해 문제를 해결하는 것을 좋아하는 개발자입니다. 
    새로운 기술을 배우고 그것을 문서화하거나 공유하는 것에 보람을 느낍니다.
""")

# --- 기술 스택 섹션 ---
st.header("🛠️ Tech Stack")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages")
    st.markdown("- Python 🐍")
    st.markdown("- JavaScript ☕")
    st.markdown("- HTML/CSS 🌐")

with col2:
    st.subheader("Frameworks & Tools")
    st.markdown("- Streamlit 🎈")
    st.markdown("- Django / FastAPI ⚡")
    st.markdown("- Git & GitHub 🐙")

# --- 프로젝트/경험 섹션 ---
st.header("🚀 Projects")

with st.expander("1. 스트림릿을 활용한 자기소개 웹 앱"):
    st.write("**개발 기간:** 2026.06 (1일)")
    st.write("**주요 기능:** Streamlit을 활용하여 빠르고 인터랙티브한 이력서 및 자기소개 페이지 구현")
    st.caption("사용한 기술: Python, Streamlit")

with st.expander("2. 데이터 시각화 대시보드 구축"):
    st.write("**개발 기간:** 2026.01 ~ 2026.03")
    st.write("**주요 기능:** 공공 데이터를 활용한 매출 예측 및 대시보드 시각화")
    st.caption("사용한 기술: Python, Pandas, Plotly")

# --- 한마디 남기기 (방명록 기능) ---
st.header("💬 한마디 남기기")
visitor_msg = st.text_input("응원의 한마디나 피드백을 남겨주세요!")
if st.button("보내기"):
    if visitor_msg:
        st.success(f"방문자님의 메시지: '{visitor_msg}'가 성공적으로 전달되었습니다! (시뮬레이션)")
    else:
        st.warning("메시지를 입력해주세요!")