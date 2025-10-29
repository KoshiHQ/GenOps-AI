# GenOps AI Development Makefile
# Common development tasks for contributors

.PHONY: help install dev-install test test-verbose lint format type-check clean build docs serve-docs

# Default target
help: ## Show this help message
	@echo "GenOps AI Development Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

# Installation
install: ## Install GenOps AI for production use
	pip install .

dev-install: ## Install GenOps AI for development (editable)
	pip install -e ".[dev,openai,anthropic]"
	pip install pre-commit
	pre-commit install
	pre-commit install --hook-type commit-msg
	@echo "✅ Development environment ready with pre-commit hooks!"

# Testing
test: ## Run tests
	pytest tests/ -v --tb=short

test-verbose: ## Run tests with detailed output
	pytest tests/ -v --tb=long --show-capture=all

test-coverage: ## Run tests with coverage report
	pytest tests/ --cov=src/genops --cov-report=html --cov-report=term
	@echo "📊 Coverage report generated in htmlcov/"

test-property: ## Run property-based tests with Hypothesis
	pytest tests/property_tests/ -v --hypothesis-show-statistics
	@echo "🔍 Property-based tests completed with statistics"

test-mutation: ## Run mutation testing to verify test quality
	mutmut run --paths-to-mutate=src/genops
	mutmut results
	mutmut html
	@echo "🧬 Mutation testing completed - see htmlcov/mutmut_index.html"

test-benchmark: ## Run performance benchmarks
	pytest benchmarks/ --benchmark-only --benchmark-json=benchmark.json
	@echo "⚡ Performance benchmarks completed"

# Code Quality
lint: ## Run linting (ruff check)
	ruff check src/ tests/ examples/

lint-fix: ## Run linting with auto-fixes
	ruff check --fix src/ tests/ examples/

format: ## Format code (ruff format)
	ruff format src/ tests/ examples/

type-check: ## Run type checking (mypy)
	mypy src/genops/

# Combined quality check
check: lint type-check test ## Run all code quality checks

# Development helpers
clean: ## Clean build artifacts and cache
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	@echo "🧹 Cleaned build artifacts"

build: clean ## Build package for distribution
	python -m build
	@echo "📦 Package built in dist/"

# Examples and demos
demo: ## Run basic usage demo
	python examples/basic_usage.py

demo-scenarios: ## Run all governance scenarios
	@echo "🚀 Running governance scenarios..."
	python examples/governance_scenarios/budget_enforcement.py
	python examples/governance_scenarios/content_filtering.py
	python examples/governance_scenarios/customer_attribution.py

# Documentation
docs: ## Generate API documentation (requires Sphinx)
	@if command -v sphinx-build >/dev/null 2>&1; then \
		sphinx-build -b html docs/ docs/_build/html; \
		echo "📖 Documentation built in docs/_build/html/"; \
	else \
		echo "❌ Sphinx not installed. Run: pip install sphinx"; \
	fi

serve-docs: docs ## Build and serve documentation locally
	@if command -v python -m http.server >/dev/null 2>&1; then \
		cd docs/_build/html && python -m http.server 8000; \
	else \
		echo "📖 Open docs/_build/html/index.html in your browser"; \
	fi

# Utility commands
validate-env: ## Validate development environment
	@echo "🔍 Validating development environment..."
	@python -c "import genops; print('✅ GenOps AI imports successfully')"
	@python -c "import pytest; print('✅ pytest available')"
	@python -c "import ruff; print('✅ ruff available')" 2>/dev/null || echo "⚠️  ruff not found - run: pip install ruff"
	@python -c "import mypy; print('✅ mypy available')" 2>/dev/null || echo "⚠️  mypy not found - run: pip install mypy"
	@echo "✅ Environment validation complete"

version: ## Show GenOps AI version
	@python -c "import genops; print(f'GenOps AI v{genops.__version__}')"

# Quick development workflow
dev: dev-install check ## Full development setup and validation
	@echo "🎉 Ready for development!"

# Release helpers (for maintainers)
bump-version: ## Bump version (requires version argument: make bump-version version=0.2.0)
	@if [ -z "$(version)" ]; then \
		echo "❌ Please specify version: make bump-version version=0.2.0"; \
		exit 1; \
	fi
	sed -i.bak 's/__version__ = ".*"/__version__ = "$(version)"/' src/genops/__init__.py
	rm src/genops/__init__.py.bak
	@echo "✅ Version bumped to $(version)"

publish-test: build ## Publish to Test PyPI
	twine upload --repository testpypi dist/*

publish: build ## Publish to PyPI (requires authentication)
	twine upload dist/*

# Git helpers
pre-commit-check: ## Run pre-commit hooks manually
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hook versions
	pre-commit autoupdate

pre-commit: check ## Run pre-commit checks (legacy)
	@echo "🔍 Pre-commit validation..."
	@if git diff --cached --name-only | grep -E '\.(py)$$' >/dev/null; then \
		echo "🔧 Running checks on staged files..."; \
		git diff --cached --name-only | grep -E '\.(py)$$' | xargs ruff check; \
		git diff --cached --name-only | grep -E '\.(py)$$' | xargs ruff format --check; \
	fi
	@echo "✅ Pre-commit checks passed"

# ADR (Architecture Decision Records) management
adr-new: ## Create new ADR (usage: make adr-new title="Decision Title")
	@if [ -z "$(title)" ]; then \
		echo "❌ Please specify title: make adr-new title='Decision Title'"; \
		exit 1; \
	fi
	@NEXT_NUM=$$(ls docs/adr/[0-9]*.md 2>/dev/null | wc -l | xargs expr 1 +); \
	PADDED_NUM=$$(printf "%04d" $$NEXT_NUM); \
	FILENAME="docs/adr/$$PADDED_NUM-$$(echo "$(title)" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$$//g').md"; \
	cp docs/adr/template.md "$$FILENAME"; \
	sed -i.bak "s/ADR-XXXX/ADR-$$PADDED_NUM/g" "$$FILENAME"; \
	sed -i.bak "s/\\[Title\\]/$(title)/g" "$$FILENAME"; \
	sed -i.bak "s/YYYY-MM-DD/$$(date +%Y-%m-%d)/g" "$$FILENAME"; \
	rm "$$FILENAME.bak"; \
	echo "📝 Created new ADR: $$FILENAME"

adr-list: ## List all ADRs
	@echo "📚 Architecture Decision Records:"
	@echo ""
	@for file in docs/adr/[0-9]*.md; do \
		if [ -f "$$file" ]; then \
			NUM=$$(basename "$$file" | cut -d'-' -f1); \
			TITLE=$$(grep "^# ADR-" "$$file" | sed 's/^# ADR-[0-9]*: //'); \
			STATUS=$$(grep -A1 "^## Status" "$$file" | tail -1 | sed 's/\\[//g' | sed 's/\\].*//g'); \
			printf "  %s: %s [%s]\\n" "$$NUM" "$$TITLE" "$$STATUS"; \
		fi \
	done
	@echo ""