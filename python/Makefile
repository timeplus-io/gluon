VERSION = $(shell git describe --tags --abbrev=0 | sed -e "s/v//g")


init:
	pip install -r requirements_dev.txt

build:
	python3 -m pip install --upgrade build
	echo __version__ = \"$(VERSION)\"  \# noqa: F401 > ./src/timeplus/version.py
	python3 -m build

install: build
	pip install ./dist/timeplus-$(VERSION).tar.gz

lint:
	flake8 ./src --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ./src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black ./src
	black ./tests

test:
	pytest tests/