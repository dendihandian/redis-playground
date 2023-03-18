# Redis Playground

## Requirements

- Docker
- Docker-Compose

___________

## Setup

1. Clone or download this project repository (obviously).

```
git clone https://github.com/dendihandian/redis-playground.git
```

2. Duplicate `.env.example` into `.env` in the same directory. You may want to change the values if needed or leave it.

3. Run one of these commands:

    - Redis only:
    ```
    docker-compose up -d redis
    ```

    - Playing with `PHPRedisAdmin` only:
    ```
    docker-compose up -d redis phpredisadmin
    ```

    - Playing with `RedisCommander` only:
    ```
    docker-compose up -d redis redis-commander
    ```

    - Playing with python redis scripts only:
    ```
    docker-compose up -d redis python-redis
    ```

    - Run all services:
    ```
    docker-compose up -d
    ```

____________

## Services

### Redis (Server)

The service can be accessed using local machine apps and redis desktop clients/GUI at `localhost:6379` by default configuration.
You can play with Redis-CLI with this service by executing:

```
docker-compose exec redis redis-cli
```

The redis-cli console will be opened and you can try commands like:

```
> AUTH your_redis_server_password
```

```
> PING
```

Type and enter `exit` to exit the console.

____________
### PHPRedisAdmin (Web)

The service can be accessed using your browser at [http://localhost:9987](http://localhost:9987) by default configuration.

____________

### Redis Commander (Web)

The service can be accessed using your browser at [http://localhost:8081](http://localhost:8081) by default configuration.
____________
### Python Redis (Console)

You can execute sample scripts in `docker/python-redis/src` or create one. Here is the example of how to execute existing scripts:

connection test:
```
docker-compose exec python-redis python connection_test.py
```

redis sub:
```
docker-compose exec python-redis python sub.py
```

redis pub:
```
docker-compose exec python-redis python pub.py "first message"
```
____________

## License

[MIT license](https://opensource.org/licenses/MIT)
