from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
