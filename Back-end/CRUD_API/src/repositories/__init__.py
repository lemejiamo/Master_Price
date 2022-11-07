from settings import Settings
from utils.connect_realtimedatabase import init_firebase_db
from utils.connect_mongodb import init_mongo_db

settings = Settings()

# Indica el estado de ejecución de las bases de datos
# 0 ninguna base de datos configurada
# 2 Solo FIREBASE_DB
# 3 Solo MONGO_DB
# 5 BOTH

STATE: int = 0

if settings.FIREBASE_DATABASE:
    db, db_app = init_firebase_db(db_url=settings.FIREBASE_DATABASE)
    print('connected to FIREBASE_DB')
    STATE = STATE + 2

if settings.MONGO_DATABASE:
    mongo_db = init_mongo_db(db_url=settings.MONGO_DATABASE, db_port=settings.DB_PORT, db_name=settings.DB_NAME)
    print('connected to MONGO_DB')
    STATE = STATE + 3