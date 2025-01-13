# Pydantic
## Javaにおけるbeanのようなものを作成できる
## OutputPersersで使用
from pydantic import BaseModel, Field 

class Packages(BaseModel):
    package: list[str] = Field(description="packages for the application.")
    architecture : list[str] = Field(description="main architecture for the application")