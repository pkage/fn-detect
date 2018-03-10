all: run

install-deps:
	pip install --user -r requirements.txt --verbose

run:
	python3 run.py

build-scss:
	scss scss/main.scss fnd/static/index.css

watch-scss:
	scss --watch scss/main.scss:fnd/static/index.css
