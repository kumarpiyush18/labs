import os
import shutil
import markdown
import yaml
import json
import urllib.request
import time
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from data import site_config, bio, skills, projects

def load_posts():
    posts = []
    posts_dir = 'content/posts'
    if not os.path.exists(posts_dir):
        return posts
        
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                
            # Split frontmatter and content
            parts = content.split('---', 2)
            if len(parts) == 3:
                metadata = yaml.safe_load(parts[1])
                md_content = parts[2]
                # Added codehilite for better code snippets
                html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])
                
                post = metadata
                post['slug'] = filename.replace('.md', '')
                post['html_content'] = html_content
                posts.append(post)
    
    # Sort by date desc
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return posts

def fetch_github_activity(username):
    cache_file = 'github_cache.json'
    cache_expiry = 3600 # 1 hour
    
    # Check cache
    if os.path.exists(cache_file):
        mtime = os.path.getmtime(cache_file)
        if time.time() - mtime < cache_expiry:
            try:
                with open(cache_file, 'r') as f:
                    print("📦 Using cached GitHub activity")
                    return json.load(f)
            except Exception:
                pass

    try:
        print(f"🌐 Fetching GitHub activity for {username}...")
        url = f"https://api.github.com/users/{username}/events/public"
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            events = []
            for event in data:
                if event['type'] in ['PushEvent', 'CreateEvent', 'WatchEvent']:
                    events.append(event)
                    if len(events) >= 5:
                        break
            
            # Save to cache
            with open(cache_file, 'w') as f:
                json.dump(events, f)
                
            return events
    except Exception as e:
        print(f"⚠️ Could not fetch GitHub activity: {e}")
        # Return cached version even if expired if we hit rate limit
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                return json.load(f)
        return []

def build():
    # 1. Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    
    # 2. Output setup
    output_dir = 'docs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 3. Render Home
    github_activity = fetch_github_activity(site_config.get('github_username', 'kumarpiyush18'))

    template_home = env.get_template('index.html')
    output_home = template_home.render(
        config=site_config,
        bio=bio,
        skills=skills,
        projects=projects,
        github_activity=github_activity,
        root_path='.'
    )
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(output_home)
    print("✅ Generated docs/index.html")

    # 4. Render Blog Index & Posts
    posts = load_posts()
    
    # Blog Index
    template_blog = env.get_template('blog.html')
    output_blog = template_blog.render(
        config=site_config,
        posts=posts,
        root_path='.'
    )
    with open(os.path.join(output_dir, 'blog.html'), 'w') as f:
        f.write(output_blog)
    print("✅ Generated docs/blog.html")

    # Individual Posts
    posts_output_dir = os.path.join(output_dir, 'posts')
    if not os.path.exists(posts_output_dir):
        os.makedirs(posts_output_dir)
        
    template_post = env.get_template('post.html')
    for post in posts:
        output_post = template_post.render(
            config=site_config,
            post=post,
            root_path='..'
        )
        with open(os.path.join(posts_output_dir, f"{post['slug']}.html"), 'w') as f:
            f.write(output_post)
    print(f"✅ Generated {len(posts)} blog posts")

    # 5. Copy static assets
    static_src = 'static'
    static_dest = os.path.join(output_dir, 'static')
    
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    
    shutil.copytree(static_src, static_dest)
    print("✅ Copied static assets to docs/static")

if __name__ == "__main__":
    build()
