pytest_plugins = [
    "tests.fixtures.settings",
    "tests.fixtures.auth.clients",
    "tests.fixtures.auth.auth_service",
    "tests.fixtures.tasks.tasks_service",
    "tests.fixtures.tasks.tasks_model",
    "tests.fixtures.users.user_model",
    "tests.fixtures.users.user_service",
    "tests.fixtures.users.user_repository",
    "tests.fixtures.tasks.repository.task_repository",
    "tests.fixtures.tasks.repository.cache_repository",
]
