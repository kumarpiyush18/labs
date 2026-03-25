# My Labs 
Welcome to my personal !!

## 🏗️ Architecture & Directory Structure
This repository uses [Turborepo](https://turbo.build/) to manage build pipelines and Node.js workspaces. Python projects are managed using `uv`.

- **`apps/`**: Frontend web applications (Next.js, Vite, React, etc.).
- **`services/`**: Backend APIs and microservices (FastAPI, Node.js, etc.).
- **`packages/`**: Shared libraries, UI components, and utility functions used across `apps/` and `services/`.
- **`dsa/`**: Data structures, algorithms, and technical interview preparations.
- **`ml/`**: Machine learning models, data exploration, and AI pipelines.
- **`experiments/`**: Scratchpad for quick proof-of-concepts and tech learning.

## 🚀 How to Use

### Global Commands
Run these from the root directory:
- `make install`: Installs global Node.js dependencies across apps/packages.
- `make dev`: Runs the turborepo development script for all workspaces.
- `make build`: Builds all turborepo workspaces.
- `make clean`: Cleans up `node_modules` across the mono-repo.

### Running Specific Applications
- **Quick Notes UI**: `make notes-ui` (Runs `apps/web-quick-notes` frontend).
- **Notes API**: `make api-notes` (Runs `services/api-notes` Python FastAPI backend).

To see all available commands, simply run:
```bash
make help
```

## 🛠️ How to Initialize New Code / Apps

### Python Projects (ML, Services, Experiments)
We use [`uv`](https://docs.astral.sh/uv/) for fast Python environment management. To create a new python project:
```bash
make init-python project_name="my-cool-api" dir="services"
```
This automatically scaffolds a `uv` project inside `services/my-cool-api`.

### Node.js/TypeScript Projects (Apps, Packages)
To create a new Node.js workspace (it will be automatically recognized by Turborepo thanks to our `package.json` config):
```bash
make init-node dest="apps/new-frontend"
```
Alternatively, for frameworks like Next.js or Vite, run the standard CLI commands inside the `apps/` folder, e.g.:
```bash
cd apps && npx create-next-app@latest my-app
```
Then, add it to the `Makefile` commands to easily run it from the root.

## 📝 Adding Dependencies
- **Node.js**: Navigate to the specific workspace folder and run `npm install <package>`.
- **Python**: Navigate to the specific project folder and run `uv add <package>`.
