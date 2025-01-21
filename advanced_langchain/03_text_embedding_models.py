# 2025/01/21時点でのソース
# RAGを作成していく
import os

# Text Embedding Models
# テキストをベクトル化するモジュール
# もともとOpenAIにEmbeddings APIというものが存在し、そのラッパークラスをLangChainから使用する。
from langchain.embeddings import OpenAIEmbeddings

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# ベクトル化
query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか。"
embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query(query)
print(vector)