.PHONY: all build clean clean-pyc flake8 package test

all: test

build:
	python setup.py build

clean: clean-pyc
	rm -rf build/ dist/ *.egg-info/

clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "__pycache__" -delete

flake8:
	@python setup.py flake8

init:
	python main.py --init

package:
	python setup.py sdist

test:
	@python -m unittest discover tests
