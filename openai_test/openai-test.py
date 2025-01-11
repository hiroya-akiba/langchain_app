# 2025/01/10時点でのソース
import os
from openai import OpenAI

# APIキーをセット
filepath = "./open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# openaiインスタンスを作成
client = OpenAI()

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a programming helpful assistant."},
        {"role": "user",   "content": "Pythonを書くプログラマが上級者になる上でワンランク上の使い方をするにはどうすればよいでしょうか。"}
    ]
)

print(completion)


# 2024/05/23時点でのソース
#client = OpenAI()
#completion = client.chat.completions.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    # roleはsystem, user, assistantのどちらかを指定
#    # systemの場合、以降のcontent部分でchatgptの設定(AIアシスタント)を変更できる。
#    # userの場合、いつも通りChatGPTに話しかけるようにcontent部分にユーザーの入力内容を指定する。
#    # assistantの場合、content部分にAIからの出力を指定する。これまでの会話をすべて送ることで、その文脈を踏まえて回答してもらえる。
#    {"role": "user", "content": "始めてAPIを使ってあなたにアクセスできました。祝ってください。"}
#  ]
#)
## chatgptの返答を表示
#print(completion.choices[0].message)
#print(completion)
