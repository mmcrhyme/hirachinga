from sqlalchemy import create_engine

from api.models.models import Base # api/models/taskでapi/db.pyからインポートしてるBaseをインポートしている？(api/db.pyから直でインポートでもOK?(あとで確認せよ))

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
