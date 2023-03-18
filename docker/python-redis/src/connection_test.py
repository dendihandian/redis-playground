from redis_client import redis

if __name__ == '__main__':
    print('Connected' if redis.ping() else 'Not Connected')