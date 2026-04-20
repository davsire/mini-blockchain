from interface.interface_base import InterfaceBase


class ListaBlocos(InterfaceBase):
    def __init__(self):
        super().__init__('LISTA DE BLOCOS')

    def mostrar_tela(self, blocos: list[dict[str, str]]) -> None:
        super().mostrar_tela()

        if not blocos:
            print('Não há blocos para listar.')
        else:
            for bloco in blocos:
                print('-' * 20)
                for (chave, valor) in bloco.items():
                    print(f'{chave}: {valor}')
            print('-' * 20)
        print()
        input('Pressione ENTER para continuar...')
