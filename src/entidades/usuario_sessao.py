from entidades.usuario import Usuario


class UsuarioSessao:
    def __init__(self, usuario: Usuario, chave_mestra: str, chave_totp: str, chave_sessao: str) -> None:
        self.__usuario = usuario
        self.__chave_mestra = chave_mestra
        self.__chave_totp = chave_totp
        self.__chave_sessao = chave_sessao

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def chave_mestra(self) -> str:
        return self.__chave_mestra

    @property
    def chave_totp(self) -> str:
        return self.__chave_totp

    @property
    def chave_sessao(self) -> str:
        return self.__chave_sessao
