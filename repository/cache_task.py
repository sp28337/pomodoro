import json

from redis import asyncio as Redis

from schema import TaskSchema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_tasks(self) -> list[TaskSchema] | None:
        async with self.redis as radis:
            tasks_json = await radis.lrange("tasks", 0, -1)
            return [TaskSchema.model_validate(json.loads(task)) for task in tasks_json]

    async def set_tasks(self, tasks: list[TaskSchema] | None):
        if tasks_json := [task.model_dump_json() for task in tasks]:
            async with self.redis as redis:
                await redis.lpush("tasks", *tasks_json, )
