from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from package import sqlalchemy_base

class UsuarioDBModel(sqlalchemy_base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    rg = Column(String(7), unique=True, nullable=False)
    titulo = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)

    # empresa_id = Column(
    #         Integer,
    #         ForeignKey('empresa.id', ondelete='CASCADE'),
    #         nullable=True)

    # empresa = relationship('EmpresaDBModel', backref='empresa')

