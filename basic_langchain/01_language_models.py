# 2025/01/10時点でのソース
import os
from langchain.chat_models import openai
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# Chat modelsの使い方
## chat modelsはチャット形式のやり取りを入力して応答を得られるようにしたモジュール
## 結果として得られるプログラム言語にJavaとPythonが載っていないことから、
## 前の会話の内容を引き継いでいることが分かる。
chat = openai.ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
messages = [
    SystemMessage(content="You are a programming helpful assistant."),
    HumanMessage(content="こんにちは。私はJavaとPythonを書くプログラマです。"),
    AIMessage(content="こんにちは。JavaとPythonを書くプログラマなんですね。"),
    HumanMessage(content="私に今後学ぶべきプログラム言語が他にあれば教えてください。")
    ]
result = chat(messages)
print(result)