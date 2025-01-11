# 2025/01/11時点でのソース
import os
from langchain.chat_models import openai
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# ストリ－ミングで応答を得る方法
chat = openai.ChatOpenAI(
    model_name="gpt-3.5-turbo", 
    temperature=0, 
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
    )
messages = [
    SystemMessage(content="You are a programming helpful assistant."),
    HumanMessage(content="こんにちは。私はJavaとPythonを書くプログラマです。"),
    ]
result = chat(messages)