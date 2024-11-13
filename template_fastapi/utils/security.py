from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


def criar_senha_hash(senha: str) -> str:
    return pwd_context.hash(senha)
