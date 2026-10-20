import streamlit as st

st.set_page_config(page_title="나의 쿼드 투자 비서", page_icon="📈")

st.title("📈 나의 쿼드 투자 비서")
st.write("미래에셋증권 API 키를 입력해 주세요.")

app_key = st.text_input("App Key", type="password")
app_secret = st.text_input("App Secret", type="password")

if st.button("확인"):
    if app_key and app_secret:
        st.success("키가 입력되었습니다!")
    else:
        st.warning("App Key와 App Secret을 모두 입력해 주세요.")
