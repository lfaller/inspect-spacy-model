# Makefile for spaCy Model Inspector

.PHONY: help install install-dev lint format type-check check test clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install runtime dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

format: ## Format code with black and isort
	@echo "🎨 Formatting code with black..."
	black *.py
	@echo "📦 Sorting imports with isort..."
	isort *.py
	@echo "✅ Formatting complete!"

lint: ## Run flake8 linter
	@echo "🔍 Running flake8..."
	flake8 *.py
	@echo "✅ Linting complete!"

check: format lint ## Run all code quality checks
	@echo "🎉 All checks passed!"

test: ## Run the inspector on default model (basic test)
	@echo "🧪 Testing inspector..."
	python inspect_spacy_model.py --help
	@echo "✅ Basic test complete!"

clean: ## Clean up generated files
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@echo "✅ Cleanup complete!"

# Default target
.DEFAULT_GOAL := help