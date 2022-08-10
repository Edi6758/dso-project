from sqlalchemy import Column, Integer, String
from package import sqlalchemy_base

class TipoValidacaoDBModel(sqlalchemy_base):

    __tablename__ = "tipo_validacao"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
