# 2025/01/11時点でのソース
import os
# ConversationChainsについて
# ConversationChain は langchain.chains モジュール内に存在しますが、
# バージョン 0.2.7 以降、非推奨となり、RunnableWithMessageHistory の使用が推奨されています。
# RunnableWithMessageHistory は以下の利点を提供します：
# ストリーミング、バッチ処理、非同期処理のサポート
# メモリ管理の柔軟性向上（チェーン外でのメモリ管理が可能）
# マルチスレッドのサポート
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_openai import ChatOpenAI

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# Memoryを定義 (チェーンの外で管理する)
store = {}

# ローカルPCのメモリ上に履歴を保管するクラス
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Chatモデル作成
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# chainを定義
chain = RunnableWithMessageHistory(llm, get_session_history)

# 会話1
response = chain.invoke(
    "こんにちは、私はプログラマの洋哉です。",
    config = {"configurable": {"session_id": "1"}}
)
print(response)

# 会話2
response = chain.invoke(
    "私の名前について、どんな印象を持ちますか？また、どんなものを由来としているか予想できますか？",
    config = {"configurable": {"session_id": "1"}}
)
print(response)