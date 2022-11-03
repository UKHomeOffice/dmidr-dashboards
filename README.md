# Deployment Process

## Pushing a new version of the Docker image

1. Create a pull request with your changes.
1. Add a label to the pull request, one of major, minor or patch, depending on your changes.
The label will determine how the version number is incremented, following `major.minor.patch`.
The pipeline will fail without this label and a new image will not be pushed to the repository.
1. After the tests have passed, merge the pull request.
1. A [Github actions workflow][push_image_workflow] will rerun the tests.
If they pass, it will build the docker image.
It will then push the image to the [quay repository][quay_repository], tagged with the new version number and create a matching tag in the github repository.
1. The creation of a tag in the github repository will trigger the [drone pipeline][drone_pipeline] to run and deploy the image to the kubernetes cluster.


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
[drone_pipeline]: https://drone-gh.acp.homeoffice.gov.uk/UKHomeOffice/hocs-mi-dashboards