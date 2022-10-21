include .env
export

run:
	./venv/bin/python3 impact/manage.py runserver

install:
	python3 -m venv venv
	./venv/bin/pip install pipenv
	./venv/bin/pipenv install -d

shell:
	./venv/bin/python3 impact/manage.py shell

migrate:
	./venv/bin/python3 impact/manage.py migrate

migrations:
	./venv/bin/python3 impact/manage.py makemigrations entreprises public reglementations users

createsuperuser:
	./venv/bin/python3 impact/manage.py createsuperuser

pytest:
	./venv/bin/pytest

test:
	./venv/bin/python3 impact/manage.py test public
