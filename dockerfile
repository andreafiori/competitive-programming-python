FROM python:3.13-slim AS builder

WORKDIR /build

COPY pyproject.toml ./
COPY src ./src

RUN pip install --upgrade pip build \
    && python -m build

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY --from=builder /build/dist/*.whl .
COPY requirements.txt .
COPY tests ./tests

RUN pip install *.whl -r requirements.txt

CMD ["pytest", "-q"]