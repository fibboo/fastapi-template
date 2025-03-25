from fakeredis import FakeAsyncRedis

from app.configs.settings import database_settings, settings
from redis import asyncio as aioredis

if settings.git_branch == 'tests':
    redis = FakeAsyncRedis(encoding='utf-8', decode_responses=True)
else:
    redis = aioredis.from_url(database_settings.redis_url,
                              encoding='utf-8',
                              decode_responses=True,
                              health_check_interval=10,
                              socket_connect_timeout=5,
                              retry_on_timeout=True,
                              socket_keepalive=True)
