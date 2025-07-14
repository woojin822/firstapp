import streamlit as st

# MBTI별 음식 추천 사전
mbti_foods = {
    "INTJ": ["다크 초콜릿", "수제 커피", "그릴드 스테이크"],
    "INTP": ["페스토 파스타", "마라탕", "콜드브루"],
    "ENTJ": ["비프 웰링턴", "레드 와인", "트러플 리조또"],
    "ENTP": ["타코", "퓨전 요리", "버블티"],
    "INFJ": ["허브차", "연어 샐러드", "그릭 요거트"],
    "INFP": ["비건 샌드위치", "스무디볼", "마카롱"],
    "ENFJ": ["홈메이드 쿠키", "파스타 알리오 올리오", "그린티 라떼"],
    "ENFP": ["핫윙", "딸기 팬케이크", "밀크셰이크"],
    "ISTJ": ["전통 한식", "된장찌개", "백미밥과 나물"],
    "ISFJ": ["김치찌개", "잡채", "수정과"],
    "ESTJ": ["돈까스", "냉면", "식혜"],
    "ESFJ": ["브런치 세트", "치킨 샐러드", "허니브레드"],
    "ISTP": ["햄버거", "프렌치프라이", "콜라"],
    "ISFP": ["크로와상", "아이스 아메리카노", "파르페"],
    "ESTP": ["양념치킨", "라면", "탄산수"],
    "ESFP": ["떡볶이", "붕어빵", "과일 에이드"],
}

st.title("🍽️ MBTI 기반 음식 추천기")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_foods.keys()))

# 음식 추천 결과 출력
if selected_mbti:
    st.subheader(f"🍴 {selected_mbti}에게 어울리는 음식")
    for food in mbti_foods[selected_mbti]:
        st.write(f"- {food}")
