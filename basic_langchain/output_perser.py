# 2025/01/11時点でのソース
import os
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import HumanMessage
from langchain.chat_models import openai
from langchain.output_parsers import PydanticOutputParser

import app_basemodel

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# Output Persers
## LLMの出力から必要な部分を切り取るモジュール
parser = PydanticOutputParser(pydantic_object=app_basemodel.Packages)

## プロンプトに含める出力形式の説明文を作成
## Parckagesクラスに対応した出力形式の指定の文字列
## 出力されるJsonの型を指定する。
format_instructions = parser.get_format_instructions()

template = """
アプリケーションを作成する際の、パッケージと使用アーキテクチャを教えてください。

{format_instructions}

使用言語: {lang}
アプリケーション名: {app}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["lang","app"],
    partial_variables={"format_instructions": format_instructions}
)

formatted_prompt = prompt.format(lang="Python", app="お気に入りメール送信Webアプリ")

# Chatモデル作成
chat = openai.ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
messages = [HumanMessage(content=formatted_prompt)]
out = chat(messages)
print(out.content)
print(type(parser.parse(out.content)))
print(parser.parse(out.content))