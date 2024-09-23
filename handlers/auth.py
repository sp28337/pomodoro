from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from dependency import get_auth_service
from exception import UserNotFound, UserIncorrectPassword
from schema import UserLoginSchema, UserCreateSchema
from service import AuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserLoginSchema)
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


@router.get("/login/google", response_class=RedirectResponse)
async def google_login(
  auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    redirect_uri = auth_service.get_google_redirect_uri()
    print(redirect_uri)
    return RedirectResponse(redirect_uri)


@router.get("/google")
async def google_auth(
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    code: str
):
    return auth_service.google_auth(code=code)


@router.get("login/yandex", response_class=RedirectResponse)
async def yandex_login(
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    redirect_uri = auth_service.get_yandex_redirect_uri()
    print(redirect_uri)
    return RedirectResponse(redirect_uri)


@router.get("/yandex")
async def yandex_auth(
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    code: str
):
    return auth_service.yandex_auth(code=code)
