import os
import streamlit as st
from dotenv import load_dotenv
import openai
# OpenAIのAPIキーが設定されているか確認
if "OPENAI_API_KEY" not in os.environ:
    st.error("OpenAI APIキーが設定されていません。環境変数を確認してください。")
    st.stop()
# 環境変数読み込み
load_dotenv()

# OpenAI APIキー
openai.api_key = os.environ["OPENAI_API_KEY"]

# StreamlitのUI
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

    # OpenAI公式APIで呼び出し
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.5
    )

    return response.choices[0].message.content

# 送信ボタン
if st.button("送信"):
    if prompt:
        response = get_llm_response(prompt, expert)
        st.subheader("LLMの回答:")
        st.write(response)
    else:
        st.warning("プロンプトを入力してください。")
