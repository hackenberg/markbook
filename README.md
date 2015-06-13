# markbook

[![Build Status](https://travis-ci.org/hackenberg/markbook.svg?branch=master)](https://travis-ci.org/hackenberg/markbook)

## Quickstart

### Set Environment Variables

```sh
$ export MARKBOOK_SETTINGS="ProductionConfig"
```

or

```sh
$ export MARKBOOK_SETTINGS="DevelopmentConfig"
```

### Create Database

```sh
$ python main.py db init
$ python main.py db migrate
$ python main.py db upgrade
```

### Run

```sh
$ python main.py notebook
```

or

```sh
$ python main.py on
```

### Testing

Without coverage:

```sh
$ python setup.py test --pytest-args=tests
```

With coverage:

```sh
$ python -m coverage run --source markbook setup.py test --pytest-args=tests
```
