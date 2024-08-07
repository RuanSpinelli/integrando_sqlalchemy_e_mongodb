from database_mongo import get_collection

def insert_clients():
    collection = get_collection()
    
    # Dados dos clientes
    clientes = [
        {
            "nome": "João",
            "cpf": "12345678901",
            "endereco": "Rua Principal, 123",
            "contas": [
                {"tipo": "corrente", "agencia": "0001", "numero": 123456, "saldo": 1500.0},
                {"tipo": "poupança", "agencia": "0001", "numero": 654321, "saldo": 3000.0}
            ]
        },
        {
            "nome": "Maria",
            "cpf": "09876543210",
            "endereco": "Rua Secundária, 456",
            "contas": [
                {"tipo": "corrente", "agencia": "0002", "numero": 234567, "saldo": 2000.0}
            ]
        }
    ]

    # Insira documentos na coleção
    collection.insert_many(clientes)
