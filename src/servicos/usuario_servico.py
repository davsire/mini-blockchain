import os
from criptografia.derivacao_chave import derivar_chave_mestra, derivar_subchave
from criptografia.hash import hash_dados
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
        usuario_salvar = Usuario(usuario, hash_dados(senha.encode()), salt)
        self.usuario_dao.salvar_usuario(usuario_salvar)

        chave_mestra = derivar_chave_mestra(senha, salt, 32)
        chave_totp = derivar_subchave(chave_mestra, 'totp', 20)
        chave_sessao = derivar_subchave(chave_mestra, 'sessao', 32)

        return UsuarioSessao(usuario_salvar, chave_mestra, chave_totp, chave_sessao)

    def validar_login_senha(self, usuario: str, senha: str) -> UsuarioSessao:
        usuario_base = self.usuario_dao.obter_usuario(usuario)
        if usuario_base is None:
            raise Exception('Usuário não encontrado.')

        senha_valida = hash_dados(senha.encode()) == usuario_base.senha
        if not senha_valida:
            raise Exception('Senha inválida.')

        chave_mestra = derivar_chave_mestra(senha, usuario_base.salt, 32)
        chave_totp = derivar_subchave(chave_mestra, 'totp', 20)
        chave_sessao = derivar_subchave(chave_mestra, 'sessao', 32)
        return UsuarioSessao(usuario_base, chave_mestra, chave_totp, chave_sessao)

    def validar_totp(self, usuario_sessao: UsuarioSessao, totp: str) -> None:
        valido = verificar_totp(usuario_sessao.chave_totp, totp)
        if not valido:
            raise Exception('TOTP inválido.')
