from pymongo import MongoClient
from urllib.parse import quote_plus

def get_mongo_client():
    username = quote_plus("pymongo")
    password = quote_plus("Senha@123")
    uri = f"mongodb+srv://{username}:{password}@cluster0.yqtqqvg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    return client
