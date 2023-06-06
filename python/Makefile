VERSION = $(shell git describe --tags --abbrev=0 | sed -e "s/v//g")

.PHONY: build test

venv:
	python3 -m venv .venv

init:
	pip install -r requirements.txt
	pip install -r test-requirements.txt

build:
	python3 -m pip install --upgrade build
	echo __version__ = \"$(VERSION)\"  \ \ \# noqa: F401 > ./timeplus/version.py
	python3 -m build

install: build
	pip install ./dist/timeplus-$(VERSION).tar.gz

lint:
	flake8 ./timeplus --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ./timeplus --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black ./timeplus

doc:
	VERSION=$(VERSION) pdoc --template-dir ./template  -o ./docs ./timeplus/ --logo "https://s3.us-west-1.amazonaws.com/timeplus.io/Option3_W.png"

test:
	pytest ./test

upload:
	twine upload  --config-file ./.pypirc  dist/*

upload_test:
	twine upload  --config-file ./.pypirc   --repository testpypi dist/*