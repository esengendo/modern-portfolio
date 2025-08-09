# 🚀 Deployment Guide

This guide will help you deploy your modern portfolio to GitHub Pages.

## 📋 Prerequisites

- GitHub account
- Git installed on your computer
- Your portfolio files ready

## 🔧 Setup Steps

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it either:
   - `yourusername.github.io` (for main portfolio site)
   - `portfolio` or any other name (for project site)
3. Make it **public** (required for free GitHub Pages)
4. Don't initialize with README (we have our own files)

### 2. Connect Local Files to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: Modern portfolio with shadcn/ui design"

# Add remote repository (replace with your repo URL)
git remote add origin https://github.com/yourusername/repository-name.git

# Push to GitHub
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select:
   - **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)** or **/docs** (if using docs folder)
5. Click **Save**

### 4. Configure GitHub Actions (Automatic Deployment)

The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that will:
- Automatically build your site when you push changes
- Deploy to GitHub Pages
- Use UV for fast Python dependency management

To enable it:
1. Go to repository **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. The workflow will run automatically on every push to main branch

## 🌐 Access Your Site

After deployment, your site will be available at:
- Main site: `https://yourusername.github.io/`
- Project site: `https://yourusername.github.io/repository-name/`

*Note: It may take a few minutes for changes to appear.*

## 🔄 Updating Your Portfolio

### Method 1: Direct GitHub Edit
1. Go to your repository on GitHub
2. Navigate to `content/portfolio.md`
3. Click the pencil icon to edit
4. Make changes and commit
5. Site will automatically rebuild and deploy

### Method 2: Local Development
1. Edit files locally
2. Test by running: `python build_site.py`
3. Open `docs/index.html` in browser to preview
4. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update portfolio content"
   git push
   ```

## 🎨 Customization Options

### Content Updates
- **Personal Info**: Edit `content/portfolio.md`
- **Projects**: Update project sections in the markdown file
- **Contact**: Change contact information and links

### Design Changes
- **Colors**: Modify CSS custom properties in `static/css/style.css`
- **Layout**: Adjust HTML structure in `templates/index.html`
- **Animations**: Customize JavaScript in `static/js/script.js`

### Adding New Sections
1. Edit `templates/index.html` to add new HTML sections
2. Update `static/css/style.css` for styling
3. Add interactivity in `static/js/script.js` if needed
4. Rebuild with `python build_site.py`

## 🐛 Troubleshooting

### Site Not Loading
- Check GitHub Pages settings
- Ensure repository is public
- Wait 5-10 minutes after deployment
- Check GitHub Actions tab for build errors

### Build Errors
- Check GitHub Actions logs
- Ensure all required files are present
- Verify Python dependencies in `requirements.txt`

### Content Not Updating
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check that changes were committed and pushed
- Verify GitHub Actions completed successfully

### Local Development Issues
- Ensure Python virtual environment is activated
- Install dependencies: `uv pip install -r requirements.txt`
- Check Python version compatibility (3.8+)

## 📱 Mobile Testing

Test your site on different devices:
- **Mobile**: iPhone/Android browsers
- **Tablet**: iPad/Android tablet
- **Desktop**: Chrome, Firefox, Safari, Edge

## 🔍 SEO & Performance

The portfolio includes:
- **Meta Tags**: For social media sharing
- **Semantic HTML**: For search engines
- **Fast Loading**: Optimized assets
- **Mobile-First**: Responsive design
- **Accessibility**: Keyboard navigation and screen readers

## 📊 Analytics (Optional)

To add Google Analytics:
1. Create Google Analytics account
2. Get tracking ID
3. Add tracking code to `templates/index.html` before `</head>`

## 🔒 Security

- Keep dependencies updated
- Don't commit sensitive information
- Use environment variables for API keys (if needed)

## 🆘 Need Help?

- **GitHub Pages Docs**: https://docs.github.com/en/pages
- **GitHub Actions**: https://docs.github.com/en/actions
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Jinja2 Templates**: https://jinja.palletsprojects.com/

---

**Happy Deploying! 🎉**
