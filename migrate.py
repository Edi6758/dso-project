from package import sqlalchemy_base, sqlalchemy_engine
from package.model.UsuarioDBModel import UsuarioDBModel
from package.model.ValidacaoDBModel import ValidacaoDBModel
from package.model.TipoValidacaoDBModel import TipoValidacaoDBModel
from sqlalchemy.orm import sessionmaker

sqlalchemy_base.metadata.create_all(sqlalchemy_engine)

Session = sessionmaker(bind=sqlalchemy_engine)
session = Session()


session.add(TipoValidacaoDBModel(id="1", nome="CONTRATO"))
session.add(TipoValidacaoDBModel(id="2", nome="MATRICULA"))
session.add(TipoValidacaoDBModel(id="3", nome="PROCURACAO"))
session.add(TipoValidacaoDBModel(id="4", nome="REQUERIMENTO"))
session.add(TipoValidacaoDBModel(id="5", nome="CERT. CIVIL"))
session.add(TipoValidacaoDBModel(id="6", nome="CERT. CND"))
session.add(TipoValidacaoDBModel(id="7", nome="CERT. CASAMENTO"))

session.commit()
