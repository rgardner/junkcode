setup:
	pipenv install --dev

format:
	pipenv run black --target-version py37 .
	pipenv run isort --apply

lint:
	pipenv run flake8
	pipenv run mypy

test:
	pipenv run pytest --cov
