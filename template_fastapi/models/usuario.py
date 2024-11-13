from sqlalchemy import Boolean, Column, Integer, String

from template_fastapi.models.base import Base
from template_fastapi.models.mixins import TimestampMixin


class Usuario(Base, TimestampMixin):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Usuario {self.id} - {self.nome}>'
