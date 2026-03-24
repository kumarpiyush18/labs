# Portfolio Website

A personal portfolio website generator built with Python and Jinja2. This project generates a static website that is fast, secure, and easy to host on GitHub Pages.

## 🚀 Features
- **Static Site Generation**: Builds HTML files from templates and data.
- **Content Management**: Easy to update content via Python dictionaries and Markdown files.
- **Blog Support**: Write blog posts in Markdown.
- **GitHub Activity**: Fetches and displays recent GitHub activity.
- **Responsive Design**: Modern, responsive UI with glassmorphism aesthetics.

## 📂 Project Structure

```
portfolio/
├── build.py           # Main build script
├── data.py            # Site configuration and content (Bio, Skills, Projects)
├── requirements.txt   # Python dependencies
├── content/           # Markdown content for blog posts
│   └── posts/
├── templates/         # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   └── ...
├── static/            # Static assets (CSS, JS, Images, Resume)
│   ├── css/
│   └── js/
└── docs/              # Generated static site (GitHub Pages source)
```

## 🛠️ Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

**requirements.txt**:
- `jinja2`: Templating engine.
- `markdown`: Converts Markdown to HTML.
- `pyyaml`: Parses YAML frontmatter in blog posts.

## 📝 How to Change Content

### 1. Personal Info & Projects
Edit `data.py` to update:
- **Site Config**: Title, author, social links.
- **Bio**: Headline, about text.
- **Skills**: List of skills.
- **Projects**: List of projects with descriptions and tags.

### 2. Blog Posts
Add new Markdown files to `content/posts/`. Format:

```markdown
---
title: My New Post
date: 2025-11-23
description: A short summary.
---

# Hello World
Write your post content here...
```

### 3. Styling
Edit `static/css/style.css` to change colors, fonts, or layout.

## 💻 How to Run Locally

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Build the Site**:
    ```bash
    python build.py
    ```
    This generates the HTML files in the `docs/` folder.

3.  **Serve Locally**:
    ```bash
    python -m http.server --directory docs
    ```
    Open [http://localhost:8000](http://localhost:8000) in your browser.

## 🚀 How to Deploy

This project is configured for **GitHub Pages**.

1.  **Build the latest version**:
    ```bash
    python build.py
    ```

2.  **Commit and Push**:
    ```bash
    git add .
    git commit -m "Update content"
    git push
    ```

3.  **Verify**:
    Go to `Settings > Pages` in your GitHub repository to ensure it's serving from the `/docs` folder on the `main` branch.

