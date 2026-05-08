from interface.interface_base import InterfaceBase


class FormTotp(InterfaceBase):
    def __init__(self):
        super().__init__('TOTP')

    def mostrar_tela(self) -> str:
        super().mostrar_tela()

        while True:
            totp = input('Informe o código TOTP: ')
            if totp:
                return totp
            print('\nO TOTP não pode estar vazio!')
