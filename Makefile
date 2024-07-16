#Make file
install:
	pip install --upgrade &&\
	pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C script.py

test:
	python -m pytest tests/test_*.py

all: lint format test