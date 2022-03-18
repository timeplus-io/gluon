
build:
	python3 -m pip install --upgrade build
	python3 -m build

install: build
	pip install ./dist/timeplus-0.0.1.tar.gz

test:
	pytest tests/