install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=/home/pavel/python-project-50 --cov-report json

lint:
	poetry run flake8

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build

publish:
	poetry publish --dry-run

package-install:
	 python3 -m pip install --user --force-reinstall dist/*.whl
