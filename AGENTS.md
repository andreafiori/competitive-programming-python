# [AGENTS.md](http://AGENTS.md)

This document defines the roles, workflows, and guidelines for **AI coding agents** and **human reviewers** collaborating on this Python project. The project contains:

- `src/`: Solutions for LeetCode, Project Euler, and Codility problems.
- `tests/`: Pytest-based unit tests for all scripts.

---

## 🎯 Objectives

1. **Complete Scripts**: Fill gaps in existing solutions (e.g., unfinished algorithms, edge cases).
2. **Build Unit Tests**: Generate comprehensive pytest cases for all functions/modules.
3. **Manual Review**: Validate agent-generated code for correctness, efficiency, and style.
4. **Integration**: Ensure all scripts and tests work cohesively.

---

## 🤖 Agent Roles

### 1. **Script Completion Agent**

**Responsibilities**:

- Analyze incomplete scripts in `src/` (e.g., LeetCode `two_sum.py`, Project Euler `problem_1.py`).
- Implement missing logic, optimize algorithms, and handle edge cases.
- Follow Python best practices (PEP 8, type hints, docstrings).
- Flag ambiguous requirements for human review.

**Workflow**:

1. Scan `src/` for TODO comments or incomplete functions.
2. Research problem requirements (e.g., LeetCode problem statement).
3. Propose solutions with explanations.
4. Submit PR with changes to `src/`.

**Tools**:

- Python 3.11+
- `pylint`, `mypy` for static analysis.
- Problem-specific libraries (e.g., `math` for Project Euler).

---

### 2. **Unit Test Agent**

**Responsibilities**:

- Generate pytest cases for all functions in `src/`.
- Cover edge cases (empty inputs, large numbers, invalid types).
- Mock external dependencies (e.g., API calls in Codility problems).
- Ensure 100% coverage for critical logic.

**Workflow**:

1. For each script in `src/`, create a corresponding test file in `tests/` (e.g., `tests/test_two_sum.py`).
2. Use `pytest` fixtures for reusable test data.
3. Validate tests pass locally before submission.
4. Submit PR with new/updated test files.

**Tools**:

- `pytest` (with `pytest-cov` for coverage).
- `hypothesis` for property-based testing.

---

### 3. **Integration Agent**

**Responsibilities**:

- Verify all scripts in `src/` are importable and functional.
- Ensure tests in `tests/` run without errors.
- Resolve dependency conflicts (e.g., Python version mismatches).
- Update `requirements.txt` or `pyproject.toml` as needed.

**Workflow**:

1. Run `pytest tests/` to validate all tests.
2. Check for circular imports or missing dependencies.
3. Submit PR with integration fixes.

**Tools**:

- `pip`, `poetry`, or `conda` for dependency management.
- `tox` for multi-environment testing.

---

## 👤 Human Reviewer Roles

### 1. **Manual Corrector**

**Responsibilities**:

- Review agent-generated code for:
  - **Correctness**: Verify logic against problem statements.
  - **Efficiency**: Check time/space complexity (e.g., O(n) vs. O(n²)).
  - **Style**: Enforce PEP 8, consistent naming, and docstrings.
- Merge or request changes to agent PRs.

**Guidelines**:

- Prioritize clarity over cleverness.
- Add comments for non-obvious optimizations.
- Reject PRs with untested edge cases.

---

### 2. **Test Validator**

**Responsibilities**:

- Run agent-generated tests locally.
- Verify test cases cover all branches of the code.
- Add manual test cases for complex scenarios.

**Guidelines**:

- Use `pytest -v` to inspect test output.
- Require tests for both happy paths and error cases.

---

## 🔄 Collaboration Workflow

- **Agent Action**:
  - Agent opens a PR with changes to `src/` or `tests/`.
  - PR description includes:
    - Problem addressed (e.g., "Completed LeetCode #2: Add Two Numbers").
    - Changes made (e.g., "Added `add_two_numbers()` function").
    - Testing instructions (e.g., "Run `pytest tests/test_add_two_numbers.py`").
- **Human Review**:
  - Reviewer checks for correctness, efficiency, and style.
  - Requests changes via PR comments or approves.
- **Integration**:
  - After approval, the Integration Agent ensures no regressions.
  - All tests must pass in CI (e.g., GitHub Actions).

---

## 📁 Project Structure

├── src/
│   ├── leetcode/
│   │   ├── two_sum.py
│   │   └── ...
│   ├── project_euler/
│   │   ├── problem_1.py
│   │   └── ...
│   └── codility/
│       ├── binary_gap.py
│       └── ...
├── tests/
│   ├── leetcode/
│   │   ├── test_two_sum.py
│   │   └── ...
│   ├── project_euler/
│   │   ├── test_problem_1.py
│   │   └── ...
│   └── codility/
│       ├── test_binary_gap.py
│       └── ...
├── AGENTS.md
├── requirements.txt
└── pyproject.toml

---

## 🛠️ Setup Instructions

### For Agents

- Clone the repository.
- Install dependencies:

  ```bash
   pip install -r requirements.txt
  ```

- Run tests:

  ```bash
   pytest tests/
  ```

### For Reviewers

- Fork the repository.
- Create a branch for reviews (e.g., `review/leetcode-two-sum`).
- Use `pre-commit` hooks for linting:

  ```bash
   pre-commit install
  ```

---

## 📜 Guidelines

### Coding Standards

- **Naming**: Use `snake_case` for functions/variables, `PascalCase` for classes.
- **Docstrings**: Follow [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
- **Type Hints**: Annotate all function signatures (e.g., `def add(a: int, b: int) -> int:`).

### Testing Standards

- **Naming**: Prefix test functions with `test_` (e.g., `test_add_two_numbers`).
- **Organization**: Mirror `src/` structure in `tests/`.
- **Coverage**: Aim for 100% branch coverage for critical logic.

### Problem-Specific Notes

- **LeetCode**: Include the problem URL in docstrings.
- **Project Euler**: Add mathematical explanations in comments.
- **Codility**: Note time/space complexity constraints.

---

## 🚀 Example Workflow

### Scenario: Completing `src/leetcode/two_sum.py`

- **Script Completion Agent**
  - Implements `two_sum(nums, target)` function.
  - Submits PR with:

    ```python
    def two_sum(nums: list[int], target: int) -> list[int]:
        """
        LeetCode Problem 1: Two Sum
        https://leetcode.com/problems/two-sum/
        Returns indices of the two numbers that add up to the target.
        """
        # Implementation here
        pass
    ```

- **Unit Test Agent**
  - Creates `tests/leetcode/test_two_sum.py`:
- **Manual Corrector**
  - Reviews PR, suggests optimizing with a hashmap.
  - Approves after changes.
- **Integration Agent**:
  - Confirms all tests pass.

---

## 📌 Notes

- Use **GitHub Issues** to track problems needing attention.
- Label PRs with `agent:script`, `agent:test`, or `review:manual`.
- Update this file as workflows evolve.