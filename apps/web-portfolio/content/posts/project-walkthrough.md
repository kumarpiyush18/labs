---
title: Project Walkthrough & Documentation
date: 2025-11-23
description: A detailed guide on how this portfolio was built, its features, and how to deploy it.
tags: [Documentation, Python, Guide]
---

# Python Static Portfolio - Walkthrough

## Overview
We have built a fast, modern, and feature-rich portfolio website using **Python** and **Jinja2**. The site is generated as static HTML in the `docs/` folder, making it perfect for hosting on **GitHub Pages**.

## Features Implemented
- **🎨 Glassmorphism Design**: A premium dark theme with blur effects and animations.
- **📝 Blog System**: Write posts in Markdown (`content/posts/`), and they are automatically converted to HTML.
- **🏷️ Project Filtering**: Filter projects by tags (Python, React, AI) using JavaScript.
- **🐙 GitHub Activity**: Fetches your latest public events from the GitHub API during the build.
- **📄 Resume Download**: Dedicated button in the navigation to download your resume.

## Project Structure
```text
.
├── build.py            # Main script to generate the site
├── data.py             # Configuration, bio, skills, and projects data
├── content/
│   └── posts/          # Markdown blog posts
├── templates/          # HTML templates (Jinja2)
├── static/             # CSS, JS, images, and resume.pdf
└── docs/               # Generated static site (Deploy this!)
```

## How to Use

### 1. Update Content
- **Profile**: Edit `data.py` to change your bio, skills, and social links.
- **Projects**: Add new projects to the `projects` list in `data.py`.
- **Blog**: Add new `.md` files to `content/posts/`.

### 2. Build the Site
Run the build script to regenerate the `docs/` folder:
```bash
python3 build.py
```

### 3. Preview Locally
Start a local server to see your changes:
```bash
python3 -m http.server 8000 --directory docs
```
Visit [http://localhost:8000](http://localhost:8000).

## Deployment (GitHub Pages)
1.  Push this entire project to a GitHub repository.
2.  Go to **Settings** > **Pages**.
3.  Under **Build and deployment**, select **Source** as `Deploy from a branch`.
4.  Select `main` branch and `/docs` folder.
5.  Click **Save**.

Your site will be live at `https://yourusername.github.io/repo-name/`.
