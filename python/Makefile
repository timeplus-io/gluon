
init:
	pip install -r requirements_dev.txt

build:
	python3 -m pip install --upgrade build
	python3 -m build

install: build
	pip install ./dist/timeplus-0.0.1.tar.gz

lint:
	flake8 ./src --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ./src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black ./src

test:
	pytest tests/