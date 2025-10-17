# Repository Guidelines

## Project Structure & Module Organization
Follow a predictable tree so agents remain discoverable. Place runtime code in `src/`, grouping automation agents under `src/agents/` and shared utilities under `src/lib/`. Keep integration shims or schedulers in `src/runners/`. Store reusable configuration in `config/` and secrets only via environment variables or the secret manager documented in `config/README.md` when it is added. Tests live in `tests/`, mirroring the package layout (`tests/agents/test_<agent>.py`). Static assets that agents rely on (fixtures, templates) belong in `assets/` with subfolders named after the consuming module.

## Build, Test, and Development Commands
Create a virtual environment (`python -m venv .venv && source .venv/bin/activate`) before installing dependencies. Install project requirements with `pip install -r requirements.txt`. Use `pytest` for the full test suite and `pytest tests/agents/test_example.py::test_case` when iterating on a single case. Run `ruff check src tests` to lint and `black src tests` to format; both commands should exit cleanly before opening a pull request. Add a `make` target when introducing new workflows so teammates can call them consistently (`make ingest-sample-data`, `make regenerate-schema`, etc.).

## Coding Style & Naming Conventions
Stick to Python 3.11 syntax. Format code with Black’s default 88-character line width and lint with Ruff using the `ruff.toml` profile checked into the repo. Name modules and packages with `snake_case`; reserve `CamelCase` for classes and `SCREAMING_SNAKE_CASE` for constants. Functions and variables should be concise, action-oriented, and aligned with the agent’s responsibility (`load_session_state`, `enqueue_follow_up`). Document non-obvious behavior with docstrings that explain “why” rather than “what”.

## Testing Guidelines
Write unit tests alongside every new agent, mocking external services with `pytest` fixtures under `tests/fixtures/`. Ensure functional flows are covered by scenario tests marked with `@pytest.mark.integration`; they may hit sandboxed endpoints but must be idempotent. Maintain at least 85% statement coverage measured by `pytest --cov=src --cov-report=term-missing`. Name tests descriptively (`test_scheduler_retries_after_network_error`). Failing tests should block merges.

## Commit & Pull Request Guidelines
Use Conventional Commit headers (`feat: add timeline agent`, `fix: harden retry loop`). Craft commits around a single cohesive change and include migration or config updates in the same commit. Pull requests need a summary, bullet list of changes, linked issue (`Closes #123`), and any relevant logs or screenshots. Request review from another agent maintainer and wait for green CI before merging; use squash merges to keep history linear.
