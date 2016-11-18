# GoCrawl

## How to

All these commands can be ran from the current folder.

### Prerequisites

1. Make sure you run Python2.7
2. `easy_install pip`
3. `pip install --upgrade pip`

### Setting up a virtual environment (optional)

1. `pip install virtualenv`
2. `virtualenv env` to create a project-owned environment
3. `source env/bin/activate` to activate it

### Install required modules

`make` or `pip install -r ./requirements.txt`

### Run with options

- `python main.py -h`
- `python main.py -L http://google.fr`
- `python main.py -L http://google.fr --silent` to hide the progress outputs
- `python main.py -L http://google.fr --wait 5` to wait between each requests

### Other

- `make test` to run unit tests
- `make lint` to run linter
