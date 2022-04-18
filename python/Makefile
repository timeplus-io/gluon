VERSION = $(shell git describe --tags --abbrev=0 | sed -e "s/v//g")

BIN_NAME ?= gluon
IMAGE_NAME ?= $(BIN_NAME):$(VERSION)
FULLNAME=$(DOCKER_ID_USER)/${IMAGE_NAME}
DOCKER_ID_USER ?= timeplus


init:
	pip install -r requirements_dev.txt

build:
	python3 -m pip install --upgrade build
	echo __version__ = \"$(VERSION)\"  \ \ \# noqa: F401 > ./src/timeplus/version.py
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

docker: Dockerfile
	docker build --build-arg VERSION="$(VERSION)" -t $(IMAGE_NAME) .

run:
	docker run -p 8888:8888 -e AUTH0_API_TOKEN=$(AUTH0_API_TOKEN) $(IMAGE_NAME)