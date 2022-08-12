from package import sqlalchemy_session
from package.model.UsuarioDBModel import UsuarioDBModel


class UsuarioDao:
    __model = UsuarioDBModel
    __session = sqlalchemy_session

    def create(self, model: __model):
        self.__session.add(model)
        self.__session.commit()

    def read(self, id=None):
        if id: return self.__session.query(self.__model).get(id)
        return self.__session.query(self.__model).all()

    def update(self, model):
        entity = self.__session.query(self.__model).get(model.id)
        for key, value in model.items():
            setattr(entity, key, value)
        self.__session.commit()

    def delete(self, id):
        self.__session.delete(self.__session.query(self.__model).get(id))
        self.__session.commit()

