import PySimpleGUI as sg
import os


class TelaValidacao:
    cwd = os.getcwd()

    def getUsuarioCpf(self):
        layout = [
            [sg.Text('Qual o cpf do usuario a acessar?')],
            [sg.Input(key='cpf_acessar')],
            [sg.Button('ok')]
        ]

        window = sg.Window('usuario a acessar', layout=layout)
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
        elif event == 'ok':
            cpf = values['cpf_acessar']
            window.close()
            return cpf

    def menu_principal(self):
        layout = [
            [sg.Text('Contrato para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='contrato'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Matricula para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='matricula'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Procuracao para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='procuracao'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Requerimento para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='requerimento'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Cert. Civil/Criminal para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='cert_civil'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Cert. CND para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='cert_cnd'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Text('Cert. casamento para validar [Deixar em branco caso não conste]')],
            [sg.InputText(key='cert_casamento'), sg.FileBrowse(initial_folder=self.cwd)],
            [sg.Button('Cadastrar')],
        ]

        window = sg.Window('Cadastrar validacoes', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'Cadastrar':
                contrato = values['contrato'] if values['contrato'] != '' else None
                matricula = values['matricula'] if values['matricula'] != '' else None
                procuracao = values['procuracao'] if values['procuracao'] != '' else None
                requerimento = values['requerimento'] if values['requerimento'] != '' else None
                cert_civil = values['cert_civil'] if values['cert_civil'] != '' else None
                cert_cnd = values['cert_cnd'] if values['cert_cnd'] != '' else None
                cert_casamento = values['cert_casamento'] if values['cert_casamento'] != '' else None
                window.close()

                return {
                    'contrato': contrato,
                    'matricula': matricula,
                    'procuracao': procuracao,
                    'requerimento': requerimento,
                    'cert_civil': cert_civil,
                    'cert_cnd': cert_cnd,
                    'cert_casamento': cert_casamento
                }
            else:
                window.close()
                break

