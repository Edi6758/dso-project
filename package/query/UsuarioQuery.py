from package import sqlalchemy_session
from package.model.UsuarioDBModel import UsuarioDBModel


class UsuarioQuery:
    __session = sqlalchemy_session

    def getUsuarioByCpf(self, cpf) -> UsuarioDBModel | None:
        return self.__session.query(UsuarioDBModel).filter_by(cpf = cpf).first()
