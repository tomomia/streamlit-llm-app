from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from langchain.llms import OpenAI
import os

load_dotenv()

app = Flask(__name__)

# HTMLテンプレート
html_template = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>LLMプロンプトフォーム</title>
  </head>
  <body>
    <h1>LLMプロンプトフォーム</h1>
    <p>このウェブアプリケーションでは、入力フォームにテキストを入力し、専門家の種類を選択して送信すると、選択した専門家としての回答が表示されます。</p>
    <p>操作方法:</p>
    <ol>
      <li>「プロンプトを入力してください」欄に質問やテキストを入力します。</li>
      <li>「専門家の種類を選択してください」欄で、犬の専門家または猫の専門家を選択します。</li>
      <li>「送信」ボタンをクリックします。</li>
    </ol>
    <form method="post">
      <label for="prompt">プロンプトを入力してください:</label><br>
      <input type="text" id="prompt" name="prompt"><br><br>
      <label for="expert">専門家の種類を選択してください:</label><br>
      <input type="radio" id="dog" name="expert" value="dog" checked>
      <label for="dog">犬の専門家</label><br>
      <input type="radio" id="cat" name="expert" value="cat">
      <label for="cat">猫の専門家</label><br><br>
      <input type="submit" value="送信">
    </form>
    {% if response %}
      <h2>LLMの回答:</h2>
      <p>{{ response }}</p>
    {% endif %}
  </body>
</html>
"""

def get_llm_response(prompt, expert):
    if expert == 'dog':
        system_message = "あなたは犬の専門家です。"
    elif expert == 'cat':
        system_message = "あなたは猫の専門家です。"
    
    full_prompt = f"{system_message} {prompt}"
    
    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # OpenAI APIキーを環境変数から取得
    response = llm(full_prompt)
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        expert = request.form['expert']
        response = get_llm_response(prompt, expert)
        
    return render_template_string(html_template, response=response)

if __name__ == '__main__':
    app.run(debug=True)
