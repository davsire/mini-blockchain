import os
from criptografia.derivacao_chave import derivar_senha, derivar_subchave
from criptografia.totp import verificar_totp
from entidades.usuario import Usuario
from entidades.usuario_sessao import UsuarioSessao
from persistencia.usuario_dao import UsuarioDAO


class UsuarioServico:
    def __init__(self, usuario_dao: UsuarioDAO):
        self.usuario_dao = usuario_dao

    def criar_usuario(self, usuario: str, senha: str) -> UsuarioSessao:
        usuario_existente = self.usuario_dao.obter_usuario(usuario)
        if usuario_existente:
            raise Exception('Usuário já existe.')

        salt = os.urandom(16).hex()
        senha_derivada = derivar_senha(senha, salt, 32)
        usuario_salvar = Usuario(usuario, senha_derivada, salt)
        self.usuario_dao.salvar_usuario(usuario_salvar)

        chave_totp = derivar_subchave(senha_derivada, 'totp', 20)
        chave_sessao = derivar_subchave(senha_derivada, 'sessao', 32)
        return UsuarioSessao(usuario_salvar, senha_derivada, chave_totp, chave_sessao)

    def validar_login_senha(self, usuario: str, senha: str) -> UsuarioSessao:
        usuario_base = self.usuario_dao.obter_usuario(usuario)
        if usuario_base is None:
            raise Exception('Usuário não encontrado.')

        senha_derivada = derivar_senha(senha, usuario_base.salt, 32)
        senha_valida = senha_derivada == usuario_base.senha
        if not senha_valida:
            raise Exception('Senha inválida.')

        chave_totp = derivar_subchave(senha_derivada, 'totp', 20)
        chave_sessao = derivar_subchave(senha_derivada, 'sessao', 32)
        return UsuarioSessao(usuario_base, senha_derivada, chave_totp, chave_sessao)

    def validar_totp(self, usuario_sessao: UsuarioSessao, totp: str) -> None:
        valido = verificar_totp(usuario_sessao.chave_totp, totp)
        if not valido:
            raise Exception('TOTP inválido.')
