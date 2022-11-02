import firebase_admin
from firebase_admin import db

from settings import Settings

settings = Settings()


def init_firebase_db(db_url: str = None):

    databaseurl = {"databaseURL": db_url}
    db_app = firebase_admin.initialize_app(options=databaseurl)

    return db, db_app
