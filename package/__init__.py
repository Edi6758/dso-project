from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from package.Config import Config

sqlalchemy_engine = create_engine(Config.SQLALCHEMY_DB_URL, echo=True)
sqlalchemy_base = declarative_base()

Session = sessionmaker(bind=sqlalchemy_engine)
sqlalchemy_session = Session()

from package.model.TipoValidacaoDBModel import TipoValidacaoDBModel
from package.model.UsuarioDBModel import UsuarioDBModel
from package.model.ValidacaoDBModel import ValidacaoDBModel

