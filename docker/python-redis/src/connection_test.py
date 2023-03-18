from redis_client import redis
import os

os.environ.get('MY_VARIABLE')

print('Connected' if redis.ping else 'Not Connected')