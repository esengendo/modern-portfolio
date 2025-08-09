# Emmanuel Sengendo - Modern Portfolio

A modern, responsive portfolio website built with Python, Jinja2, and modern web technologies. Features a shadcn/ui inspired design with dark/light mode, smooth animations, and mobile-first responsive design.

## 🚀 Features

- **Modern Design**: Clean, professional design inspired by shadcn/ui
- **Dark/Light Mode**: Toggle between themes with smooth transitions
- **Responsive**: Mobile-first design that works on all devices
- **Performance**: Optimized loading with lazy loading and animations
- **Accessibility**: Keyboard navigation and screen reader friendly
- **SEO Optimized**: Meta tags and semantic HTML structure

## 🛠 Tech Stack

- **Python**: Static site generation with Jinja2 templates
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript**: Modern ES6+ with smooth animations
- **Markdown**: Content management with frontmatter
- **GitHub Pages**: Free hosting and deployment

## 📁 Project Structure

```
esengendo-portfolio/
├── build_site.py          # Static site generator
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── content/
│   └── portfolio.md      # Portfolio content in Markdown
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── script.js     # Interactive functionality
│   └── images/           # Image assets
└── docs/                 # Generated site (GitHub Pages)
    ├── index.html
    ├── css/
    ├── js/
    └── images/
```

## 🚀 Quick Start

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd esengendo-portfolio
   uv venv .venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

2. **Build the Site**:
   ```bash
   python build_site.py
   ```

3. **Deploy to GitHub Pages**:
   - Push to your GitHub repository
   - Enable GitHub Pages in repository settings
   - Set source to "Deploy from a branch" and select "main" branch, "/docs" folder

## 📝 Customization

### Content
Edit `content/portfolio.md` to update:
- Personal information
- Project descriptions
- Skills and experience
- Contact information

### Styling
Modify `static/css/style.css` for:
- Custom animations
- Color schemes
- Layout adjustments

### Functionality
Update `static/js/script.js` for:
- Interactive features
- Animation triggers
- Form handling

## 🎨 Design Features

- **Glassmorphism**: Modern glass-like effects
- **Gradient Animations**: Dynamic color transitions
- **Particle Background**: Subtle floating particles
- **Hover Effects**: Smooth micro-interactions
- **Scroll Animations**: Elements fade in on scroll
- **Typography**: Inter font with proper hierarchy

## 📱 Responsive Breakpoints

- **Mobile**: 640px and below
- **Tablet**: 641px - 1024px
- **Desktop**: 1025px and above

## 🌟 Performance

- **Lazy Loading**: Images load as needed
- **Optimized CSS**: Minimal custom styles with Tailwind
- **Efficient JS**: Modern ES6+ with event delegation
- **Fast Loading**: Optimized assets and CDN usage

## 🔧 Development

To modify the site:

1. **Update Content**: Edit `content/portfolio.md`
2. **Rebuild**: Run `python build_site.py`
3. **Test**: Open `docs/index.html` in your browser
4. **Deploy**: Push changes to GitHub

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Built with ❤️ by Emmanuel Sengendo**
