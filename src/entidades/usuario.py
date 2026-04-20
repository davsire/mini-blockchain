

class Usuario:
    def __init__(self, usuario: str, salt: str):
        self.__usuario = usuario
        self.__salt = salt

    @property
    def usuario(self) -> str:
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: str) -> None:
        self.__usuario = usuario

    @property
    def salt(self) -> str:
        return self.__salt

    @salt.setter
    def salt(self, salt: str) -> None:
        self.__salt = salt
