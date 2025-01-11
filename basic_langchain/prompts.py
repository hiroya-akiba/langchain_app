# 2025/01/11時点でのソース
import os
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain.chat_models import openai


# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# ChatPromptTemplateの使い方
## Chat Completions APIの形式に対応したメッセージを作ると、以下のようになる。
## プロンプトの指定部分に差し込んで作成される。
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("あなたは{lang}言語のプロフェッショナルです。"),
    HumanMessagePromptTemplate.from_template("以下のアプリケーションを作成する際に、どんなパッケージを揃えたらよいか教えてください。\n\nアプリケーション : {app}")
])
messages = chat_prompt.format_prompt(lang="Java", app="お気に入りメール送信アプリケーション").to_messages()

# Chatモデル作成
chat = openai.ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
result = chat(messages)
print(result)