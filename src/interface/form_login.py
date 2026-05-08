from interface.interface_base import InterfaceBase


class FormLogin(InterfaceBase):
    def __init__(self):
        super().__init__('LOGIN')

    def mostrar_tela(self) -> tuple[str, str]:
        super().mostrar_tela()

        while True:
            usuario = input('Informe seu usuário: ')
            senha = input('Informe sua senha: ')
            if usuario and senha:
                return usuario, senha
            print('\nPreencha todos os campos!')
