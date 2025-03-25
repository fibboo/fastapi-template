from fastapi import APIRouter

from app.api.endpoints import examples
from app.schemas.error_response import responses

api_router = APIRouter(responses=responses)

api_router.include_router(examples.router, prefix='/examples', tags=['Example'])
