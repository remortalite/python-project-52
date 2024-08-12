install:
	poetry install --without dev


# development

build:
	./build.sh

dev: install-dev
	poetry run python manage.py runserver

install-dev:
	poetry install --with dev

lint: install-dev
	poetry run flake8 .

test: install-dev
	poetry run python manage.py test
