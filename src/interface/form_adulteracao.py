from interface.interface_base import InterfaceBase


class FormAdulteracao(InterfaceBase):
    def __init__(self):
        super().__init__('ADULTERAR BLOCO')

    def mostrar_tela(self) -> tuple[str, int, str]:
        super().mostrar_tela()

        while True:
            try:
                id_bloco = input('Informe o ID do bloco: ')
                campo = int(input('Informe o campo a ser alterado (1 - conteudo; 2 - hash_prev): '))
                if campo not in [1, 2]:
                    raise Exception('Campo inválido')
                novo_valor = input('Informe o novo valor: ')
                if id_bloco and novo_valor:
                    return id_bloco, campo, novo_valor
                print('\nPreencha todos os campos!')
            except Exception as e:
                print(f'\n{e}')
