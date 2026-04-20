import os
from criptografia.cript_decript import criptografar_dados, descriptografar_dados
from criptografia.derivacao_chave import derivar_subchave
from criptografia.hash import hash_dados
from entidades.bloco import Bloco
from entidades.usuario_sessao import UsuarioSessao
from persistencia.bloco_dao import BlocoDAO


class BlocoServico:
    def __init__(self, bloco_dao: BlocoDAO):
        self.bloco_dao = bloco_dao

    def criar_bloco(self, conteudo: str, usuario_sessao: UsuarioSessao) -> None:
        id_bloco = os.urandom(8).hex()
        iv_bloco = derivar_subchave(usuario_sessao.chave_mestra, f'iv_bloco_{id_bloco}', 12)
        ultimo_bloco = self.obter_ultimo_bloco()
        hash_ultimo_bloco = hash_dados(self.serializar_bloco(ultimo_bloco)) if ultimo_bloco else '0' * 64
        dados_criptografados = criptografar_dados(conteudo.encode(), usuario_sessao.chave_sessao, iv_bloco)
        bloco = Bloco(
            id_bloco,
            dados_criptografados,
            iv_bloco,
            hash_ultimo_bloco,
            usuario_sessao.usuario.usuario
        )
        self.bloco_dao.salvar_bloco(bloco)

    def obter_blocos(self) -> list[Bloco]:
        return self.bloco_dao.obter_blocos()

    def obter_ultimo_bloco(self) -> Bloco | None:
        blocos = self.bloco_dao.obter_blocos()
        return blocos[-1] if blocos else None

    def serializar_bloco(self, bloco: Bloco) -> bytes:
        return (bloco.conteudo + bloco.iv + str(bloco.timestamp) + bloco.hash_prev + bloco.usuario).encode()

    def obter_conteudo_bloco(self, bloco: Bloco, usuario_sessao: UsuarioSessao) -> str:
        conteudo = bloco.conteudo
        if bloco.usuario == usuario_sessao.usuario.usuario:
            conteudo_bytes = descriptografar_dados(bytes.fromhex(bloco.conteudo), usuario_sessao.chave_sessao, bloco.iv)
            conteudo = conteudo_bytes.decode('utf-8')
        return conteudo
