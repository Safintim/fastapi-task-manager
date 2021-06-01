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

formatter:
	poetry run autopep8 --recursive --in-place --aggressive --aggressive .

init-db:
	poetry run python -m fastapi_task_manager.tables

.PHONY: install test lint selfcheck check build formatter
