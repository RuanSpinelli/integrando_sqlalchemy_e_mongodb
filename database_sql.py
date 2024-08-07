from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///meu_banco.db')
Session = sessionmaker(bind=engine) 

def create_all():
    Base.metadata.create_all(engine)

def get_session():
    session = Session()
    return session
