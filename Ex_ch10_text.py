import streamlit as st

st.title("나의 소개 페이지")

st.header("자기소개")

st.write("안녕하세요, 제 이름은 송현준입니다.")

st.markdown("저는 **인공지능**과 *반도체*에 관심이 있습니다.")

st.header("좋아하는 것")

st.write("저는 게임과 야구를 좋아합니다.")

st.markdown(
    "가장 자주 방문하는 사이트는 "
    "[ETL 홈페이지](https://etl.snu.ac.kr) 입니다."
)

st.header("앞으로의 목표")

st.write("앞으로 다양한 활동을 진행하면서 실력을 키우고 싶습니다.")

st.caption("제가 좋아하는 파이썬 코드 예시")

st.code(
    """msg1 = "Hello "
    msg2 = " World!"
    msg = msg1 + msg2
    print(msg)""",
    language="python"
)

st.caption("Convolution")

st.latex(r"x(t) \ast h(t) \equiv \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau")
