from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float)
    cliente = relationship("Cliente")


