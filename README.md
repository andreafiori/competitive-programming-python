# Competitive Programming Problems and Solutions in Python

![CI](https://img.shields.io/badge/tests-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)
![TDD](https://img.shields.io/badge/methodology-TDD-purple)

A collection of competitive programming problems and their Python solutions from popular online coding platforms.

Each solution has been adapted to support automated unit testing with **pytest**, making it easier to verify correctness and experiment with alternative implementations.

## Supported Platforms

* [CodeChef](https://www.codechef.com)
* [Codeforces](https://codeforces.com)
* [Codility](https://www.codility.com)
* [LeetCode](https://leetcode.com)
* [Project Euler](https://projecteuler.net)

## Requirements

* Python 3.13.3 or later

## Getting Started

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the tests

Run all tests with:

```bash
pytest
```

Alternatively:

```bash
python -m pytest
```

Code coverage HTML report:

```bash
python -m pytest --cov=src --cov-report=html tests/
```

## Docker

You can also run the test suite using Docker:

```bash
docker build --target test -t PythonCompetitiveprogramming-test .
docker run --rm PythonCompetitiveprogramming-test
```

## Cleaning Python Cache

To remove all `__pycache__` directories and compiled Python files:

```bash
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```
