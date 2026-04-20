from interface.interface_base import InterfaceBase


class FormBloco(InterfaceBase):
    def __init__(self):
        super().__init__('ADICIONAR BLOCO')

    def mostrar_tela(self) -> str:
        super().mostrar_tela()

        while True:
            conteudo = input('Informe o conteúdo do bloco: ')
            if conteudo:
                return conteudo
            print('\nO conteúdo não pode estar vazio!')
