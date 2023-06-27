from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンからのアクセスを許可します。実際の運用環境では、必要なオリジンのみを許可するよう設定してください。
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "hoge"}