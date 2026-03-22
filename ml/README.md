# ML (Machine Learning)

This directory contains machine learning pipelines, AI experiments, data processing scripts, and Jupyter notebooks.

## Quick Start
It is recommended to use `uv` for python environments. When scaffolding a new ML project, run:
```bash
make init-python project_name="my-model" dir="ml"
```
This will create a new Python project using `uv` inside `ml/my-model`.

## Best Practices
- Keep large datasets out of version control (add them to `.gitignore`).
- Document the requirements and running instructions per model.
