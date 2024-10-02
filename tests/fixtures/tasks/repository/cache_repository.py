from dataclasses import dataclass

import pytest


@dataclass
class FakeCacheRepository:

    async def get_tasks(self):
        return

    async def set_tasks(self, task_id: int):
        return


@pytest.fixture
def task_cache():
    return FakeCacheRepository()
