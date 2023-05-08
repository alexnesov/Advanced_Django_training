# Advanced_Django_training
Django using a TDD approach, using containerization of it for agility, API documentation with Swagger, Github Actions for automated testing, etc...

# Apps

- ```app/``` - Django project 
- ```app/core/``` - Code shared between multiple apps
- ```app/user/``` - User related code (User registration & auth tokens)
- ```app/recipe/``` - Recipe related code (Handling and updating ingrediants and tags and managing tags)


![docker_compose_setup](docker_compose_setup.png)


<code>docker-compose run --rm app sh -c "python manage.py collectstatic"</code> <br>

```run``` will start a specific container defined in config, to remove the container once is finished running. Important to avoir having lots of containers running in the background. <br>
```--rm``` removes the container <br>
```sh -c``` passes in a shell command

## Init project

```docker-compose run --rm app sh -c "django-admin startproject app .```

## Start services

```docker-compose up``` <br>
```docker build .``` once one has the app folder created at root <br>

<br>

**How we'll test** <br>
```docker-compose run --rm app sh -c "python manage.py test"```
<br>


**Django installation from within docker**<br>
```docker-compose run --rm app sh -c "django-admin startproject app ."```
<br>


**Run project with Docker Compose**<br>
```docker-compose up```
<br>

### Other commands:

**Stop all the containers** <br>
```docker stop $(docker ps -a -q)```

<br>

**Remove all the containers**<br>
```docker rm $(docker ps -a -q)```

<br>

# Creating a new Django app (example):

**Creating core app:** <br>
```docker-compose run --rm app sh -c "python manage.py startapp core"```

# DB Migration:

Init:

```docker-compose run --rm app sh -c "python manage.py makemigrations"```


# Why using Mocking ?

- Avoid relying on external services!! (we dont' have necessarily control over these)
    - Ex: sendin email func, but we don't want to actually send an email
- Speeding up tests (for example bypass sleep funcs)

<br>

# What is "psycopg2" (important)

Package that you need in order for Django to connect to our database. It's the most popular PostgreSQL adaptor for Python. Supported by Django officially.


- ```psycopg2-binary```: ok for dev, but not for prod
- ```psycopg2```: compiled from source, compiled for the OS your running on.Better for reliability and perf.

**Dependencies**:
- C compiler
- python3-dev
- libq-dev
<br>

**Equivalent packages for Alpine**
<br>
- postgresql-client
- buildbase
- postgresql-dev
- musldev


# Check directly of DB works:

```docker-compose run --rm app sh -c "python manage.py wait_for_db"```


# First migration

Not working: ```docker-compose run --rm app sh -c "python manage.py makemigrations"```
<br>

Working: ```docker-compose run app sh -c "python manage.py makemigrations core"```

<br>

```docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"```


# Create superuser


```docker-compose run --rm app sh -c "python manage.py createsuperuser"```