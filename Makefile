.PHONY: all static format black isort check test
all: static test
static: format check
format: black isort

black:
	poetry run black .

isort:
	poetry run isort python

check:
	poetry run pre-commit run --all-files

test:
	cd app/api && poetry run pytest --cov=.
