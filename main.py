""""
Integrantes: Fabrício Silvany / Victor Andrade
"""
import os

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")