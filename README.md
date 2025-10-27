# Research Portfolio Website

A professional researcher portfolio built with Hugo and the PaperMod theme.

## Features

- 🎓 **Profile Mode** - Clean, professional landing page
- 📚 **Publications Page** - Showcase your research papers
- 🔬 **Projects Page** - Display your research projects
- 📄 **About Page** - Complete academic profile
- 🔍 **Search Functionality** - Easy content discovery
- 🌓 **Dark/Light Mode** - Automatic theme switching
- 📱 **Responsive Design** - Works on all devices
- 🤖 **Auto-Update Publications** - Weekly automatic updates from Google Scholar

## Quick Start

### Development Server

```bash
/opt/homebrew/bin/hugo server -D
```

Visit `http://localhost:1313` to see your site.

### Build for Production

```bash
/opt/homebrew/bin/hugo
```

The static site will be generated in the `public/` directory.

## Customization

### Update Your Profile

Edit `hugo.toml` to update:
- Your name and title
- Social media links
- Profile image
- Button links

### Add Publications

#### Manual Update
Edit `content/publications.md` to manually add your research papers.

#### Automatic Update from Google Scholar
The site includes an automatic update system that fetches your publications from Google Scholar weekly.

**Setup:**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the update script locally:
   ```bash
   python scripts/update_publications.py
   ```

**GitHub Actions (Automatic):**
- Updates run every Monday at 9:00 AM KST
- Can be manually triggered from GitHub Actions tab
- See `scripts/README.md` for configuration details

### Add Projects

Edit `content/projects.md` to showcase your research projects:
- Current projects
- Past projects
- Open source contributions
- Collaborations

### Update About Page

Edit `content/about.md` to include:
- Biography
- Education
- Experience
- Skills
- Awards

## Directory Structure

```
.
├── content/
│   ├── about.md          # About page
│   ├── publications.md   # Publications list
│   ├── projects.md       # Projects showcase
│   └── search.md         # Search page
├── static/
│   └── cv.pdf            # Your CV (add this)
│   └── profile.jpg       # Profile picture (add this)
├── themes/
│   └── PaperMod/         # Theme
├── hugo.toml             # Configuration
└── README.md
```

## Adding Content

### Add Your CV

Place your CV PDF in the `static/` directory:
```bash
cp /path/to/your/cv.pdf static/cv.pdf
```

### Add Profile Picture

Add your profile picture to the `static/` directory:
```bash
cp /path/to/your/photo.jpg static/profile.jpg
```

## Deployment

### GitHub Pages

1. Create a GitHub repository
2. Push your code
3. Enable GitHub Pages in repository settings
4. Set source to GitHub Actions
5. Add Hugo deployment workflow

### Netlify

1. Connect your Git repository
2. Build command: `hugo --gc --minify`
3. Publish directory: `public`
4. Deploy!

### Custom Domain

Update `baseURL` in `hugo.toml`:
```toml
baseURL = 'https://your-domain.com/'
```

## Customizing Theme Colors

Create `assets/css/extended/custom.css` to override colors:
```css
:root {
    --primary: #your-color;
}
```

## Tips

### Optimizing for Academic Use

1. **Publications**: Keep them updated with links to papers, code, and data
2. **Projects**: Include images, demos, and GitHub links
3. **CV**: Update regularly and keep it accessible
4. **SEO**: Fill in meta descriptions in each page
5. **Scholar Links**: Add Google Scholar, ORCID, ResearchGate

### Content Organization

- Use clear headings
- Add relevant links (papers, code, demos)
- Include visuals for projects
- Keep information current
- Add contact information

## Support

- [Hugo Documentation](https://gohugo.io/documentation/)
- [PaperMod Documentation](https://github.com/adityatelange/hugo-PaperMod/wiki)

## License

This portfolio template is free to use and modify for your academic website.
