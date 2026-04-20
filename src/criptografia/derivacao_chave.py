from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derivar_chave_mestra(senha: str, salt: str, tamanho: int) -> str:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=tamanho,
        salt=bytes.fromhex(salt),
        iterations=100_000,
    )
    chave_mestra = kdf.derive(senha.encode())
    return chave_mestra.hex()


def derivar_subchave(chave_mestra: str, contexto: str, tamanho: int) -> str:
    kdf = HKDF(
        algorithm=hashes.SHA256(),
        length=tamanho,
        salt=None,
        info=contexto.encode()
    )
    subchave = kdf.derive(bytes.fromhex(chave_mestra))
    return subchave.hex()
