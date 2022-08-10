from sqlalchemy import Column, String, Integer
from package import sqlalchemy_base

class UsuarioDBModel(sqlalchemy_base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    cpf = Column(String(11), unique=True)
    rg = Column(String(7), unique=True)
    email = Column(String(100), unique=True)
    senha = Column(String(100))

