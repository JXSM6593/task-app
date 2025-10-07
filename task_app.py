import streamlit as st
from datetime import datetime

# --- ページ設定 ---
st.set_page_config(page_title="かわいいStreamlit", page_icon="🌸", layout="centered")

# --- CSS（強化版：白枠完全ブロック） ---
st.markdown("""
<style>
/* レイアウト調整 */
.main .block-container { 
  padding-top: 3rem !important;
  max-width: 720px;
}
header[data-testid="stHeader"] { background: transparent; }

/* ---------- 白枠対策（強） ----------
   Streamlit の text_input は実装によって
   - div[data-testid="stTextInput"]
   - [data-baseweb="input"]（BaseWeb）
   - input[type="text"]
   など異なるDOMになることがあるため、すべて一度隠す。
*/
section.main div[data-testid="stTextInput"],
section.main [data-baseweb="input"],
section.main input[type="text"] {
  display: none !important;
  height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
}

/* #keep-input の中だけ再表示 */
#keep-input div[data-testid="stTextInput"],
#keep-input [data-baseweb="input"],
#keep-input input[type="text"] {
  display: block !important;
  height: auto !important;
  margin: initial !important;
  padding: initial !important;
}

/* ---------- 見た目（かわいい仕上げ） ---------- */
.kawaii-card {
  background: #fff;
  border-radius: 18px;
  padding: 18px 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,.06);
  border: 1px solid #f3eaf7;
}
input[type="text"]{
  border-radius: 12px !important;
  border: 1px solid #e9d9f3 !important;
}
.stButton>button{
  border-radius: 999px;
  padding: .5rem 1.2rem;
  border: none;
  box-shadow: 0 6px 14px rgba(240,169,220,.35);
  background-color: #ffe6f3 !important;
}
h1 { margin-top: .25rem; }
</style>
""", unsafe_allow_html=True)

# --- タイトル ---
st.markdown("""
<h1 style="text-align:center; margin-bottom:0;">🌸 Streamlit アプリ 🌸</h1>
<p style="text-align:center; color:#8c8c8c; margin-top:6px;">
  GitHub → Streamlit Cloud で公開中
</p>
""", unsafe_allow_html=True)

# --- メインカード ---
with st.container():
    st.markdown('<div class="kawaii-card">', unsafe_allow_html=True)

    st.subheader("🧁 名前を入力してね")

    # ✅ 表示したい入力欄だけ「許可ゾーン」で囲む
    st.markdown('<div id="keep-input">', unsafe_allow_html=True)
    name = st.text_input("お名前")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("💖 あいさつする"):
        if name.strip():
            st.success(f"✨ こんにちは、{name} さん！ いい一日になりますように ✨")
            st.balloons()
        else:
            st.warning("お名前を入れてね 🌟")

    st.markdown("</div>", unsafe_allow_html=True)

# --- フッター ---
st.caption(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M')} / made with Streamlit")
