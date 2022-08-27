from typing import Optional
from package.dao.UsuarioDao import UsuarioDao
from package.entidades.Usuario import Usuario
from package.model.UsuarioDBModel import UsuarioDBModel
from package.query.UsuarioQuery import UsuarioQuery
from package.service.ValidacaoService import ValidacaoService


class UsuarioService:
    def __init__(self):
        self.__validacao_service = ValidacaoService()
        self.__usuarioQuery = UsuarioQuery()
        self.__usuarioDao = UsuarioDao()

    def getUsuarioById(self, id) -> Optional[Usuario]:
        return self.convertModelToEntity(self.__usuarioDao.read(id))

    def getUsuarioByCpf(self, cpf) -> Optional[Usuario]:
        return self.convertModelToEntity(self.__usuarioQuery.getUsuarioByCpf(cpf))

    def deleteUsuarioById(self, id):
        self.__usuarioDao.delete(id)

    def getUsuarios(self):
        usuarios = self.__usuarioDao.read()
        return [self.convertModelToEntity(model) for model in usuarios]

    def persist(self, entity):
        model = self.convertEntityToModel(entity)
        self.__usuarioDao.create(model)

    def update(self, entity: Usuario):
        self.__usuarioDao.update(self.convertEntityToModel(entity))

    def getValidacoesByUsuarioId(self, id):
        usuario = self.getUsuarioById(id)
        if not usuario: return None
        return [val for val in usuario.validacoes] if usuario.validacoes else None

    def saveValidacoesByUsuarioId(self, id, validacoes):
        for validacao in validacoes:
            self.__validacao_service.persist(
                self.__validacao_service.convertDictToModel({
                    'usuario_id': id,
                    'tipo_validacao_id': validacao.value
                }))

    def convertDictToEntity(self, dto: dict) -> Usuario:
            return Usuario(
                dto['nome'],
                dto['cpf'],
                dto['rg'],
                dto['titulo'],
                dto['email'],
                dto['senha'],
                dto['num_matricula'])

    def convertEntityToModel(self, entity: Usuario) -> UsuarioDBModel:
        return UsuarioDBModel(nome=entity.nome,
                              cpf=entity.cpf,
                              rg=entity.rg,
                              titulo=entity.titulo,
                              email=entity.email,
                              num_matricula=entity.num_matricula,
                              senha=entity.senha)

    def convertModelToEntity(self, model) -> Optional[Usuario]:
        if not model: return None
        return Usuario(
                id=model.id,
                nome=model.nome,
                cpf=model.cpf,
                rg=model.rg,
                email=model.email,
                senha=model.senha,
                titulo=model.titulo,
                num_matricula=model.num_matricula,
                validacoes=model.validacoes)

    def checkForDuplicateByCpf(self, cpf) -> bool:
        return bool(self.getUsuarioByCpf(cpf))


