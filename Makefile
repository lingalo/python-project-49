install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	python -m games.scripts.brain_games

brain-even:
	python -m games.scripts.brain_even

brain-calc:
	python -m games.scripts.brain_calc