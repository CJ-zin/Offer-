import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 初始化
st.set_page_config(page_title="Offer捕手", layout="wide")
st.title("Offer捕手 - 求职匹配智能体")

st.sidebar.header("你的求职信息")
resume_text = st.sidebar.text_area("粘贴简历文本：", height=300)
job_intention = st.sidebar.text_input("目标岗位/行业：")

if st.button("开始匹配岗位"):
    with st.spinner("正在为你匹配高适配岗位..."):
        llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
        prompt = f"根据以下简历和求职意向，推荐3个匹配度高的岗位，说明匹配理由：\n简历：{resume_text}\n意向：{job_intention}"
        response = llm.predict(prompt)
        st.subheader("岗位匹配结果")
        st.write(response)
