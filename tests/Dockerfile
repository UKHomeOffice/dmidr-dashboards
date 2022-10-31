FROM amd64/alpine:3

COPY app app
COPY tests tests

COPY ./requirements.txt requirements.txt

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 && \
    apk add --no-cache git && \
    apk add --no-cache bash
RUN ln -sf python3 /usr/bin/python

RUN python -m venv .venv
RUN /.venv/bin/python -m pip install --upgrade pip
RUN /.venv/bin/pip install -r requirements.txt
RUN /.venv/bin/pip install dash\[testing]
RUN /.venv/bin/pip install pytest

ENTRYPOINT [ "/.venv/bin/pytest" ]
CMD [ "tests" ]