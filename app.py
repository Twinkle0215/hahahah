import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="가시 피하기 게임",
    layout="wide"
)

# 여백 제거
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        iframe { border: none !important; }
    </style>
""", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body { margin: 0; background: #0a0a15; display: flex; justify-content: center; padding: 20px; }
</style>
</head>
<body>

<!-- 여기에 기존 게임 HTML 전체 붙여넣기 -->
<div id="game-container" ...>
  ...
</div>
<script>
  ...
</script>

</body>
</html>
"""

# ✅ 핵심: height를 게임 전체 높이보다 크게 설정
components.html(game_html, height=500, scrolling=False)
