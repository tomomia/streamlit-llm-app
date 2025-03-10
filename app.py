import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI

# 環境変数読み込み
load_dotenv()

# APIキー確認
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY が見つかりません。`.env` ファイルを確認してください。")
    st.stop()  # これ以上実行させない

# Streamlit UI
st.title("LLMプロンプトフォーム")
st.write("このウェブアプリでは、入力フォームにテキストを入力し、専門を選択すると、専門家としての回答が表示されます。")

# 入力
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家の種類を選択してください", ("犬の専門家", "猫の専門家"))

# LLM 呼び出し関数
def get_llm_response(prompt, expert):
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
        response = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(response)
    else:
        st.warning("プロンプトを入力してください。")
