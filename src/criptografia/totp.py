import time
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor import InvalidToken
from cryptography.hazmat.primitives.twofactor.totp import TOTP


def obter_uri_totp(chave_totp: str, usuario: str) -> str:
    totp = TOTP(bytes.fromhex(chave_totp), 6, SHA1(), 30)
    return totp.get_provisioning_uri(account_name=usuario, issuer='Mini-Blockchain')


def verificar_totp(chave_totp: str, codigo: str) -> bool:
    totp = TOTP(bytes.fromhex(chave_totp), 6, SHA1(), 30)
    tempo_atual = time.time()
    try:
        totp.verify(codigo.encode(), int(tempo_atual))
        return True
    except InvalidToken:
        return False
