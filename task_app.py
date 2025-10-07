import streamlit as st
from datetime import datetime

# --- ページ＆ヘッダー ---
st.set_page_config(page_title="かわいいStreamlit", page_icon="🌸", layout="centered")

st.markdown("""
<style>
/* ✅ 上余白と中央寄せ調整 */
.main .block-container { 
  padding-top: 3rem !important;
  max-width: 720px;
}
header[data-testid="stHeader"] { background: transparent; }

/* ---------- 見た目調整 ---------- */
.stButton>button{
  border-radius: 999px; padding: .5rem 1.2rem; border: none;
  box-shadow: 0 6px 14px rgba(240,169,220,.35);
}
h1 { margin-top: .25rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="text-align:center; margin-bottom:0;">🌸 なおこ初アプリ 🌸</h1>
<p style="text-align:center; color:#8c8c8c; margin-top:6px;">
  GitHub → Streamlit Cloud で公開中
</p>
""", unsafe_allow_html=True)

# --- 本体カード ---
with st.container():
    st.markdown('<div class="kawaii-card">', unsafe_allow_html=True)

    st.subheader("🧁 名前を入力してね")
    name = st.text_input("お名前")
    if st.button("💖 あいさつする"):
        if name.strip():
            st.success(f"✨ こんにちは、{name} さん！ いい一日になりますように ✨")
            st.balloons()
        else:
            st.warning("お名前を入れてね 🌟")

    st.markdown("</div>", unsafe_allow_html=True)

# --- フッター ---
st.caption(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M')} / made with Streamlit")


