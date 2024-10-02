import pytest
import datetime as dt

from jose import jwt

from app.settings import Settings
from app.users.auth.schema import UserLoginSchema
from app.users.auth.service import AuthService
from app.users.user_profile.models import UserProfile

pytestmark = pytest.mark.asyncio


async def test_get_google_redirect_uri__success(auth_service_mock: AuthService, settings: Settings):
    settings_google_redirect_uri = settings.google_redirect_uri
    auth_service_mock_google_redirect_uri = auth_service_mock.get_google_redirect_uri()
    assert settings_google_redirect_uri == auth_service_mock_google_redirect_uri


async def test_get_yandex_redirect_uri__success(auth_service_mock: AuthService, settings: Settings):
    settings_yandex_redirect_uri = settings.yandex_redirect_uri
    auth_service_mock_yandex_redirect_uri = auth_service_mock.get_yandex_redirect_uri()
    assert settings_yandex_redirect_uri == auth_service_mock_yandex_redirect_uri


async def test_google_redirect_uri__fail(auth_service_mock: AuthService, settings: Settings):
    settings_google_redirect_uri = "https://fake_google_redirect_uri.com"
    auth_service_mock_google_redirect_uri = auth_service_mock.get_google_redirect_uri()
    assert settings_google_redirect_uri != auth_service_mock_google_redirect_uri


async def test_yandex_redirect_uri__fail(auth_service_mock: AuthService, settings: Settings):
    settings_yandex_redirect_uri = "https://fake_yandex_redirect_uri.com"
    auth_service_mock_yandex_redirect_uri = auth_service_mock.get_yandex_redirect_uri()
    assert settings_yandex_redirect_uri != auth_service_mock_yandex_redirect_uri


async def test_generate_access_token__success(auth_service_mock: AuthService, settings: Settings):
    user_id = str(1)
    access_token = auth_service_mock.generate_access_token(user_id=user_id)
    decode_access_token = jwt.decode(
        token=access_token,
        key=settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ENCODE_ALGORITHM]
    )
    decoded_user_id = decode_access_token.get("user_id")
    decoded_token_expire = dt.datetime.fromtimestamp(decode_access_token.get("expire"), tz=dt.timezone.utc)
    assert (decoded_token_expire - dt.datetime.now(tz=dt.UTC)) > dt.timedelta(days=6)
    assert decoded_user_id == user_id


async def test_get_user_id_from_access_token__success(auth_service_mock: AuthService):
    user_id = str(1)
    access_token = auth_service_mock.generate_access_token(user_id=user_id)
    decoded_user_id = auth_service_mock.get_user_id_from_access_token(token=access_token)
    assert decoded_user_id == user_id


async def test_google_auth__success(auth_service_mock: AuthService):
    code = "fake_code"
    user = await auth_service_mock.google_auth(code=code)
    decoded_user_id = auth_service_mock.get_user_id_from_access_token(token=user.access_token)
    assert user.user_id == decoded_user_id
    assert isinstance(user, UserLoginSchema)


async def test_yandex_auth__success(auth_service_mock: AuthService):
    code = "fake_code"
    user = await auth_service_mock.yandex_auth(code=code)
    decoded_user_id = auth_service_mock.get_user_id_from_access_token(token=user.access_token)
    assert user.user_id == decoded_user_id
    assert isinstance(user, UserLoginSchema)


async def test_login__success(auth_service_mock: AuthService):
    name = "adik"
    user_id = "1"
    user = await auth_service_mock.user_repository.get_user_by_username(username=name)

    assert isinstance(user, UserProfile)
    assert user.username == name

    access_token = auth_service_mock.generate_access_token(user_id=user_id)
    login_schema = UserLoginSchema(access_token=access_token, user_id=user_id)

    assert isinstance(login_schema, UserLoginSchema)
    assert login_schema.user_id == 1
