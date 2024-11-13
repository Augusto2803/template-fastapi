from fastapi import FastAPI

from template_fastapi.api import api_router
from template_fastapi.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)


app.include_router(api_router)


@app.get(
    '/healthcheck',
    tags=['healthcheck'],
)
async def healthcheck() -> dict:
    return {'status': 'running'}
