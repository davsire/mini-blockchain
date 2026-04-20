from cryptography.hazmat.primitives import hashes


def hash_dados(dados: bytes) -> str:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(dados)
    return digest.finalize().hex()
