from entidades.usuario import Usuario
from persistencia.dao_base import DaoBase


class UsuarioDAO(DaoBase):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def salvar_usuario(self, usuario: Usuario) -> None:
        self.adicionar(usuario.usuario, usuario)

    def obter_usuario(self, usuario: str) -> Usuario | None:
        return self.obter(usuario)
