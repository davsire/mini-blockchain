from interface.interface_base import InterfaceBase


class Aviso(InterfaceBase):
    def __init__(self):
        super().__init__('AVISO')

    def mostrar_tela(self, mensagem: str) -> None:
        super().mostrar_tela()
        print(mensagem)
        input('Pressione ENTER para continuar...')
