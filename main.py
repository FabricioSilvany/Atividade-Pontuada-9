""""
Integrantes: Fabrício Silvany / Victor Andrade
"""
import os

os.system("cls || clear") 
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#Tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    #Campos da tabela
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    matricula = Column("matricula", Integer)
    senha = Column("senha", String)

    def __init__(self, nome: str, matricula: int, senha: str):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha

#Criando tabela
Base.metadata.create_all(bind=MEU_BANCO)

os.system("cls || clear")

def logo():
    print("""
    === FOLHA DE PAGAMENTO ===
    """)