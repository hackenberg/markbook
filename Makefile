.PHONY: all build clean clean-pyc cov flake8 package test

all: cov flake8

build:
	python setup.py build

clean: clean-pyc
	rm -rf *.egg-info/ build/ dist/ tmp/ .coverage

clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "__pycache__" -delete

cov:
	python -m coverage run --source markbook setup.py test --pytest-args=tests
	python -m coverage report -m

flake8:
	-@python setup.py flake8
	-@flake8 main.py setup.py
	-@flake8 tests

init:
	python main.py db init
	python main.py db migrate
	python main.py db upgrade

package:
	mkdir -p dist
	cp PKGBUILD dist/PKGBUILD
	cd dist && makepkg -f

test:
	python setup.py test --pytest-args=tests
