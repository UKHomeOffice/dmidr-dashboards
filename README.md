# Deployment Process

## Pushing a new version of the Docker image

1. Create a pull request with your changes, and ensure you have merged the main branch into your branch.
1. Add a label to the pull request, one of major, minor or patch, depending on your changes.
The label will determine how the version number is incremented, following `major.minor.patch`.
A new image will not be pushed to the repository without this label.
1. After the tests have passed, merge the pull request.
1. A [Github actions workflow][push_image_workflow] will rerun the tests.
Then if they pass, it will build the docker image from the code in the pull request.
It will then push the image to the [quay repository][quay_repository], tagged with the new version number.

# Local Develpoment
## Deploying the app
### With Docker
```
$ docker compose build reporting-app && docker compose up reporting-app
```

### Without Docker

1. Set up virtual env

```
$ python -m venv .venv
```

2. Start env

```
$ source .venv/bin/activate
```

3. Install requirements

```
$ pip install -r requirements.txt
```

4. Run app

```
$ PYTHONPATH=./ python app/index.py
```
## Running the tests
### Using Docker
```
$ docker compose build test && docker compose up test
```

### Without Docker
1. Set up virtual env

```
$ python -m venv .venv
```

2. Start env

```
$ source .venv/bin/activate
```

3. Install requirements

```
$ pip install -r requirements.txt
```

4. Install dash testing
```
$ pip install dash\[testing] pytest
```

5. Run tests
```
$ python -m pytest tests
```

[quay_repository]: https://quay.io/repository/ukhomeofficedigital/hocs-mi-dashboards?tab=tags&tag=latest
[push_image_workflow]: https://github.com/UKHomeOffice/hocs-mi-dashboards/actions/workflows/docker-push.yml