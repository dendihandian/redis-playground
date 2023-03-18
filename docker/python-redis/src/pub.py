from redis_client import redis
from sys import argv

if __name__ == '__main__':

    try:

        message = argv[1]
        redis.publish('messages', message)

    except Exception as e:
        print(e)