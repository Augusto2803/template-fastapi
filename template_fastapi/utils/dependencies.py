from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from template_fastapi.core.database import SessionLocal
from template_fastapi.services import UsuarioService

# Session Dependencies


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# Service Dependencies


SessionDep = Annotated[Session, Depends(get_session)]


def get_usuario_service(session: SessionDep) -> UsuarioService:
    return UsuarioService(session=session)


UsuarioServiceDep = Annotated[UsuarioService, Depends(get_usuario_service)]
