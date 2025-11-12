install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run

project:
	poetry run project

package-install: build
	poetry run pip install --force-reinstall dist/*.whl
	
clean:
	rm -rf dist/ *.egg-info/
