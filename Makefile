# ------------------------
# GLOBAL COMMANDS
# ------------------------

install:
	npm install

dev:
	npm run dev

build:
	npm run build

# ------------------------
# SCAFFOLDING / INITIALIZATION
# ------------------------

# Initialize a new python project using uv
# Usage: make init-python project_name="my-model" dir="ml"
init-python:
	@if [ -z "$(project_name)" ] || [ -z "$(dir)" ]; then \
		echo "Usage: make init-python project_name=\"my-project\" dir=\"services|ml|experiments\""; \
		exit 1; \
	fi
	@echo "Creating python project $(project_name) in $(dir)/"
	mkdir -p $(dir)/$(project_name) && cd $(dir)/$(project_name) && uv init
	@echo "Done! Navigate to $(dir)/$(project_name) to start coding."

# Initialize a new Node.js workspace (package or app)
# Usage: make init-node dest="apps/my-app"
init-node:
	@if [ -z "$(dest)" ]; then \
		echo "Usage: make init-node dest=\"apps/my-app|packages/my-lib\""; \
		exit 1; \
	fi
	@echo "Creating Node.js project at $(dest)"
	mkdir -p $(dest) && cd $(dest) && npm init -y
	@echo "Done! Remember to update package.json name field."

# ------------------------
# FRONTEND APPS
# ------------------------

notes-ui:
	cd apps/web-quick-notes && npm run dev

# ------------------------
# BACKEND (PYTHON - uv)
# ------------------------

api-notes:
	cd services/api-notes && uv run uvicorn main:app --reload --port 8000

# ------------------------
# CLEANUP
# ------------------------

clean:
	rm -rf node_modules
	rm -rf apps/*/node_modules
	rm -rf packages/*/node_modules
	rm -rf services/*/node_modules
	rm -rf experiments/*/node_modules
	rm -rf ml/*/node_modules

# ------------------------
# HELP
# ------------------------

help:
	@echo "Available commands:"
	@echo "  make install     - Install all dependencies"
	@echo "  make dev         - Run all apps (turbo)"
	@echo "  make init-python project_name=<name> dir=<dir> - Initialize Python project"
	@echo "  make init-node   dest=<path>                   - Initialize Node project"
	@echo "  make notes-ui    - Run notes frontend"
	@echo "  make api-notes   - Run FastAPI backend"
	@echo "  make clean       - Clean node_modules"