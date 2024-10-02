import pytest

from app.users.user_profile.repository import UserRepository
from app.users.user_profile.service import UserService
from app.users.auth.service import AuthService


@pytest.fixture
def user_service(fake_user_repository: UserRepository, mock_auth_service: AuthService):
    return UserService(
        user_repository=fake_user_repository,
        auth_service=mock_auth_service,
    )
