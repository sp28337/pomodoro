import redis as r


def get_redis_connection() -> r.Redis:
    return r.Redis(
        host="localhost",
        port=6379,
        db=0
    )
