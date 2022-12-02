FROM amd64/alpine:3

RUN mkdir app
COPY app app/
COPY ./requirements.txt ./requirements.txt

ENV PYTHONPATH ./
ENV STAGE production

RUN apk update && \
    apk upgrade && \
    apk add --no-cache python3 && \
    apk add --no-cache git && \
    apk add --no-cache bash
RUN ln -sf python3 /usr/bin/python

RUN python -m venv .venv
RUN /.venv/bin/python -m pip install --upgrade pip
RUN /.venv/bin/pip install -r requirements.txt

RUN adduser -D -u 1001 plotly

USER 1001

ENTRYPOINT [ "/.venv/bin/python" ]
CMD [ "app/index.py"]
