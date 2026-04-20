from interface.menu_base import MenuBase


class MenuApp(MenuBase):
    def __init__(self):
        super().__init__(
            'MINI-BLOCKCHAIN',
            {
                1: 'Adicionar bloco',
                2: 'Listar blocos',
                3: 'Logout'
            }
        )
