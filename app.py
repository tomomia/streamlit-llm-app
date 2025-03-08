import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI

# 環境変数を読み込む
load_dotenv()

# OpenAI APIキーを取得
api_key = os.getenv('OPENAI_API_KEY')

# Streamlit の UI 設計
st.title("LLMプロンプトフォーム")
st.write("このウェブアプリでは、入力フォームにテキストを入力し、専門を選択すると、選択した専門家としての回答が表示されます。")

# 入力フォーム
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家の種類を選択してください", ("犬の専門家", "猫の専門家"))

# LLM の応答を取得する関数
def get_llm_response(prompt, expert):
    if expert == "犬の専門家":
        system_message = "あなたは犬の専門家です。"
    else:
        system_message = "あなたは猫の専門家です。"

    full_prompt = f"{system_message} {prompt}"

    llm = OpenAI(api_key=api_key)
    response = llm(full_prompt)
    
    return response

# 送信ボタン
if st.button("送信"):
    if prompt:
        response = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(response)
    else:
        st.warning("プロンプトを入力してください。")
