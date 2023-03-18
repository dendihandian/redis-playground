from redis import Redis
import os

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_AUTH = os.environ.get('REDIS_AUTH')

redis = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_AUTH, charset="utf-8", decode_responses=True)
