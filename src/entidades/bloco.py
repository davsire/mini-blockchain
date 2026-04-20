import time


class Bloco:
    def __init__(
        self,
        id_bloco: str,
        conteudo: str,
        iv: str,
        hash_prev: str,
        usuario: str
    ):
        self.__id_bloco = id_bloco
        self.__conteudo = conteudo
        self.__iv = iv
        self.__timestamp = time.time()
        self.__hash_prev = hash_prev
        self.__usuario = usuario

    @property
    def id_bloco(self) -> str:
        return self.__id_bloco

    @property
    def conteudo(self) -> str:
        return self.__conteudo

    @property
    def iv(self) -> str:
        return self.__iv

    @property
    def timestamp(self) -> float:
        return self.__timestamp

    @property
    def hash_prev(self) -> str:
        return self.__hash_prev

    @property
    def usuario(self) -> str:
        return self.__usuario
