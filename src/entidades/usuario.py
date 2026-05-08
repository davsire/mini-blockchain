

class Usuario:
    def __init__(self, usuario: str, senha: str, salt: str):
        self.__usuario = usuario
        self.__senha = senha
        self.__salt = salt

    @property
    def usuario(self) -> str:
        return self.__usuario

    @property
    def senha(self) -> str:
        return self.__senha

    @property
    def salt(self) -> str:
        return self.__salt
