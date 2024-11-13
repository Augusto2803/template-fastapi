from typing import Dict

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from template_fastapi.models.usuario import Usuario
from template_fastapi.repositories import UsuarioRepository
from template_fastapi.schemas.usuario import (
    UsuarioCreate,
    UsuarioCurto,
    UsuarioInDB,
    UsuarioList,
    UsuarioTrocarSenha,
    UsuarioUpdate,
)
from template_fastapi.utils.security import criar_senha_hash, verificar_senha


class UsuarioService:
    def __init__(self, session: Session):
        self.__session = session
        self.__repository = UsuarioRepository(session)

    def buscar_usuarios(self) -> UsuarioList:
        usuarios = self.__repository.buscar_todos()
        return UsuarioList(
            usuarios=[UsuarioCurto.model_validate(usuario) for usuario in usuarios],
            total=len(usuarios),
        )

    def buscar_usuario_por_id(self, usuario_id: int) -> UsuarioInDB:
        usuario = self.__repository.buscar_por_id(usuario_id)
        return UsuarioInDB.model_validate(usuario)

    def criar_usuario(self, usuario_data: UsuarioCreate) -> UsuarioInDB:
        usuario_email_existe = self.__repository.buscar_por_email(usuario_data.email)
        if usuario_email_existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='O email já está em uso',
            )

        if usuario_data.senha != usuario_data.senha_confirmacao:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='As senhas não coincidem',
            )
        else:
            usuario_data = usuario_data.model_dump()
            usuario_data.senha = criar_senha_hash(usuario_data.senha)

        usuario = Usuario(
            nome=usuario_data.nome,
            email=usuario_data.email,
            senha=usuario_data.senha,
        )

        usuario = self.__repository.criar(usuario)
        self.__session.commit()

        return UsuarioInDB.model_validate(usuario)

    def atualizar_usuario(self, usuario_id: int, usuario_data: UsuarioUpdate) -> UsuarioInDB:
        usuario = self.__repository.buscar_por_id(usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuário não encontrado',
            )

        usuario_data = usuario_data.model_dump(exclude_unset=True, exclude_none=True)

        usuario = self.__repository.atualizar(usuario, usuario_data)
        self.__session.commit()

        return UsuarioInDB.model_validate(usuario)

    def trocar_senha(self, usuario_id: int, senha_data: UsuarioTrocarSenha) -> Dict:
        usuario = self.__repository.buscar_por_id(usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuário não encontrado',
            )

        if not verificar_senha(senha_data.senha_atual, usuario.senha):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Senha atual incorreta',
            )

        if senha_data.nova_senha != senha_data.nova_senha_confirmacao:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='As novas senhas não coincidem',
            )

        usuario.senha = criar_senha_hash(senha_data.nova_senha)

        self.__repository.atualizar(usuario, {'senha': usuario.senha})
        self.__session.commit()

        return {'detail': 'Senha alterada com sucesso'}

    def deletar_usuario(self, usuario_id: int) -> Dict:
        usuario = self.__repository.buscar_por_id(usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuário não encontrado',
            )

        self.__repository.deletar(usuario)
        self.__session.commit()

        return {'detail': 'Usuário deletado com sucesso'}
