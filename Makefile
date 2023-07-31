.PHONY: help
help: ## Command help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Reset project and clean containers
	@docker-compose down -v --remove-orphans | true
	@docker-compose rm -f | true

.PHONY: install
install: ## Install dependencies on container environment
	@docker-compose up -d --build

.PHONY: status
infra-status: ## Show running containers
	@docker ps

.PHONY: install-local
install-local: ## Install dependencies on local environment
	@curl -sSL https://install.python-poetry.org | python3 -
	@poetry env use python3
	@poetry install

.PHONY: run-local-server
run-local-server: ## Run FastAPI server on local environment
	@poetry run uvicorn app.main:app --reload


.PHONY: run-backend-tests
run-backend-tests: ## Run the backend tests
	@docker-compose exec backend poetry run pytest

.PHONY: run-populate-database
run-populate-database: ## Populate the local database with the example from menu_create_payload
	@chmod +x resources/populate_database.sh
	@sh resources/populate_database.sh
