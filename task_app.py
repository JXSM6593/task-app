import streamlit as st
from datetime import datetime

# --- ページ＆ヘッダー ---
st.set_page_config(page_title="かわいいStreamlit", page_icon="🌸", layout="centered")

st.markdown("""
<h1 style="text-align:center; margin-bottom:0;">🌸 かわいい Streamlit アプリ 🌸</h1>
<p style="text-align:center; color:#8c8c8c; margin-top:6px;">
  GitHub → Streamlit Cloud で公開中だよ
</p>
""", unsafe_allow_html=True)

# --- ちょい足しCSS（角丸カード/余白/ボタン） ---
st.markdown("""
<style>
/* 本文幅を少し狭くして中央に */
.css-18e3th9, .block-container { max-width: 720px; padding-top: 1.2rem; }
/* 白カード */
.kawaii-card {
  background: white; border-radius: 18px; padding: 18px 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06); border: 1px solid #f3eaf7;
}
/* 入力欄をふっくら */
input[type="text"]{
  border-radius: 12px !important; border: 1px solid #e9d9f3 !important;
}
/* ボタンをまるっと */
.stButton>button{
  border-radius: 999px; padding: .5rem 1.2rem; border: none;
  box-shadow: 0 6px 14px rgba(240, 169, 220, .35);
}
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="kawaii-card">', unsafe_allow_html=True)

    st.subheader("🧁 おなまえカード")
    name = st.text_input("お名前を入力してね")
    if st.button("💖 あいさつする"):
        if name.strip():
            st.success(f"✨ こんにちは、{name} さん！ いい一日になりますように ✨")
            st.balloons()
        else:
            st.warning("お名前を入れてね 🌟")

    st.markdown("</div>", unsafe_allow_html=True)

# ひとことフッター
st.caption(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M')} / made with Streamlit")

