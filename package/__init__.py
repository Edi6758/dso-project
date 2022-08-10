from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from package.Config import Config

sqlalchemy_engine = create_engine(Config.SQLALCHEMY_DB_URL, echo=True)
sqlalchemy_base = declarative_base()
