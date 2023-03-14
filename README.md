# Advanced_Django_training
Django using TDD approach, API documentation with Swagger, etc;..


<code>docker-compose run --rm app sh -c "python manage.py collectstatic"</code> <br>

```run``` will start a specific container defined in config, to remove the container once is finished running. Important to avoir having lots of containers running in the background. <br>
```--rm``` removes the container <br>
```sh -c``` passes in a shell command





```docker build .``` once one has the app folder created at root <br>



**How we'll handling Linting** <br>

```docker-compose run --rm app sh -c "flake8"```

<br>

**How we'll test** <br>
```docker-compose run --rm app sh -c "python manage.py test"```
