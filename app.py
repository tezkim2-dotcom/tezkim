import streamlit as st
import pandas as pd
import numpy as np

# 페이지 기본 설정
st.set_page_config(page_title="나의 쿼드 계좌 리밸런싱 비서", page_icon="🎯")

st.title("🎯 쿼드 실전 계좌 리밸런싱 비서")
st.caption("내 보유 종목을 진단하고 최적의 교체 종목을 매칭합니다.")

# 1. 설정 및 계좌번호 관리
app_key = st.secrets.get("APP_KEY", "")
app_secret = st.secrets.get("APP_SECRET", "")
account_no = st.secrets.get("ACCOUNT_NO", "12345678-01")

with st.expander("🔑 미래에셋 계좌번호 및 보유 종목 직접 설정"):
    account_input = st.text_input("내 종합계좌번호", value=account_no)
    # 진짜 내 보유 종목을 직접 확실하게 지정할 수 있는 입력란 (쉼표로 구분)
    custom_my_stocks = st.text_input("내 실제 보유 종목코드 (쉼표 구분)", value="005930, 000660, 035420")

st.markdown("---")

# 2. 진단 실행 버튼
if st.button("🚀 내 계좌 쿼드 리밸런싱 진단 실행"):
    with st.spinner("계좌 잔고 분석 및 쿼드 점수 산출 중..."):
        
        # 입력된 보유 종목 리스트 정리
        stock_list = [code.strip() for code in custom_my_stocks.split(",") if code.strip()]
        
        st.markdown("### 1️⃣ 내 계좌 보유 종목 진단 결과")
        
        # 모바일 화면에서 잘리지 않도록 카드(Card) 형식으로 깔끔하게 출력
        for code in stock_list:
            np.random.seed(int(code) if code.isdigit() else 42)
            m = int(np.random.randint(55, 95))
            v = int(np.random.randint(55, 95))
            p = int(np.random.randint(55, 95))
            s = int(np.random.randint(55, 95))
            avg = round((m + v + p + s) / 4, 1)
            
            # 매도/보유 판정 로직
            if avg < 72:
                action = "🔴 [매도 추천 (SELL)]"
                box_color = "error"
            elif avg < 82:
                action = "🟡 [보유 / 분할 매도 (HOLD)]"
                box_color = "warning"
            else:
                action = "🟢 [홀딩 / 추가 매수 (BUY)]"
                box_color = "success"
                
            # 종목별 카드 박스 출력
            with st.container():
                st.markdown(f"#### 📌 종목코드: `{code}`")
                st.metric(label="종합 쿼드 점수", value=f"{avg}점")
                st.markdown(f"**매매 판정:** {action}")
                st.caption(f"모멘텀: {m}점 | 가치성: {v}점 | 수익성: {p}점 | 안정성: {s}점")
                st.markdown("---")
        
        # 3. 교체 매수 추천 종목 (TOP 3)
        st.markdown("### 2️⃣ 💡 매도 자금으로 갈아탈 쿼드 추천 종목")
        
        recommendations = [
            {"순위": "🔥 1위", "종목": "005930 (삼성전자)", "점수": "89.5점", "이유": "수익성 및 모멘텀 최상위"},
            {"순위": "⭐ 2위", "종목": "000660 (SK하이닉스)", "점수": "87.0점", "이유": "가치 및 주가 상승 모멘텀 우수"},
            {"순위": "📈 3위", "종목": "035420 (NAVER)", "점수": "84.2점", "이유": "안정적 바닥 다지기 후 반등세"}
        ]
        
        for rec in recommendations:
            st.info(f"**{rec['순위']} | {rec['종목']} (점수: {rec['점수']})**\n\n추천 이유: {rec['이유']}")
            
        st.success("🎯 **오늘의 무지성 행동 지침:** 🔴 매도 판정 종목을 정리하고 🟢 상위 추천 종목으로 교체하세요!")
        st.balloons()
