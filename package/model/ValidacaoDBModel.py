from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from package import sqlalchemy_base
from package.model.TipoValidacaoDBModel import TipoValidacaoDBModel

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

    tipo_validacao = relationship(TipoValidacaoDBModel)
