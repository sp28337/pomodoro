import json

from redis import Redis

from schema import TaskSchema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_tasks(self) -> list[TaskSchema] | None:
        with self.redis as radis:
            tasks_json = radis.lrange("tasks", 0, -1)
            return [TaskSchema.model_validate(json.loads(task)) for task in tasks_json]

    def set_tasks(self, tasks: list[TaskSchema] | None):
        if tasks_json := [task.model_dump_json() for task in tasks]:
            with self.redis as redis:
                redis.lpush("tasks", *tasks_json, )
