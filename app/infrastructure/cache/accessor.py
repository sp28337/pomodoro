from redis import asyncio as r

from app.settings import Settings


def get_redis_connection() -> r.Redis:
    settings = Settings()
    return r.Redis(
        host=settings.CACHE_HOST,
        port=settings.CACHE_PORT,
        db=settings.CACHE_DB,
    )
