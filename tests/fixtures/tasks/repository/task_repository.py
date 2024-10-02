from dataclasses import dataclass

import pytest

from app.tasks.schema import TaskCreateSchema
from tests.fixtures.tasks.tasks_model import TasksFactory, CategoriesFactory


@dataclass
class FakeTaskRepository:

    async def get_tasks(self):
        return [TasksFactory() for _ in range(5)]

    async def get_task(self, task_id: int):
        return TasksFactory(id=task_id)

    async def get_user_task(self, task_id: int, user_id: int):
        return TasksFactory(id=task_id, user_id=user_id)

    async def create_task(self, task: TaskCreateSchema, user_id: int):
        return user_id

    async def update_task_name(self, task_id: int, name: str):
        return TasksFactory(id=task_id, name=name)


@pytest.fixture
def fake_task_repository():
    return FakeTaskRepository()
