from typing import Dict

from fastapi import APIRouter, status

from template_fastapi.schemas.usuario import (
    UsuarioCreate,
    UsuarioInDB,
    UsuarioList,
    UsuarioTrocarSenha,
    UsuarioUpdate,
)
from template_fastapi.utils.dependencies import UsuarioServiceDep as UsuarioService

router = APIRouter()


@router.get('/', response_model=UsuarioList, name='Listar usuários', status_code=status.HTTP_200_OK)
def listar_usuarios(usuario_service: UsuarioService):
    return usuario_service.buscar_usuarios()


@router.post(
    '/', response_model=UsuarioInDB, name='Criar usuário', status_code=status.HTTP_201_CREATED
)
def criar_usuario(usuario_in: UsuarioCreate, usuario_service: UsuarioService):
    return usuario_service.criar_usuario(usuario_in)


@router.get(
    '/{usuario_id}',
    response_model=UsuarioInDB,
    name='Buscar usuário',
    status_code=status.HTTP_200_OK,
)
def buscar_usuario(usuario_id: int, usuario_service: UsuarioService):
    return usuario_service.buscar_usuario_por_id(usuario_id)


@router.patch(
    '/{usuario_id}',
    response_model=UsuarioInDB,
    name='Atualizar usuário',
    status_code=status.HTTP_200_OK,
)
def atualizar_usuario(usuario_id: int, usuario_in: UsuarioUpdate, usuario_service: UsuarioService):
    return usuario_service.atualizar_usuario(usuario_id, usuario_in)


@router.delete(
    '/{usuario_id}', response_model=Dict, name='Deletar usuário', status_code=status.HTTP_200_OK
)
def deletar_usuario(usuario_id: int, usuario_service: UsuarioService):
    return usuario_service.deletar_usuario(usuario_id)


@router.patch(
    '/{usuario_id}/trocar-senha',
    response_model=Dict,
    name='Trocar senha',
    status_code=status.HTTP_200_OK,
)
def trocar_senha(usuario_id: int, usuario_in: UsuarioTrocarSenha, usuario_service: UsuarioService):
    return usuario_service.trocar_senha(usuario_id, usuario_in)
