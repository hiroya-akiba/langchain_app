# 2025/01/14時点でのソース
# RAGを作成していく
import os

# Document loaders
# Githubからファイルをインポートするモジュール
from langchain_community.document_loaders.git import GitLoader

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

print(len(raw_docs))