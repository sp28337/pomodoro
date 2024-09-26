from redis import asyncio as r

from settings import Settings

settings = Settings()


def get_redis_connection() -> r.Redis:
    return r.Redis(
        host=settings.CACHE_HOST,
        port=settings.CACHE_PORT,
        db=settings.CACHE_DB
    )
