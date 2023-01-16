instal:
	poetry install

brain-games:
	python -m brain_games.scripts.brain_games

brain-even:
	python -m brain_games.scripts.brain_even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

reinstall:
	pip install --user --force-reinstall dist/*.whl