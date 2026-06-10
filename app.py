import streamlit as st
import requests

st.set_page_config(page_title="Offer捕手", layout="wide")
st.title("Offer 捕手")

api_key = st.sidebar.text_input("通义千问 API-KEY", type="password")
if not api_key:
    st.warning("请输入API Key")
    st.stop()

def qwen_call(prompt):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {"model":"qwen-turbo","input":{"messages":[{"role":"user","content":prompt}]},"parameters":{"temperature":0.1}}
    res = requests.post(url, json=data)
    return res.json()["output"]["text"]

resume = st.sidebar.text_area("粘贴简历")
intent = st.sidebar.text_input("目标岗位")

st.divider()
if st.button("岗位匹配") and resume and intent:
    res = qwen_call(f"根据简历：{resume}，意向：{intent}，推荐3个岗位并说明理由")
    st.write(res)
