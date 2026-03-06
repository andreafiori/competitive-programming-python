# Competitive programming problems and solutions in Python

Competitive programming problems and solution implementations in Python from the most popular websites.
All scripts and solutions are modified to write unit tests.

## Requirements

Python version: 3.13.3

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

## Clear the development environment

If you need to clear all temp __pycache__ directories:

### Clear pycache directories

find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

### Remove venv

rm .env

## Platforms

* [Codechef](https://www.codechef.com)
* [Codeforces](https://codeforces.com)
* [Codility](https://www.codility.com)
* [Leetcode](https://www.leetcode.com)
