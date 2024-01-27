
# Andres' Fork
## Before starting
All the sensitive data is stored in .env file in root folder, since this is a test that won't go into production, copy and paste this in your .env
```
DATABASE_USER=root
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=3305
DATABASE_NAME=test_db

MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=test_db
```
## Run with Docker
I decided to dockerize the project because of the possible issues you could have with the database, to setup mysql and fastAPI just run this command with docker

```bash
docker compose -f docker-compose-dev.yml up --build
```

## Run Project (the hard way, at your own risk)
If you don't have docker installed, configure your tables manually, then run:
```bash
cd api

source /venv/bin/activate

pip install -r requirements.txt

uvicorn main:app
```

then change your .env file with the data you need
```
DATABASE_USER={your_user}
DATABASE_PASSWORD={your_password}
DATABASE_HOST={your_db_host} # for example, localhost
DATABASE_PORT={mysql_port} # probably 3306
DATABASE_NAME={your_db}

MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=test_db
```

# Run tests
If you ran the project with docker, then you will need to access the container to run the tests, it can be done using this command:
 ```bash
 docker compose -f docker-compose-dev.yml exec app pytest "" -p no:warnings
 ```

# Run Tests  (without docker)
```bash
cd api

pytest
```
