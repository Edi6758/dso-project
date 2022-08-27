from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import backref, relationship
from package import sqlalchemy_base
from package.model.ValidacaoDBModel import ValidacaoDBModel

class UsuarioDBModel(sqlalchemy_base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    rg = Column(String(7), unique=True, nullable=False)
    num_matricula = Column(String(100), nullable=False)
    titulo = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)

    validacoes = relationship(ValidacaoDBModel, backref=backref('usuario', cascade="all,delete"))
