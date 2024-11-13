from fastapi import APIRouter

from .endpoints.api import usuario_router

api_router = APIRouter(prefix='/api')


api_router.include_router(usuario_router, prefix='/usuario', tags=['usuario'])
