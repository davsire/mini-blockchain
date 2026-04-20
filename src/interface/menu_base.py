from interface.interface_base import InterfaceBase


class MenuBase(InterfaceBase):
    def __init__(self, titulo: str, opcoes_menu: dict[int, str]):
        super().__init__(titulo)
        self.opcoes_menu = opcoes_menu

    def mostrar_tela(self) -> int:
        super().mostrar_tela()

        for opcao, label in self.opcoes_menu.items():
            print(f'{opcao} - {label}')

        while True:
            try:
                opcao = int(input('Informe o número da opção desejada: '))
                if opcao not in self.opcoes_menu:
                    raise ValueError
                return opcao
            except ValueError:
                print('Informe uma opção válida!')
