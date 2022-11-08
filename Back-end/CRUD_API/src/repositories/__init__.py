"""
    Inicializacion del repositorio
    Recuerde haber configurado correctamente el entorno
"""
from settings import Settings
from utils.connect_realtimedatabase import init_firebase_db
from utils.connect_mongodb import init_mongo_db

# Instacia la configuracion
settings = Settings()

# " STATE " Indica el estado de ejecución de las bases de datos
# 0 ninguna base de datos configurada
# 2 Solo FIREBASE_DB
# 3 Solo MONGO_DB
# 5 BOTH

STATE: int = 0
db: any = None
db_app: any = None

if settings.FIREBASE_DATABASE:
    db, db_app = init_firebase_db(db_url=settings.FIREBASE_DATABASE)
    print(f'connected to FIREBASE_DB {db}')
    STATE = STATE + 2

if settings.MONGO_DATABASE:
    mongo_db = init_mongo_db(db_url=settings.MONGO_DATABASE, db_port=settings.DB_PORT, db_name=settings.DB_NAME)
    print(f'connected to MONGO_DB {mongo_db}')
    STATE = STATE + 3

print(f'current state {STATE}')