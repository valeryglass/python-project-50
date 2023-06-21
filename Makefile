# Makefile
install:
	poetry install

gendiff-help:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-force:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games
