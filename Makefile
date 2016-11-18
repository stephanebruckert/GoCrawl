init:
	pip install -r requirements.txt

test:
	nosetests tests

lint:
	flake8 **/*.py
