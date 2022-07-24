from DAO.AbstractDAO import DAO
from entidades.Empresa import Empresa


class EmpresaDAO(DAO):
    def __init__(self):
        super().__init__('empresas.pkl')

    def add(self, cnpj, empresa: Empresa):
        if empresa is not None:
            super().add(cnpj, empresa)

    def get(self, key: str):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, int):
            return super().remove(key)
