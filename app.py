from sqlalchemy import *
from sqlalchemy.orm import *
from database import *
from models import *

# ... (sua configuração de engine e sessionmaker)
def main():
    create_all() #cria o banco de dados
    with Session() as session:
        
        # Inserir dados
        novo_cliente = Cliente(nome='João', cpf='12345678901', endereco='Rua Principal, 123')
        session.add(novo_cliente) # Insere novo cliente na tabela de clientes
        session.commit()

        # Consultar dados
        todos_clientes = session.query(Cliente).all()
        for cliente in todos_clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}")


if __name__ == '__main__':
    main()
