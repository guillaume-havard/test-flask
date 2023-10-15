help:     ## Show this help.
	@grep -E -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":[^:]*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

format: ## Format python code.
	poetry run black `git ls-files '*.py'`
	poetry run isort `git ls-files '*.py'`
.PHONY: format

linting: ## Linting python code.
	poetry run pylint `git ls-files '*.py'`
.PHONY: linting

install: ## Install python dependancies.
	poetry install
.PHONY: install

update_dependancies: ## Update pythondependancies, may broke code.
	poetry update
.PHONY: update_dependancies