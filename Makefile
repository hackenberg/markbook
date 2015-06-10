.PHONY: all build clean clean-pyc coverage flake8 package test

all: test coverage flake8

build:
	python setup.py build

clean: clean-pyc
	rm -rf build/ dist/ *.egg-info/ .coverage

clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "__pycache__" -delete

coverage:
	@python -m coverage report -m

flake8:
	-@python setup.py flake8
	-@flake8 main.py setup.py
	-@flake8 tests

init:
	python main.py --init

package:
	python setup.py sdist
	cp PKGBUILD dist/PKGBUILD
	cd dist && makepkg -g >> PKGBUILD && makepkg -f

test:
	python -m coverage run --source markbook setup.py test --pytest-args=tests
