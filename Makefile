install:
	poetry install --without dev


# development

dev: install-dev
	poetry run python task_manager/manage.py runserver

install-dev:
	poetry install --with dev

lint: install-dev
	poetry run flake8 .

test: install-dev
	poetry run pytest

test-coverage: install-dev
	poetry run pytest --cov=task_manager --cov-report xml
