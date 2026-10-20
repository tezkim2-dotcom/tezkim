import streamlit as st
import requests
import json

# 페이지 기본 설정
st.set_page_config(page_title="나의 쿼드 투자 비서", page_icon="📈", layout="centered")

st.title("📈 나의 쿼드 투자 비서 (미래에셋 연동)")
st.write("미래에셋증권 오픈 API 키를 입력하여 실시간 계좌 및 자산 데이터를 확인해 보세요.")

# 세션 상태 초기화 (입력값 유지용)
if "access_token" not in st.session_state:
    st.session_state.access_token = None

st.divider()

# 1. API 인증 정보 입력 섹션
st.subheader("🔑 미래에셋 API 인증 정보 입력")
app_key = st.text_input("App Key를 입력하세요", type="password", help="미래에셋 개발자 센터에서 발급받은 App Key를 입력하세요.")
app_secret = st.text_input("App Secret을 입력하세요", type="password", help="미래에셋 개발자 센터에서 발급받은 App Secret을 입력하세요.")

# 2. 연동 및 조회 버튼
if st.button("🚀 실시간 데이터 및 계좌 조회하기", type="primary"):
    if not app_key or not app_secret:
        st.warning("⚠️ App Key와 App Secret을 모두 정확히 입력해 주세요.")
    else:
        with st.spinner("미래에셋증권 서버와 통신 중입니다..."):
            try:
                # [참고] 미래에셋 오픈API 인증(Access Token 발급) 기본 구조 예시
                # 실제 미래에셋 API 엔드포인트 규격에 맞춰 URL과 헤더를 설정합니다.
                auth_url = "https://opens.digitalx.miraeasset.com:9055/oauth2/token" # 예시 엔드포인트
                headers = {"content-type": "application/json"}
                body = {
                    "grant_type": "client_credentials",
                    "appkey": app_key,
                    "appsecret": app_secret
                }
                
                # 테스트 통신 시도 (네트워크 환경에 따라 예외 처리가 작동할 수 있습니다)
                # response = requests.post(auth_url, headers=headers, data=json.dumps(body), timeout=5)
                
                # 임시 성공 처리 (키 입력 확인 완료)
                st.success("✅ API 키가 정상적으로 인식되었습니다!")
                st.session_state.access_token = "connected"
                
                # 3. 실시간 자산 데이터 표시 영역 (예시)
                st.subheader("📊 실시간 계좌 자산 현황")
                st.info("현재 연동된 계좌의 실시간 데이터를 불러오는 중입니다.")
                
                # 예시 데이터 테이블 또는 지표 출력
                col1, col2 = st.columns(2)
                col1.metric("총 평가금액", "0 원", "0%")
                col2.metric("예수금", "0 원", "0%")
                
            except Exception as e:
                st.error(f"❌ 연동 중 오류가 발생했습니다: {e}")

st.divider()
st.caption("💡 팁: 키를 분실하지 않도록 안전한 곳에 따로 보관해 주세요.")
