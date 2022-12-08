FROM python:3.10-bullseye

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION 1.2.2

WORKDIR /tmp

RUN pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

WORKDIR /backend

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "5000", "--debugger", "--with-threads", "--reload" ]
