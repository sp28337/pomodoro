import pytest

from dataclasses import dataclass

from app.users.user_profile.schema import UserCreateSchema
from tests.fixtures.users.user_model import UserProfileFactory


@dataclass
class FakeUserReposytory:

    async def get_user_by_email(self, email: str) -> None:
        return UserProfileFactory(email=email)

    async def create_user(self, user_data: UserCreateSchema):
        return UserProfileFactory(username=user_data.username, password=user_data.password)

    async def get_user(self, user_id: int):
        return UserProfileFactory(id=user_id)

    async def get_user_by_username(self, username: str):
        return UserProfileFactory(username=username)


@pytest.fixture
def fake_user_repository():
    return FakeUserReposytory()
