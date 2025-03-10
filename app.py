import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI

# 読み込み関数
def get_api_key():
    load_dotenv()  # セッションごとに再読み込み
    return os.environ.get("OPENAI_API_KEY")

# Streamlit UI
st.title("LLMプロンプトフォーム")

# 入力
prompt = st.text_input("プロンプトを入力:")
expert = st.radio("専門家を選んでください", ("犬の専門家", "猫の専門家"))

# 回答関数
def get_llm_response(prompt, expert):
    api_key = get_api_key()  # ここで毎回安全に読む
    if not api_key:
        return "❌ APIキーが見つかりません"

    system_message = "あなたは犬の専門家です。" if expert == "犬の専門家" else "あなたは猫の専門家です。"
    full_prompt = f"{system_message} {prompt}"

    llm = OpenAI(
        model_name="gpt-4o",
        temperature=0.5,
        openai_api_key=api_key
    )
    response = llm(full_prompt)
    return response

# ボタン
if st.button("送信"):
    if prompt:
        answer = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(answer)
    else:
        st.warning("プロンプトを入力してください。")
