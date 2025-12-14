import streamlit as st
import random
from datetime import datetime

# 页面配置：全局设置
st.set_page_config(
    page_title="投硬币决定学不学",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自定义CSS：适配手机端样式
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
    }
    .stCaption {
        font-size: 14px;
        color: #666;
    }
    @media (max-width: 480px) {
        h1 {
            font-size: 24px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# 初始化会话状态
if "history" not in st.session_state:
    st.session_state.history = []
if "coin_times" not in st.session_state:
    st.session_state.coin_times = 0

# 页面标题与说明
st.title("📚 投硬币决定学不学")
st.caption("点击按钮投币，结果实时更新，支持查看历史记录 | 手机/电脑均可使用")

# 投硬币核心函数
def toss_coin():
    result = random.choice(["正面（立刻去学习）", "反面（再玩一会儿）"])
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.history.append({"time": now, "result": result})
    st.session_state.coin_times += 1
    return result

# 投币按钮区域
col1, col2 = st.columns([2, 1])
with col1:
    if st.button("点击投硬币 🪙", type="primary"):
        res = toss_coin()
        if "学习" in res:
            st.success(f"🎯 本次结果：{res}")
        else:
            st.warning(f"😜 本次结果：{res}")
with col2:
    st.metric("投币次数", st.session_state.coin_times)

# 历史记录区域
st.subheader("📜 投币历史")
if st.session_state.history:
    # 倒序显示最新记录
    for record in reversed(st.session_state.history):
        st.write(f"{record['time']}：{record['result']}")
    # 清空历史按钮
    if st.button("清空历史记录 🗑️"):
        st.session_state.history = []
        st.session_state.coin_times = 0
        st.rerun()
else:
    st.info("还没有投币记录，快点击按钮试试吧～")