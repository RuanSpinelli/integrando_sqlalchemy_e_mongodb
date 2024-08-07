from config_mongo import get_mongo_client

def get_database():
    client = get_mongo_client()
    db = client['meu_banco']
    return db

def get_collection():
    db = get_database()
    collection = db['bank']
    return collection

def create_database_and_collection():
    db = get_database()
    # Verifique se a coleção existe e, se não, crie uma coleção vazia para inicializá-la
    if 'bank' not in db.list_collection_names():
        db.create_collection('bank')
