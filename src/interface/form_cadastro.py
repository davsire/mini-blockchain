from interface.interface_base import InterfaceBase


class FormCadastro(InterfaceBase):
    def __init__(self):
        super().__init__('CADASTRO')

    def mostrar_tela(self) -> tuple[str, str]:
        super().mostrar_tela()

        while True:
            usuario = input('Digite seu usuário: ')
            senha = input('Digite sua senha: ')
            confirmacao_senha = input('Confirme sua senha: ')
            if not usuario or not senha or not confirmacao_senha:
                print('Preencha todos os campos!')
                continue
            if senha != confirmacao_senha:
                print('A senha e a confirmação da senha devem ser iguais!')
                continue
            return usuario, senha
