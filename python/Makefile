VERSION = $(shell git describe --tags --abbrev=0 | sed -e "s/v//g")

BIN_NAME ?= gluon
IMAGE_NAME ?= $(BIN_NAME):$(VERSION)
FULLNAME=$(DOCKER_ID_USER)/${IMAGE_NAME}
DOCKER_ID_USER ?= timeplus

.PHONY: build 

init:
	pip install -r requirements_dev.txt

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
	black ./tests

doc:
	VERSION=$(VERSION) pdoc --template-dir ./template  -o ./docs ./timeplus/ --logo "https://s3.us-west-1.amazonaws.com/timeplus.io/Option3_W.png"

test:
	pytest tests/

docker: Dockerfile
	docker build --build-arg VERSION="$(VERSION)" -t $(IMAGE_NAME) .

run:
	docker run -p 8888:8888 -e TIMEPLUS_API_TOKEN=$(TIMEPLUS_API_TOKEN) -e KAFKA_USER=$(KAFKA_USER) -e KAFKA_PASS=$(KAFKA_PASS) $(IMAGE_NAME)

upload:
	twine upload  --config-file ./.pypirc  dist/*

upload_test:
	twine upload  --config-file ./.pypirc   --repository testpypi dist/*