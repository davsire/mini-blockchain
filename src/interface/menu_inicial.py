from interface.menu_base import MenuBase


class MenuInicial(MenuBase):
    def __init__(self):
        super().__init__(
            'MINI-BLOCKCHAIN',
            {
                1: 'Login',
                2: 'Cadastro',
                3: 'Sair'
            }
        )
