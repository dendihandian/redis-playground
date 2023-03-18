from redis_client import redis

print('Connected' if redis.ping() else 'Not Connected')