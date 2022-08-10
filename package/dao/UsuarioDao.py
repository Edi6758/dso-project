from package import sqlalchemy_session
from package.model.UsuarioDBModel import UsuarioDBModel


class UsuarioDao:
    __model = UsuarioDBModel
    __session = sqlalchemy_session

    def create(self, model: UsuarioDBModel):
        self.__session.add(model)
        self.__session.commit()

    def read(self, id=None):
        if id: return self.__session.query(self.__model).get(id)
        return self.__session.query(self.__model).all()

    def update(self, id, nome, cpf, rg, email, senha):
        pass
        # self.__session.query(self.__model).filter_by(id = id).update()

    def delete(self, id):
        self.__session.query(self.__model).get(id).delete()

