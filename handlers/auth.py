from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from dependency import get_auth_service
from exception import UserNotFound, UserIncorrectPassword
from schema import UserLoginSchema, UserCreateSchema
from service import AuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=UserLoginSchema
)
async def login(
        body: UserCreateSchema,
        auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    try:
        return auth_service.login(body.username, body.password)
    except UserNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
    except UserIncorrectPassword as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )
