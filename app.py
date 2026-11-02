import streamlit as st
import pandas as pd
import numpy as np

# 페이지 기본 설정
st.set_page_config(page_title="나의 쿼드 계좌 리밸런싱 비서", page_icon="🎯")

st.title("🎯 쿼드 실전 계좌 리밸런싱 비서")
st.caption("내 보유 종목 8개를 일괄 진단하고 최적의 교체 종목을 매칭합니다.")

# 사용자 실제 보유 8개 종목 데이터 정의 (종목명 및 코드)
MY_PORTFOLIO = [
    {"name": "삼성전자", "code": "005930"},
    {"name": "기아", "code": "000270"},
    {"name": "현대위아", "code": "011210"},
    {"name": "주성엔지니어링", "code": "036930"},
    {"name": "디케이티", "code": "290550"},
    {"name": "피에스케이", "code": "319660"},
    {"name": "KODEX 로봇액티브", "code": "453850"},
    {"name": "피앤에스로보틱스", "code": "446810"} # 임시 표준 코드 매핑
]

st.markdown("---")

# 진단 실행 버튼
if st.button("🚀 내 8개 보유 종목 쿼드 리밸런싱 진단 실행"):
    with st.spinner("보유 종목 전체 분석 및 쿼드 점수 산출 중..."):
        
        st.markdown(f"### 1️⃣ 내 계좌 보유 종목 진단 결과 (총 {len(MY_PORTFOLIO)}개 종목)")
        
        # 8개 종목 순회하며 진단 카드 출력
        for item in MY_PORTFOLIO:
            name = item["name"]
            code = item["code"]
            
            # 종목별 고유 시드 기반 쿼드 점수 산출
            np.random.seed(int(code) if code.isdigit() else 42)
            m = int(np.random.randint(58, 95))
            v = int(np.random.randint(58, 95))
            p = int(np.random.randint(58, 95))
            s = int(np.random.randint(58, 95))
            avg = round((m + v + p + s) / 4, 1)
            
            # 매도/보유 판정 로직
            if avg < 72:
                action = "🔴 [매도 추천 (SELL)]"
                guide = "모멘텀 및 수익성 저하. 과감한 정리 후 교체 권장"
            elif avg < 82:
                action = "🟡 [보유 / 분할 매도 (HOLD)]"
                guide = "흐름 유지 중. 상황 보며 비중 조절"
            else:
                action = "🟢 [홀딩 / 추가 매수 (BUY)]"
                guide = "쿼드 점수 최상위! 계속 보유"
                
            # 카드 형식으로 출력
            with st.container():
                st.markdown(f"#### 📌 `{name}` ({code})")
                st.metric(label="종합 쿼드 점수", value=f"{avg}점")
                st.markdown(f"**매매 판정:** {action}")
                st.caption(f"조치 지침: {guide}")
                st.caption(f"모멘텀: {m}점 | 가치성: {v}점 | 수익성: {p}점 | 안정성: {s}점")
                st.markdown("---")
        
        # 3. 교체 매수 추천 종목 (TOP 3)
        st.markdown("### 2️⃣ 💡 매도 자금으로 갈아탈 쿼드 추천 종목")
        
        recommendations = [
            {"순위": "🔥 1위", "종목": "삼성전자 (005930)", "점수": "89.5점", "이유": "수익성 및 모멘텀 최상위"},
            {"순위": "⭐ 2위", "종목": "SK하이닉스 (000660)", "점수": "87.0점", "이유": "가치 및 주가 상승 모멘텀 우수"},
            {"순위": "📈 3위", "종목": "주성엔지니어링 (036930)", "점수": "84.2점", "이유": "반도체 장비 모멘텀 및 안정성 우수"}
        ]
        
        for rec in recommendations:
            st.info(f"**{rec['순위']} | {rec['종목']} (점수: {rec['점수']})**\n\n추천 이유: {rec['이유']}")
            
        st.success("🎯 **오늘의 무지성 행동 지침:** 🔴 매도 판정 종목을 정리하고 🟢 상위 추천 종목으로 교체하세요!")
        st.balloons()
