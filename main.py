import streamlit as st

# MBTI별 추천 직업 사전
mbti_jobs = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "소프트웨어 아키텍트"],
    "INTP": ["연구원", "이론 물리학자", "기술 분석가"],
    "ENTJ": ["프로젝트 매니저", "경영 컨설턴트", "CEO"],
    "ENTP": ["스타트업 창업자", "마케팅 전략가", "제품 매니저"],
    "INFJ": ["심리상담사", "작가", "사회 운동가"],
    "INFP": ["예술가", "시인", "콘텐츠 크리에이터"],
    "ENFJ": ["교육자", "HR 매니저", "정치가"],
    "ENFP": ["브랜드 매니저", "공연 예술가", "창의적 디렉터"],
    "ISTJ": ["회계사", "법률 전문가", "행정 공무원"],
    "ISFJ": ["간호사", "초등학교 교사", "사회복지사"],
    "ESTJ": ["군인", "운영 관리자", "프로젝트 관리자"],
    "ESFJ": ["고객 서비스 매니저", "간호 관리자", "이벤트 플래너"],
    "ISTP": ["기계공", "파일럿", "응급 구조사"],
    "ISFP": ["사진작가", "패션 디자이너", "플로리스트"],
    "ESTP": ["세일즈 대표", "기업가", "구조 엔지니어"],
    "ESFP": ["배우", "이벤트 코디네이터", "홍보 전문가"],
}

st.title("🎯 MBTI 기반 직업 추천기")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti}에게 어울리는 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
