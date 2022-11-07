import pymongo

def init_mongo_db(db_url: str = None, db_port: str = None, db_name: str = None):

    db = pymongo.MongoClient(db_url, int(db_port))[db_name]
    return db
