.PHONY: help install envs test format lint clean run

help:  ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install:  ## Install development environment
	uv venv .venv --python 3.10
	uv sync --dev
	pre-commit install
	@echo "Done! Activate with: source .venv/bin/activate"

test:  ## Run tests
	pytest

format:  ## Format code
	black src/ tests/

lint:  ## Check code quality
	flake8 src/ tests/

clean:  ## Remove virtual environment and cache
	rm -rf .venv .pytest_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

run:  ## Run the application
	python main.py
