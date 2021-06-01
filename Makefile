install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=fastapi_task_manager --cov-report html

lint:
	poetry run flake8 fastapi_task_manager

start:
	poetry run python fastapi_task_manager

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
