# CLAUDE.md

This file provide guidance to Claude Code when working with code in this repository.

## Project Overview

This is a Python 3.10+ project containing Python Solutions for LeetCode Problems.

## Project Structure

```text
.
├── awesome_python_leetcode/    # Main package for LeetCode solutions
├── docs/                       # Project documentation and assets
├── tests/                      # Pytest tests
├── .github/
│   ├── workflows/              # CI/CD pipeline definitions
│   ├── ISSUE_TEMPLATE/         # Github Issue Templates
│   └── PULL_REQUEST_TEMPLATE/  # Github Pull Request Templates
├── pyproject.toml
├── tox.ini
├── CLAUDE.md
└── GEMINI.md
```

## Commands

- Install dependencies: `uv sync`
- Run tests: `uv run pytest tests`
- Lint code: `uv run ruff check awesome_python_leetcode tests`
- Format code: `uv run ruff format awesome_python_leetcode tests`
- Lint markdown: `uv run rumdl check README.md CLAUDE.md GEMINI.md`
- Format markdown: `uv run rumdl fmt README.md CLAUDE.md GEMINI.md`
- Type check: `uv run ty check awesome_python_leetcode tests`
- Security scan: `uv run bandit -r awesome_python_leetcode tests`
- Dependency check: `uv run deptry awesome_python_leetcode tests`
- Run all checks: `uv run tox`

## CI/CD Pipelines

- [Linting](.github/workflows/lint.yml)
- [Testing](.github/workflows/test.yml)
- [Releasing](.github/workflows/release.yml)

## Templates

- [GitHub Issue Templates](.github/ISSUE_TEMPLATE/)
- [GitHub Pull Request Templates](.github/PULL_REQUEST_TEMPLATE/)

## Coding Standards

- **Type Hints:** All functions and methods MUST include complete type hints for arguments and return values.
- **Docstrings:** All functions and methods MUST include `Google Python Style Guide` docstring format.
- **Modern Python**: ALWAYS use modern Python features and best practices.
- **Testing**: All solutions should have corresponding tests in the `tests/` directory.

## Resources

### Core Stack

- [Python 3.10+](https://docs.python.org/3.10/)
- [uv](https://docs.astral.sh/uv/)

### Code Quality & Testing

- [bandit](https://bandit.readthedocs.io/en/latest/)
- [deptry](https://deptry.com/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [pytest](https://docs.pytest.org/en/stable/)
- [ruff](https://docs.astral.sh/ruff/)
- [rumdl](https://rumdl.dev/)
- [tox-uv](https://github.com/tox-dev/tox-uv)
- [ty](https://docs.astral.sh/ty/)
