from redis_client import redis

sub = redis.pubsub()
sub.subscribe('messages')

if __name__ == '__main__':

    listen = True
    while listen:
        for message in sub.listen():

            print(message)

            if message['data'] == 'stop':
                listen = False
                break
