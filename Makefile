.DEFAULT_GOAL := help

run: ## Run the application using uvicorn with provided arguments or defaults
	poetry run gunicorn app.main:app --worker-class uvicorn_worker.UvicornWorker -c gunicorn.conf.py

install: ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

migrate-create: ## Create migration
	alembic revision --autogenerate -m $(NAME)

migrate-apply: ## Upgrade migration
	alembic upgrade head

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "commands"
	@echo -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.?## "}; {printf " %-20s %s\n", $$1, $$2}'
