from typing import List
import PySimpleGUI as sg
import os

from package.entidades.ValidacaoDocumentoEnum import ValidacaoDocumentoEnum


class TelaValidacao:
    cwd = os.getcwd()

    def getUsuarioCpf(self):
        layout = [
            [sg.Text("Qual o cpf do usuario a acessar?")],
            [sg.Input(key="cpf_acessar")],
            [sg.Button("ok")],
        ]

        window = sg.Window("usuario a acessar", layout=layout)
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
        elif event == "ok":
            cpf = values["cpf_acessar"]
            window.close()
            return cpf

    def menu_principal(self):
        layout = [
            [sg.Text("Contrato para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="contrato"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text("Matricula para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="matricula"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text("Procuracao para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="procuracao"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text("Requerimento para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="requerimento"), sg.FileBrowse(initial_folder=self.cwd)],
            [
                sg.Text(
                    "Cert. Civil/Criminal para validar [Deixar em branco caso não conste]"
                )
            ],
            [sg.InputText(key="cert_civil"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text("Cert. CND para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="cert_cnd"), sg.FileBrowse(initial_folder=self.cwd)],
            [
                sg.Text(
                    "Cert. casamento para validar [Deixar em branco caso não conste]"
                )
            ],
            [
                sg.InputText(key="cert_casamento"),
                sg.FileBrowse(initial_folder=self.cwd),
            ],
            [
                sg.Text(
                    "Documento. de Identidade Nacional para validar [Deixar em branco caso não conste]"
                )
            ],
            [
                sg.InputText(key="documento_identidade"),
                sg.FileBrowse(initial_folder=self.cwd),
            ],
            [
                sg.Text(
                    "Certificado Nacional de Habilitação para validar [Deixar em branco caso não conste]"
                )
            ],
            [sg.InputText(key="documento_cnh"), sg.FileBrowse(initial_folder=self.cwd)],
            [
                sg.Text(
                    "Cert. trabalhista para validar [Deixar em branco caso não conste]"
                )
            ],
            [
                sg.InputText(key="cert_trabalhista"),
                sg.FileBrowse(initial_folder=self.cwd),
            ],
            [
                sg.Text(
                    "Cert. nascimento para validar [Deixar em branco caso não conste]"
                )
            ],
            [
                sg.InputText(key="cert_nascimento"),
                sg.FileBrowse(initial_folder=self.cwd),
            ],
            [sg.Text("Cert. estadual para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="cert_estadual"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text("Cert. federal para validar [Deixar em branco caso não conste]")],
            [sg.InputText(key="cert_federal"), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Button("Cadastrar")],
        ]

        window = sg.Window("Cadastrar validacoes", layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == "Cadastrar":
                contrato = values["contrato"] if values["contrato"] != "" else None
                matricula = values["matricula"] if values["matricula"] != "" else None
                procuracao = (
                    values["procuracao"] if values["procuracao"] != "" else None
                )
                requerimento = (
                    values["requerimento"] if values["requerimento"] != "" else None
                )
                cert_civil = (
                    values["cert_civil"] if values["cert_civil"] != "" else None
                )
                cert_cnd = values["cert_cnd"] if values["cert_cnd"] != "" else None
                cert_casamento = (
                    values["cert_casamento"] if values["cert_casamento"] != "" else None
                )
                documento_identidade = (
                    values["documento_identidade "]
                    if values["documento_identidade "] != ""
                    else None
                )
                documento_cnh = (
                    values["documento_cnh"] if values["documento_cnh"] != "" else None
                )
                cert_trabalhista = (
                    values["cert_trabalhista"]
                    if values["cert_trabalhista"] != ""
                    else None
                )
                cert_nascimento = (
                    values["cert_nascimento"]
                    if values["cert_nascimento"] != ""
                    else None
                )
                cert_estadual = (
                    values["cert_estadual"] if values["cert_estadual"] != "" else None
                )
                cert_federal = (
                    values["cert_federal"] if values["cert_federal"] != "" else None
                )

                window.close()

                return {
                    "contrato": contrato,
                    "matricula": matricula,
                    "procuracao": procuracao,
                    "requerimento": requerimento,
                    "cert_civil": cert_civil,
                    "cert_cnd": cert_cnd,
                    "cert_casamento": cert_casamento,
                    "documento_identidade": documento_identidade,
                    "documento_cnh": documento_cnh,
                    "cert_trabalhista": cert_trabalhista,
                    "cert_nascimento": cert_nascimento,
                    "cert_estadual": cert_estadual,
                    "cert_federal": cert_federal,
                }
            else:
                window.close()
                break

    def documentos_validados(self, validacoes: List[ValidacaoDocumentoEnum]):
        documentos = [[sg.Text(e.name)] for e in validacoes]
        layout = [
            [sg.Text("Documentos Validados:")],
            *documentos,
            [sg.Button("OK")],
        ]

        window = sg.Window("Validacao", layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == "OK":
                window.close()
                break
