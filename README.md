# Python competitive programming problems and solutions

Python version: 3.13.3

Competitive programming problems and solution in Python from the most popular websites.

## Create virtual env

python -m venv .venv

Activate:

Windows:
.venv\Scripts\activate

MacOS/Linux
source .venv/bin/activate

## Install dependencies

pip install -e .
pip install pytest

## Docker support

Alternatively, you can use Docker:

docker build --target test -t myapp-test .
docker run --rm myapp-test

## Run tests

pytest

or

.venv/bin/python -m pytest

## Clear pycache dirs

find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
