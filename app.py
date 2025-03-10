import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI  # ✅ Chatモデル

# 環境変数を読み込む
load_dotenv()

# Streamlit の UI 設計
st.title("LLMプロンプトフォーム")
st.write("このウェブアプリでは、入力フォームにテキストを入力し、専門を選択すると、選択した専門家としての回答が表示されます。")
st.write("操作方法:")
st.write("1. 下の入力欄に質問やテキストを入力します。")
st.write("2. ラジオボタンで専門家の種類を選択します。")
st.write("3. 送信ボタンをクリックすると、選択した専門家の視点からの回答が表示されます。")

# 入力フォーム
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家の種類を選択してください", ("犬の専門家", "猫の専門家"))

# LLM 応答関数
def get_llm_response(prompt, expert):
    if expert == "犬の専門家":
        system_message = "あなたは犬の専門家です。"
    else:
        system_message = "あなたは猫の専門家です。"

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    llm = ChatOpenAI(
        model="gpt-4o",  # ✅ 最新方式は model
        temperature=0.5,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )
    response = llm.invoke(messages)
    return response.content

# 送信ボタン
if st.button("送信"):
    if prompt:
        response = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(response)
    else:
        st.warning("プロンプトを入力してください。")
