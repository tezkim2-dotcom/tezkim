import streamlit as st

st.set_page_config(page_title="나의 쿼드 투자 비서", page_icon="📈")

st.title("📈 나의 쿼드 투자 비서")

# 1. Streamlit Secrets에서 API 키 자동 불러오기 시도
app_key = st.secrets.get("APP_KEY", "")
app_secret = st.secrets.get("APP_SECRET", "")

# 2. Secrets에 키가 없다면 화면에서 직접 입력받기
if not app_key or not app_secret:
    st.write("미래에셋증권 API 키를 입력해 주세요.")
    app_key = st.text_input("App Key", type="password")
    app_secret = st.text_input("App Secret", type="password")
    
    if st.button("확인"):
        if app_key and app_secret:
            st.success("키가 입력되었습니다!")
        else:
            st.warning("App Key와 App Secret을 모두 입력해 주세요.")
else:
    st.success("🔒 보안 설정(Secrets)에서 API 키가 안전하게 연동되었습니다.")

# 3. API 키가 준비된 이후에 실행될 쿼드 분석 및 그래프 영역
if app_key and app_secret:
    st.markdown("---")
    st.subheader("📊 쿼드 분석 및 그래프 모니터링")
    
    # 예시: 종목 선택 및 분석 영역 (추후 실제 API 연동 코드를 추가할 자리)
    stock_code = st.text_input("분석할 종목코드 입력 (예: 005930)", "005930")
    
    if st.button("쿼드 분석 및 차트 실행"):
        st.info(f"[{stock_code}] 종목에 대한 쿼드 분석 및 그래프를 불러오는 중입니다...")
        # 여기에 미래에셋 API 데이터 호출 및 st.line_chart 등 그래프 코드가 들어가게 됩니다.
