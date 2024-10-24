""""
Integrantes: Fabrício Silvany / Victor Andrade
"""
import os

os.system("cls || clear") 
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

def logo():
    print("""
    === FOLHA DE PAGAMENTO ===
    """)

def INSS (salario):
    if salario <= 1100:
        salario_liquido = salario-(0.075 * salario)
    #- Salário até R$ 1.100,00: 7,5%
    elif salario > 1100 and salario <= 2203.48:
        salario_liquido = salario-(0.09 * salario)
    #- Salário de R$ 1.100,01 até R$ 2.203,48: 9%
    elif salario > 2203.48 and salario <= 3305.22:
        salario_liquido = salario-(0.12 * salario)
    #- Salário de R$ 2.203,49 até R$ 3.305,22: 12%
    elif salario > 3305.22 and salario <= 6433.57:
        salario_liquido = salario-(0.14 * salario)
    #- Salário de R$ 3.305,23 até R$ 6.433,57: 14%
    =
    #- O valor máximo de desconto do INSS é de R$ 854,36.
    return salario_liquido

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
    salario = Column("salario", Float)

    def __init__(self, nome: str, matricula: int, senha: str, salario:float):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha
        self.salario = salario

#Criando tabela
Base.metadata.create_all(bind=MEU_BANCO)

print("== REGISTRO ==")
registro_nome = input("Insira seu nome: ")
registro_matricula = input("Insira sua matricula: ")
registro_senha = input("Insira sua senha: ")
registro_salario = float(input("Insira sua renda mensal: "))

dados_funcionario = Funcionario(matricula = registro_matricula, senha = registro_senha, nome = registro_nome)

session.add(dados_funcionario)
session.commit()

print("Dados salvos!")
os.system("cls || clear")

while True:
    print("\n== LOGIN ==")
    login_matricula = input("Insira sua matricula: ")
    login_senha = input("Insira sua senha: ")
    os.system("cls || clear")

    if login_matricula != registro_matricula and login_senha != registro_senha:
        print("Login ou senha Incorretos. \n Tente novamente")
    else:
        print("Login bem sucedido!")
        break