import streamlit as st
import pandas as pd
import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="모바일 쿼드 분석 비서",
    page_icon="📈",
    layout="centered"
)

st.title("📈 나의 쿼드(Quad) 투자 비서")
st.markdown("장중엔 본업에 집중하고, **저녁엔 5분 예약 매매**로 1억 원을 향해 나아갑니다!")

# 탭 메뉴 구성
tab1, tab2, tab3 = st.tabs(["📊 내 계좌 진단", "🔍 쿼드 추천 종목", "🛠️ 매매 가이드"])

with tab1:
    st.subheader("💡 현재 계좌 포트폴리오 요약")
    st.markdown("스크린샷 기준 핵심 주도주 및 자산 현황입니다.")
    
    # 계좌 데이터프레임
    portfolio_data = {
        "종목명": ["삼성전자", "기아", "현대위아", "디케이티"],
        "보유수량": [8, 2, 10, 3],
        "평가손익(%)": ["+58.19%", "+24.86%", "-42.20%", "-15.25%"],
        "전략 방향": ["추세 홀딩", "목표가 익절 대기", "반등 시 교체 매도", "관망"]
    }
    st.table(pd.DataFrame(portfolio_data))
    
    st.info("📌 **핵심 조언:** 수익 중인 삼성전자와 기아는 방어선을 지키며 홀딩하고, 현대위아는 기술적 반등 시 현금화하여 S&P 500 ETF로 리밸런싱하세요.")

with tab2:
    st.subheader("⭐ 쿼드 점수 우수 종목 (관심 종목)")
    
    # 예시 종목 카드
    st.markdown("### 1️⃣ 주성엔지니어링 (036930)")
    st.write("- **쿼드 점수:** 85점 / 100점 (A등급)")
    mem_col1, mem_col2 = st.columns(2)
    with mem_col1:
        st.success("🟢 1차 눌림목 매수가\n\n **235,000원** (예약)")
    with mem_col2:
        st.warning("🎯 1차 목표가\n\n **275,000원**")
        
    st.markdown("---")
    st.markdown("### 2️⃣ TIGER 미국S&P500 (코어 자산)")
    st.write("- **특징:** 지수형 전략")
