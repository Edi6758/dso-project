from sqlalchemy import Column, Integer, String
from package import sqlalchemy_base

class EmpresaDBModel(sqlalchemy_base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    cnpj = Column(String(20), unique=True)
