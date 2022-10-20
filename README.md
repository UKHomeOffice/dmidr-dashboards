# Running the app locally
## Using Docker
```
$ docker compose build reporting-app && docker compose up reporting-app
```

## Without Docker

### 1. Set up virtual env

```
$ python -m venv .venv
```

### 2. Start env

```
$ source .venv/bin/activate
```

### 3. Install requirements

```
$ pip install -r requirements.txt
```

### 4. Run app

```
$ python app/index.py
```
# Running the tests
## Using Docker
```
$ docker compose build test && docker compose up test
```

## Without Docker
### 1. Set up virtual env

```
$ python -m venv .venv
```

### 2. Start env

```
$ source .venv/bin/activate
```

### 3. Install requirements

```
$ pip install -r requirements.txt
```

### 4. Install dash testing
```
$ pip install dash\[testing] pytest
```

### 5. Run tests
```
$ python -m pytest tests
```