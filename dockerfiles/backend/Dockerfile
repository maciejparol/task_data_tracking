# STAGE 1
FROM python:3.9.5-alpine3.13 as base

ENV APP_NAME=data_tracking \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6

RUN apk add --no-cache \
	    bash \
	    # Needed to build python packages
        build-base \
        linux-headers \
        postgresql-dev \
        jpeg-dev zlib-dev libjpeg \
        libxml2-dev \
        libxslt-dev \
        libffi-dev

RUN pip install -U pip \
    # https://stackoverflow.com/questions/59441794/error-could-not-build-wheels-for-cryptography-which-use-pep-517-and-cannot-be-i
    && pip install cryptography==2.8 \
    && pip install --no-cache-dir poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock ./$APP_NAME/
ENV CPU_COUNT=1

WORKDIR /$APP_NAME

RUN poetry export --dev --without-hashes -f requirements.txt > /tmp/requirements.txt.lock \
     && poetry run pip install wheel \
     && poetry run pip wheel \
      --no-cache-dir \
      --no-deps \
      --wheel-dir /tmp/wheels \
      -r /tmp/requirements.txt.lock


# STAGE 2
FROM python:3.9.5-alpine3.13

ENV APP_NAME=data_tracking \
    POETRY_VERSION=1.1.6

RUN apk add --no-cache \
	    bash \
        postgresql-dev \
        jpeg-dev zlib-dev libjpeg \
        libxml2-dev \
        libxslt-dev \
        libffi-dev \
        && rm -rf /var/lib/apt/lists/*

COPY config_files/config/entrypoint.sh pyproject.toml poetry.lock ./$APP_NAME/
COPY --from=base /tmp/wheels /tmp/wheels

RUN pip install --upgrade pip \
    && pip install --no-cache /tmp/wheels/* \
    && rm -rf /tmp/wheels

ADD /app/api /$APP_NAME/app/api

WORKDIR /$APP_NAME

ENTRYPOINT ["/data_tracking/entrypoint.sh"]
