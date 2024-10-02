import pytest

from app.users.auth.schema import UserLoginSchema
from app.users.auth.service import AuthService
from app.users.user_profile.repository import UserRepository
from app.users.user_profile.schema import UserCreateSchema

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_create_user__success(
    fake_user_repository: UserRepository,
    auth_service_mock: AuthService
):
    username = "adik"
    password = "Rust"
    access_token = auth_service_mock.generate_access_token(user_id="1")
    user_data = UserCreateSchema(username=username, password=password)

    user = await fake_user_repository.create_user(user_data)
    user_login_schema = UserLoginSchema(
        user_id=user.id,
        access_token=access_token
    )
    assert isinstance(user_login_schema, UserLoginSchema)
    assert user_login_schema.access_token == access_token


@pytest.mark.asyncio
async def test_create_user__fail(
    fake_user_repository: UserRepository,
    auth_service_mock: AuthService
):
    username = "adik"
    password = "Rust"
    access_token = auth_service_mock.generate_access_token(user_id="1")
    user_data = UserCreateSchema(username=username, password=password)

    user = await fake_user_repository.create_user(user_data)
    user_login_schema = UserLoginSchema(
        user_id=user.id,
        access_token="accesdfhs3769sdfstofhken"
    )
    assert isinstance(user_login_schema, UserLoginSchema)
    assert user_login_schema.access_token != access_token
