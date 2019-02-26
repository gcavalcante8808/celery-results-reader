## Requirements

Docker and docker-compose installed and working.

## How to Use

Clone the repository, create an .env file with the following env vars:

 * RESULT_BACKEND_URL
 * BROKER_URL

After that, bring the project up by using the command `docker-compose up -d`; you can now verify an result by viewing the url `localhost:5000/results/task_id`.

If something is not quite right, you can see the logs of the application through the command `docker-compose logs app`.

## How to Develop

An `docker-compose.dev.yml` is present in the root dir, you can use in the startup through the following command:

```bash
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

The `src` folder will be mounted as a bind volume in the `/usr/src/`folder inside the container.


## How to execute Tests

You can run the tests through the following commands:

```bash
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
    docker-compose exec app python -m pytest tests.py
```

## Caveats


Only tested against Celery 3 and Redis as Result Backend.

## RoadMap

 * Test against other result backends;
 * Use Tox to run tests;
 * User Interface;
 