from interface.interface_base import InterfaceBase


class FormLogin(InterfaceBase):
    def __init__(self):
        super().__init__('LOGIN')

    def mostrar_tela(self) -> tuple[str, str, str]:
        super().mostrar_tela()

        while True:
            usuario = input('Digite seu usuário: ')
            senha = input('Digite sua senha: ')
            totp = input('Digite o código TOTP: ')
            if usuario and senha and totp:
                return usuario, senha, totp
            print('\nPreencha todos os campos!')
