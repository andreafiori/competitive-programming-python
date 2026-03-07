# 🏆 Competitive Programming — Python Solutions

A curated collection of competitive programming problems and solutions in Python, sourced from the most popular platforms. Every solution is adapted with unit tests for easy verification and learning.

## 📋 Requirements

- **Python**: 3.13.3

## 🚀 Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUse
.venv\Scripts\activate.ps1
```


Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUse

| macOS / Linux | `source .venv/bin/activate` |

### 2. Install dependencies

```bash
pip install -e .
pip install pytest
```

---

## 🐳 Docker

Prefer containers? Build and run tests with Docker:

```bash
docker build --target test -t myapp-test .
docker run --rm myapp-test
```


## 🧪 Running Tests

```bash
pytest
```

Or explicitly via the venv Python:

```bash
.venv/bin/python -m pytest
```


## 🧹 Cleaning Up

Remove temporary files and the virtual environment:

```bash
# Clear all __pycache__ directories and compiled files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

# Remove the virtual environment
rm -rf .venv
```

> ⚠️ Note: The cleanup command uses `rm -rf .venv` (not `rm .env`) to remove the virtual environment directory.


## 🌐 Platforms

Solutions are sourced from the following competitive programming platforms:

| Platform | URL |
|---|---|
| CodeChef | [codechef.com](https://www.codechef.com) |
| Codeforces | [codeforces.com](https://codeforces.com) |
| Codility | [codility.com](https://www.codility.com) |
| LeetCode | [leetcode.com](https://www.leetcode.com) |


## 📁 Project Structure

```
.
├── solutions/        # Problem solutions organized by platform
├── tests/            # Unit tests for each solution
├── pyproject.toml    # Project metadata and dependencies
└── Dockerfile        # Docker configuration
```

## 🤝 Contributing

Contributions are welcome! When adding a new solution, please ensure:

1. The solution is placed in the appropriate platform folder.
2. A corresponding unit test is included.
3. All existing tests pass before submitting.

## Resources

* [Leetcode main](https://github.com/doocs/leetcode/tree/main)