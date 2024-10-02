import pytest

from app.tasks.repository import TaskRepository
from app.tasks.schema import TaskSchema, TaskCreateSchema

pytestmark = pytest.mark.asyncio


async def test_get_tasks__success(fake_task_repository: TaskRepository):
    tasks = await fake_task_repository.get_tasks()
    tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
    assert isinstance(tasks_schema, list)
    assert len(tasks) == 5
    assert isinstance(tasks_schema[0], TaskSchema)


async def test_create_task__success(fake_task_repository: TaskRepository):
    user_id = 7
    task_id = await fake_task_repository.create_task(task=TaskCreateSchema(), user_id=user_id)
    task = await fake_task_repository.get_task(task_id)
    task_schema = TaskSchema.model_validate(task)
    print("\n\n", task_schema, sep="")
    assert task_schema.id == user_id
    assert isinstance(task_schema, TaskSchema)


async def test_update_task_name__success(fake_task_repository: TaskRepository):
    task_id, name = 10, "adik"

    task = await fake_task_repository.update_task_name(task_id=task_id, name=name)
    task_schema = TaskSchema.model_validate(task)

    assert isinstance(task_schema, TaskSchema)
    assert task_schema.id == task_id
    assert task_schema.name == name
