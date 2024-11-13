from abc import ABC
from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy.future import select
from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    def __init__(self, session: Session, modelo: Type[T]):
        self.__session = session
        self.__modelo = modelo

    def buscar_por_id(self, id: int) -> Optional[T]:
        return self.__session.execute(select(self.__modelo).filter_by(id=id)).scalar_one_or_none()

    def buscar_todos(self) -> List[T]:
        return self.__session.query(self.__modelo).all()

    def criar(self, obj: T) -> T:
        self.__session.add(obj)
        self.__session.flush()
        return obj

    def atualizar(self, obj_db: T, obj_in: dict) -> T:
        for campo, valor in obj_in.items():
            if hasattr(obj_db, campo):
                setattr(obj_db, campo, valor)
        self.__session.add(obj_db)
        self.__session.flush()
        return obj_db

    def deletar(self, obj: T) -> None:
        self.__session.delete(obj)
