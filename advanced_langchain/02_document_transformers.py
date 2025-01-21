# 2025/01/21時点でのソース
# RAGを作成していく
import os

# Document loaders
# Githubからファイルをインポートするモジュール
from langchain_community.document_loaders.git import GitLoader

# Document transformers
# ドキュメントに何らかの変換をかける
# 今回はドキュメントをある程度の長さ(チャンク)に分割する
from langchain.text_splitter import CharacterTextSplitter

# APIキーをセット
filepath = "../auth_info/open_ai_20250110.key"
with open(filepath, "r", encoding="utf-8") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

# 
def file_filter(file_path: str) -> bool:
    return file_path.endswith(".mdx")

loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./langchain",
    branch="master",
    file_filter= file_filter
)

raw_docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)

print(len(raw_docs))

## 他にも
## Html2TextTransformer HTMLをプレーンテキストに変換する
## EmbeddingsRedundantFilter 類似ドキュメントは除外
## OpenAIMetadataTagger メタデータの抽出
## DoctranTextTranslator 翻訳
## DoctranQATransformer ドキュメントからQAを生成する
## などがあるよ