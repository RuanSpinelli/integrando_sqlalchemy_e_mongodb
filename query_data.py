from database_mongo import get_collection

def get_client_by_cpf(cpf):
    collection = get_collection()
    cliente = collection.find_one({"cpf": cpf})
    return cliente

def get_all_clients():
    collection = get_collection()
    todos_clientes = collection.find()
    return list(todos_clientes)

def get_rich_clients(min_saldo):
    collection = get_collection()
    clientes_ricos = collection.find({"contas.saldo": {"$gt": min_saldo}})
    return list(clientes_ricos)
