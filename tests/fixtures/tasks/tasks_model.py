import factory
from pytest_factoryboy import register
from faker import Factory as FakerFactory

from app.tasks.models import Tasks, Categories

faker = FakerFactory.create()


@register(_name="tasks")
class TasksFactory(factory.Factory):
    class Meta:
        model = Tasks

    id = factory.LazyFunction(lambda: faker.random_int())
    name = factory.LazyFunction(lambda: faker.name())
    pomodoro_count = factory.LazyFunction(lambda: faker.random_int())
    category_id = factory.LazyFunction(lambda: faker.random_int())
    user_id = factory.LazyFunction(lambda: faker.random_int())


@register(_name="categories")
class CategoriesFactory(factory.Factory):
    class Meta:
        model = Categories

    id = factory.LazyFunction(lambda: faker.random_int())
    name = None
    type = factory.LazyFunction(lambda: faker.name())
