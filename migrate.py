from package import sqlalchemy_base, sqlalchemy_engine, sqlalchemy_session
from package.model.UsuarioDBModel import UsuarioDBModel
from package.model.ValidacaoDBModel import ValidacaoDBModel
from package.model.TipoValidacaoDBModel import TipoValidacaoDBModel

sqlalchemy_base.metadata.drop_all(sqlalchemy_engine)
sqlalchemy_base.metadata.create_all(sqlalchemy_engine)

sqlalchemy_session.add(TipoValidacaoDBModel(id=1, nome="CONTRATO"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=2, nome="MATRICULA"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=3, nome="PROCURACAO"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=4, nome="REQUERIMENTO"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=5, nome="CERT. CIVIL"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=6, nome="CERT. CND"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=7, nome="CERT. CASAMENTO"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=8, nome="DOCUMENTO IDENTIDADE NACIONAL"))
sqlalchemy_session.add(
    TipoValidacaoDBModel(id=9, nome="CERTIFICADO NACIONAL HABILITACAO")
)
sqlalchemy_session.add(TipoValidacaoDBModel(id=9, nome="CERTIDAO TRABALHISTA"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=10, nome="CERTIDAO NASCIMENTO"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=11, nome="CERTIDAO ESTADUAL"))
sqlalchemy_session.add(TipoValidacaoDBModel(id=12, nome="CERTIDAO FEDERAL"))

sqlalchemy_session.commit()
