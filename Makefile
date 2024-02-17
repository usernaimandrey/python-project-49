intall:
	poetry install

brain-games:
	poetry run brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl	
