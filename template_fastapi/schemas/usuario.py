from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=3)
    email: EmailStr = Field(...)
    senha: str = Field(..., min_length=8)
    confirmacao_senha: str = Field(..., min_length=8)


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = Field(None)


class UsuarioTrocarSenha(BaseModel):
    senha: str = Field(..., min_length=8)
    nova_senha: str = Field(..., min_length=8)
    confirmacao_nova_senha: str = Field(..., min_length=8)


class UsuarioCurto(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


class UsuarioInDB(BaseModel):
    id: int
    nome: str
    email: EmailStr
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True


class UsuarioList(BaseModel):
    usuarios: List[UsuarioCurto]
    total: int
