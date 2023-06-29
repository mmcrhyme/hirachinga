from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from api.routers import user
from api.routers import item
from api.routers import choice
from api.routers import progress
from api.routers import scene
from api.routers import difficulty_level
from api.routers import game_session

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)
app.include_router(choice.router)
app.include_router(progress.router)
app.include_router(scene.router)
app.include_router(difficulty_level.router)
app.include_router(game_session.router)


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
    return {"Hello": "huga"}