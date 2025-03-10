import os
import streamlit as st
from langchain.llms import OpenAI

# 環境変数確認（デバッグ用、一部だけ表示）
#api_key = os.environ.get("OPENAI_API_KEY")
#st.write("🔑 API Key:", api_key[:5] + "..." if api_key else "❌ None")
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("LLMプロンプトフォーム")
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家を選んでください", ("犬の専門家", "猫の専門家"))

# LLM呼び出し関数
def get_llm_response(prompt, expert):
    if not api_key:
        return "❌ APIキーが見つかりません"

    system_message = "あなたは犬の専門家です。" if expert == "犬の専門家" else "あなたは猫の専門家です。"
    full_prompt = f"{system_message} {prompt}"

    llm = OpenAI(
        model="gpt-4o",  # ✅ 正しいパラメータ名
        temperature=0.5
    )
    response = llm(full_prompt)
    return response

# ボタン処理
if st.button("送信"):
    if prompt:
        answer = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(answer)
    else:
        st.warning("プロンプトを入力してください。")
