

class Usuario:
    def __init__(self, usuario: str, salt: str):
        self.__usuario = usuario
        self.__salt = salt

    @property
    def usuario(self) -> str:
        return self.__usuario

    @property
    def salt(self) -> str:
        return self.__salt
