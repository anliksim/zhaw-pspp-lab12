.PHONY: all llinit test

all: init test

init:
	pip install -r requirements.txt

test:
	nosetests tests
