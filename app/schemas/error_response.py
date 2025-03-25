from enum import Enum

from pydantic import BaseModel
from starlette import status


class ErrorCodeType(str, Enum):
    ENTITY_NOT_FOUND = 'ENTITY_NOT_FOUND'
    INTEGRITY_ERROR = 'INTEGRITY_ERROR'

    NOT_IMPLEMENTED = 'NOT_IMPLEMENTED'


class ErrorResponse(BaseModel):
    message: str
    error_code: ErrorCodeType | None = None


responses = {
    status.HTTP_418_IM_A_TEAPOT: {
        'description': 'Custom errors with possible codes: 400, 401, 403, 404, 409, 501',
        'model': ErrorResponse
    }
}
