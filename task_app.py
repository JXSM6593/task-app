import streamlit as st

st.set_page_config(page_title="はじめてのStreamlitアプリ")

st.title("🌱 はじめてのStreamlitアプリ")
st.write("これは GitHub 上で作って、Streamlit Cloud で動かすアプリです。")

name = st.text_input("お名前を入力してください")
if name:
    st.success(f"こんにちは、{name} さん！😊")
