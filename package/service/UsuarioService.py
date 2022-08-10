from sqlalchemy.orm import Query
from package.dao.UsuarioDao import UsuarioDao
from package.entidades.Usuario import Usuario
from package.model.UsuarioDBModel import UsuarioDBModel
from package.service.DocumentoService import DocumentoService
from package.service.ValidacaoService import ValidacaoService


class UsuarioService:
    def __init__(self):
        self.__documento_service = DocumentoService()
        self.__validacao_service = ValidacaoService()
        self.__usuarioDao = UsuarioDao()

    def getUsuarioById(self, id) -> Usuario:
        return self.convertModelToEntity(self.__usuarioDao.read(id))

    def getUsuarioByCpf(self, cpf) -> Usuario:
        return self.convertModelToEntity(self.__usuarioDao.read().filter_by(cpf = cpf))

    def deleteUsuarioById(self):
        self.__usuarioDao.delete(id)

    def getUsuarios(self):
        usuarios = self.__usuarioDao.read()
        return [self.convertModelToEntity(model) for model in usuarios]

    def persist(self, entity):
        model = self.convertEntityToModel(entity)
        self.__usuarioDao.create(model)

    def convertDictToEntity(self, dto: dict) -> Usuario:
            if dto['contrato']:
                val_contrato = self.__documento_service.validar_contrato(
                    document=self.__validacao_service.read_image_to_text(dto['contrato']),
                    nome=dto['nome'],
                    cpf=dto['cpf'],
                    rg=dto['rg'],
                    num_matricula=dto['num_matricula'])
            else: val_contrato = False

            if dto['matricula']:
                val_matricula = self.__documento_service.validar_matricula(
                    document=self.__validacao_service.read_image_to_text(dto['matricula']),
                    nome=dto['nome'])
            else: val_matricula = False

            if dto['procuracao']:
                val_procuracao = self.__documento_service.validar_procuracao(
                    document=self.__validacao_service.read_image_to_text(dto['procuracao']),
                    nome=dto['nome'])
            else: val_procuracao = False

            if dto['requerimento']:
                val_requerimento = self.__documento_service.validar_requerimento(
                    document=self.__validacao_service.read_image_to_text(dto['requerimento']),
                    nome=dto['nome'])
            else: val_requerimento = False

            if dto['cert_civil']:
                val_cert_civil = self.__documento_service.validar_cert_criminal(
                    document=self.__validacao_service.read_image_to_text(dto['cert_civil']),
                    nome=dto['nome'],
                    cpf=dto['cpf'])
            else: val_cert_civil = False

            if dto['cert_cnd']:
                val_cert_cnd = self.__documento_service.validar_cert_cnd(
                    document=self.__validacao_service.read_image_to_text(dto['cert_cnd']),
                    nome=dto['nome'],
                    cpf=dto['cpf'])
            else: val_cert_cnd = False

            if dto['cert_casamento']:
                val_cert_casamento = self.__documento_service.validar_cert_casamento(
                    document=self.__validacao_service.read_image_to_text(dto['cert_casamento']),
                    nome=dto['nome'],
                    cpf=dto['cpf'])
            else: val_cert_casamento = False

            return Usuario(
                dto['nome'],
                dto['cpf'],
                dto['rg'],
                dto['titulo'],
                dto['email'],
                dto['senha'],
                val_contrato,
                val_matricula,
                val_procuracao,
                val_requerimento,
                val_cert_civil,
                val_cert_cnd,
                val_cert_casamento)


    def convertEntityToModel(self, entity: Usuario) -> UsuarioDBModel:
        return UsuarioDBModel(nome=entity.nome,
                              cpf=entity.cpf,
                              rg=entity.rg,
                              titulo=entity.titulo,
                              email=entity.email,
                              senha=entity.senha)

    def convertModelToEntity(self, model) -> Usuario:
        return Usuario(nome=model.nome,
                cpf=model.cpf,
                rg=model.rg,
                email=model.email,
                senha=model.senha,
                titulo=model.titulo)
