import streamlit as st
import pandas as pd

st.title("📚 나의 수업 시간표")

st.header("정적 시간표 (st.table)")

schedule = pd.DataFrame({
    "요일": ["월", "화", "수", "목", "금"],
    "1교시": ["논설실", "", "논설실", "빅수", "컴탐"],
    "2교시": ["기전연", "", "기전연", "", "기전연"],
    "3교시": ["전선대", "", "전선대", "", ""],
    "4교시" : ["논설실", "", "", "", ""]
})

st.table(schedule)

st.header("수업 정보 (st.json)")

class_info = {
    "컴탐": {
        "교수": "변해선",
        "강의실": "26동 104호"
    },
    "빅수": {
        "교수": "유용재",
        "강의실": "X"
    },
    "논설실": {
        "교수": "최우석",
        "강의실": "301동 102호"
    },
    "기전연" : {
        "교수" : "오정석",
        "강의실" : "301동 102호"
    },
    "전선대" : {
        "교수" : "이경무",
        "강의실" : "301동 202호"
    }
}

st.json(class_info)

st.header("이번 학기 요약 (st.metric)")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="수강 과목 수",
        value="5"
    )

with col2:
    st.metric(
        label="총 학점",
        value="17",
        delta="+3"
    )