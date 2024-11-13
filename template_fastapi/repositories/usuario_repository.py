from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from template_fastapi.models.usuario import Usuario
from template_fastapi.repositories import BaseRepository


class UsuarioRepository(BaseRepository[Usuario]):
    def __init__(self, session: Session):
        self.__session = session
        super().__init__(session, Usuario)

    def buscar_por_email(self, email: str) -> Usuario:
        return self.__session.execute(
            select(Usuario).filter(Usuario.email == email)
        ).scalar_one_or_none()
