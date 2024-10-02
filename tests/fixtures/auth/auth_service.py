import pytest

from app.settings import Settings
from app.users.auth.service import AuthService
# from app.users.user_profile.repository import UserRepository


@pytest.fixture
def auth_service_mock(yandex_client, google_client, fake_user_repository):
    return AuthService(
        user_repository=fake_user_repository,
        settings=Settings(),
        google_client=google_client,
        yandex_client=yandex_client,
    )
#
#
# @pytest.fixture
# def auth_service(yandex_client, google_client, auth_service_mock, db_session):
#     return AuthService(
#         user_repository=UserRepository(db_session=db_session),
#         settings=Settings(),
#         google_client=google_client(),
#         yandex_client=yandex_client(),
#     )
