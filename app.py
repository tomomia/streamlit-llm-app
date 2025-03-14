import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI  # ✅ チャットモデル対応

# 環境変数読み込み
load_dotenv()
#api_key = os.getenv("OPENAI_API_KEY")
#環境変数読み込み変更 3/14
openai_api_key = st.secrets.get("OPENAI_API_KEY")

# Streamlit UI
st.title("LLMプロンプトフォーム")
prompt = st.text_input("プロンプトを入力してください:")
expert = st.radio("専門家を選んでください", ("犬の専門家", "猫の専門家"))

# LLM呼び出し関数
def get_llm_response(prompt, expert):
    if not openai_api_key:
        return "❌ APIキーが見つかりません"

    system_message = "あなたは犬の専門家です。" if expert == "犬の専門家" else "あなたは猫の専門家です。"

    llm = ChatOpenAI(
        model="gpt-4o",  
        temperature=0.5,
        openai_api_key=openai_api_key  
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    # 実行
    response = llm.invoke(messages)
    return response.content

# ボタン処理
if st.button("送信"):
    if prompt:
        answer = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(answer)
    else:
        st.warning("プロンプトを入力してください。")
