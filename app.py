from insert_data import insert_clients
from query_data import get_client_by_cpf, get_all_clients, get_rich_clients
from database_mongo import create_database_and_collection

def main():
    # Crie o banco de dados e a coleção
    create_database_and_collection()

    # Insira os dados dos clientes
    insert_clients()

    # Recuperar um cliente pelo CPF
    cliente = get_client_by_cpf("12345678901")
    print("Cliente encontrado:", cliente)

    # Recuperar todos os clientes
    todos_clientes = get_all_clients()
    print("\nTodos os clientes:")
    for cliente in todos_clientes:
        print(cliente)

    # Recuperar clientes com saldo acima de um certo valor
    clientes_ricos = get_rich_clients(2500)
    print("\nClientes com saldo acima de 2500:")
    for cliente in clientes_ricos:
        print(cliente)

if __name__ == '__main__':
    main()
