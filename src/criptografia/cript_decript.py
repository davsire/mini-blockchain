from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def criptografar_dados(dados: bytes, chave: str, iv: str) -> str:
    aesgcm = AESGCM(bytes.fromhex(chave))
    resultado = aesgcm.encrypt(bytes.fromhex(iv), dados, None)
    return resultado.hex()


def descriptografar_dados(dados: bytes, chave: str, iv: str) -> bytes:
    aesgcm = AESGCM(bytes.fromhex(chave))
    return aesgcm.decrypt(bytes.fromhex(iv), dados, None)
