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

#Banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")



while True:
    logo()
    login_matricula = input("\nInsira seu número de matricula: ").lower()
    login_senha = int(input("Insira a senha: "))

    if login_matricula != "123" and login_senha != 123:
        print("Matricula ou senha incorretos. \n Tente novamente")
    else:
        break