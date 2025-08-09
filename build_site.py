#!/usr/bin/env python3
"""
Modern portfolio site generator with shadcn/ui inspired design
"""

import os
import shutil
from jinja2 import Environment, FileSystemLoader
import markdown
import frontmatter

def create_directories():
    """Create necessary directories for the site"""
    dirs = ['docs', 'templates', 'static/css', 'static/js', 'static/images', 'content']
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)

def build_site():
    """Build the static site"""
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    
    # Load the main template
    template = env.get_template('index.html')
    
    # Load content
    with open('content/portfolio.md', 'r') as f:
        content = frontmatter.load(f)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['codehilite', 'fenced_code'])
    content_html = md.convert(content.content)
    
    # Render the page
    output = template.render(
        title=content.metadata.get('title', 'Emmanuel Sengendo'),
        content=content_html,
        metadata=content.metadata
    )
    
    # Write the output
    with open('docs/index.html', 'w') as f:
        f.write(output)
    
    # Copy static files
    if os.path.exists('static'):
        for item in os.listdir('static'):
            src = os.path.join('static', item)
            dst = os.path.join('docs', item)
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

if __name__ == '__main__':
    create_directories()
    build_site()
    print("✅ Site built successfully in 'docs' directory!")
    print("🚀 Ready for GitHub Pages deployment!")
