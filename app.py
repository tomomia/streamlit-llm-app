import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI

# 環境変数を読み込む
load_dotenv()

# APIキー取得 (外で一度だけ)
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY が見つかりません。")
    st.stop()  # プログラム停止

# 確認
st.write("🔑 API Key:", api_key[:5] + "..." if api_key else "None")  # 一部だけ表示（安全のため）

# StreamlitのUI
st.title("LLMプロンプトフォーム")
st.write("このウェブアプリでは、質問と専門家タイプを選んで回答を得られます。")

# 入力フォーム
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家の種類", ("犬の専門家", "猫の専門家"))

# ✅ APIキーを引数として渡す関数
def get_llm_response(prompt, expert, api_key):  # ← APIキーも引数に
    system_message = "あなたは犬の専門家です。" if expert == "犬の専門家" else "あなたは猫の専門家です。"
    full_prompt = f"{system_message} {prompt}"

    # OpenAIのインスタンス生成
    llm = OpenAI(
        model_name="gpt-4o",
        temperature=0.5,
        openai_api_key=api_key  # 関数内で新たに読まない
    )
    response = llm(full_prompt)
    return response

# ボタン処理
if st.button("送信"):
    if prompt:
        response = get_llm_response(prompt, expert, api_key)  # ✅ APIキー渡して呼び出し
        st.subheader("LLMの回答:")
        st.write(response)
    else:
        st.warning("プロンプトを入力してください。")
