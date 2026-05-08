import os
import time
from criptografia.cript_decript import criptografar_dados, descriptografar_dados
from criptografia.derivacao_chave import derivar_subchave
from criptografia.hash import hash_dados
from entidades.bloco import Bloco
from entidades.usuario_sessao import UsuarioSessao
from persistencia.bloco_dao import BlocoDAO


class BlocoServico:
    def __init__(self, bloco_dao: BlocoDAO):
        self.bloco_dao = bloco_dao
        self.hash_vazio = '0' * 64

    def criar_bloco(self, conteudo: str, usuario_sessao: UsuarioSessao) -> None:
        cadeia_valida = self.validar_cadeia()
        if not cadeia_valida:
            raise Exception('Não foi possível adicionar. Cadeia de blocos inválida.')
        id_bloco = os.urandom(8).hex()
        iv_bloco = self.obter_iv_bloco(usuario_sessao, id_bloco)
        ultimo_bloco = self.obter_ultimo_bloco()
        hash_ultimo_bloco = hash_dados(ultimo_bloco.serializar_bloco()) if ultimo_bloco else self.hash_vazio
        dados_criptografados = criptografar_dados(conteudo.encode(), usuario_sessao.chave_sessao, iv_bloco)
        bloco = Bloco(
            id_bloco,
            dados_criptografados,
            hash_ultimo_bloco,
            usuario_sessao.usuario.usuario
        )
        self.bloco_dao.salvar_bloco(bloco)

    def obter_blocos_lista(self, usuario_sessao: UsuarioSessao) -> list[dict[str, str]]:
        blocos = self.bloco_dao.obter_blocos()
        blocos_lista: list[dict[str, str]] = []
        hash_bloco_anterior = self.hash_vazio
        for bloco in blocos:
            conteudo, adulterado = self.obter_conteudo_bloco(bloco, usuario_sessao)
            bloco_lista = {
                'ID': bloco.id_bloco,
                'Usuário': bloco.usuario,
                'Hash anterior': bloco.hash_prev,
                'Hash anterior válido': '✓ VÁLIDO' if hash_bloco_anterior == bloco.hash_prev else '✗ INVÁLIDO',
                'Timestamp': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(bloco.timestamp)),
                'Conteúdo': conteudo,
            }
            if bloco.usuario == usuario_sessao.usuario.usuario:
                bloco_lista['Status bloco'] = '✗ ADULTERADO' if adulterado else '✓ VÁLIDO'
            blocos_lista.append(bloco_lista)
            hash_bloco_anterior = hash_dados(bloco.serializar_bloco())
        return blocos_lista

    def adulterar_bloco(self, id_bloco: str, campo: int, novo_valor: str):
        bloco = self.bloco_dao.obter_bloco(id_bloco)
        if bloco is None:
            raise Exception('Bloco não encontrado.')
        if campo == 1:
            bloco.conteudo = novo_valor
        elif campo == 2:
            bloco.hash_prev = novo_valor
        else:
            raise Exception('Campo inválido.')
        bloco.timestamp = time.time()
        self.bloco_dao.salvar_bloco(bloco)

    def obter_ultimo_bloco(self) -> Bloco | None:
        blocos = self.bloco_dao.obter_blocos()
        return blocos[-1] if blocos else None

    def obter_conteudo_bloco(self, bloco: Bloco, usuario_sessao: UsuarioSessao) -> tuple[str, bool]:
        conteudo = bloco.conteudo
        adulterado = False
        if bloco.usuario == usuario_sessao.usuario.usuario:
            try:
                iv_bloco = self.obter_iv_bloco(usuario_sessao, bloco.id_bloco)
                conteudo_bytes = descriptografar_dados(bytes.fromhex(bloco.conteudo), usuario_sessao.chave_sessao, iv_bloco)
                conteudo = conteudo_bytes.decode('utf-8')
            except:
                adulterado = True
        return conteudo, adulterado

    def obter_iv_bloco(self, usuario_sessao: UsuarioSessao, id_bloco: str) -> str:
        return derivar_subchave(usuario_sessao.chave_mestra, f'iv_bloco_{id_bloco}', 12)

    def validar_cadeia(self) -> bool:
        blocos = self.bloco_dao.obter_blocos()
        hash_bloco_anterior = self.hash_vazio
        for bloco in blocos:
            if hash_bloco_anterior != bloco.hash_prev:
                return False
            hash_bloco_anterior = hash_dados(bloco.serializar_bloco())
        return True
