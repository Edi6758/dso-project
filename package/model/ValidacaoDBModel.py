from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from package import sqlalchemy_base

class ValidacaoDBModel(sqlalchemy_base):

    __tablename__ = "validacao"

    usuario_id = Column(
            Integer,
            ForeignKey('usuario.id', ondelete='CASCADE'),
            primary_key=True)
    tipo_validacao_id = Column(
            Integer,
            ForeignKey('tipo_validacao.id'),
            primary_key=True)

    usuario = relationship('UsuarioDBModel', backref='usuario')
    tipo_validacao = relationship('TipoValidacaoDBModel', backref='tipo_validacao')
