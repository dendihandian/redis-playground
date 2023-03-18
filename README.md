# Redis Playground

## Requirements

- Docker
- Docker-Compose

## Setup

1. Duplicate `.env.example` into `.env` in the same directory. You may want to change the values if needed or leave it.

2. Run of these commands:

    - Redis only:
    ```
    docker-compose up -d redis
    ```

    - Playing with PHPRedisAdmin only:
    ```
    docker-compose up -d redis phpredisadmin
    ```

    - Playing with python redis scripts only:
    ```
    docker-compose up -d redis python-redis
    ```

    - Run all services:
    ```
    docker-compose up -d
    ```