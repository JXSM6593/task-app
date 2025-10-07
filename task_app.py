st.markdown("""
<style>
/* ✅ 安全なセレクタで上の余白をしっかり確保 */
.main .block-container { 
  padding-top: 3rem !important;   /* ← 上の余白を増やす */
  max-width: 720px;
}

/* ヘッダーが重なって見える場合の予防 */
header[data-testid="stHeader"] { background: transparent; }

/* ---------- ここから見た目の調整 ---------- */
.kawaii-card {
  background: #fff; border-radius: 18px; padding: 18px 20px;
  box-shadow: 0 6px 18px rgba(0,0,0,.06); border: 1px solid #f3eaf7;
}
input[type="text"]{
  border-radius: 12px !important; border: 1px solid #e9d9f3 !important;
}
.stButton>button{
  border-radius: 999px; padding: .5rem 1.2rem; border: none;
  box-shadow: 0 6px 14px rgba(240,169,220,.35);
}
h1 { margin-top: .25rem; }  /* タイトルが切れないように微調整 */
</style>
""", unsafe_allow_html=True)


# ひとことフッター
st.caption(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M')} / made with Streamlit")

