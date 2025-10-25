# X WIRELESS - Deployment Guide

## 🚀 GitHub Repository Setup

### 1. Create GitHub Repository

```bash
# Initialize git repository
cd xwirless
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: X WIRELESS v1.0.0 - Educational Wi-Fi Audit Tool"

# Add remote origin (replace with your GitHub username)
git remote add origin https://github.com/adilfayyaz/xwirless.git

# Push to GitHub
git push -u origin main
```

### 2. Repository Settings

1. **Go to GitHub repository settings**
2. **Enable Issues and Discussions**
3. **Set up branch protection** for main branch
4. **Configure GitHub Pages** (optional)

### 3. GitHub Secrets Setup

For CI/CD and Gist upload functionality:

1. **Go to Settings > Secrets and variables > Actions**
2. **Add the following secrets**:

```
PYPI_API_TOKEN=your_pypi_token_here
GITHUB_TOKEN=your_github_token_here
```

## 🔐 GitHub Token Setup for Gist Upload

### 1. Create Personal Access Token

1. **Go to GitHub Settings > Developer settings > Personal access tokens**
2. **Click "Generate new token (classic)"**
3. **Select scopes**:
   - `gist` (for Gist creation)
   - `repo` (for repository access)
4. **Copy the token**

### 2. Configure Token Usage

```bash
# Set environment variable (temporary)
export GITHUB_TOKEN="your_token_here"

# Or add to .bashrc/.zshrc for permanent use
echo 'export GITHUB_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Test Gist Upload

```bash
# Test Gist upload functionality
python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --upload --gist-token $GITHUB_TOKEN
```

## 📦 PyPI Package Publishing

### 1. Create PyPI Account

1. **Register at [PyPI](https://pypi.org/account/register/)**
2. **Verify email address**
3. **Generate API token** in account settings

### 2. Build and Upload Package

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to PyPI
twine upload dist/* --username __token__ --password your_pypi_token
```

### 3. Test Package Installation

```bash
# Test installation from PyPI
pip install xwirless

# Test CLI
xwirless --help
```

## 🛠️ Development Workflow

### 1. Local Development

```bash
# Clone repository
git clone https://github.com/adilfayyaz/xwirless.git
cd xwirless

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Format code
black xwirless tests

# Lint code
flake8 xwirless tests
```

### 2. Feature Development

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and test
python -m xwirless scan --dry-run

# Commit changes
git add .
git commit -m "Add new feature: description"

# Push branch
git push origin feature/new-feature

# Create Pull Request on GitHub
```

### 3. Release Process

```bash
# Update version in pyproject.toml
# Update CHANGELOG.md
# Create release commit
git commit -m "Release v1.0.1"

# Create tag
git tag v1.0.1
git push origin v1.0.1

# GitHub Actions will automatically build and publish
```

## 🔧 Configuration Files

### 1. GitHub Actions Secrets

Required secrets for CI/CD:

- `PYPI_API_TOKEN`: For PyPI package publishing
- `GITHUB_TOKEN`: For GitHub API access

### 2. Local Configuration

Create `.env` file for local development:

```bash
# .env
GITHUB_TOKEN=your_github_token
PYPI_TOKEN=your_pypi_token
```

### 3. Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

## 📋 Checklist for Deployment

### Pre-Deployment

- [ ] All tests passing (`pytest tests/ -v`)
- [ ] Code formatted (`black xwirless tests`)
- [ ] Code linted (`flake8 xwirless tests`)
- [ ] Type checked (`mypy xwirless`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in pyproject.toml

### GitHub Repository

- [ ] Repository created and configured
- [ ] All files committed and pushed
- [ ] Branch protection rules set
- [ ] GitHub Actions secrets configured
- [ ] Issues and Discussions enabled

### Package Publishing

- [ ] PyPI account created
- [ ] API token generated
- [ ] Package built successfully
- [ ] Package uploaded to PyPI
- [ ] Installation tested from PyPI

### Documentation

- [ ] README.md complete and accurate
- [ ] CONTRIBUTING.md guidelines clear
- [ ] SECURITY.md policy defined
- [ ] CHANGELOG.md up to date
- [ ] Installation instructions tested

## 🚨 Important Notes

### Legal Compliance

- **Always maintain educational focus**
- **Keep safety warnings prominent**
- **No offensive capabilities**
- **Comply with all applicable laws**

### Security Considerations

- **Never commit tokens or secrets**
- **Use environment variables for sensitive data**
- **Regular security updates**
- **Monitor for vulnerabilities**

### Maintenance

- **Regular dependency updates**
- **Monitor GitHub Issues**
- **Update documentation as needed**
- **Keep CI/CD pipeline working**

## 📞 Support and Contact

- **Author**: Adil Fayyaz
- **Instagram**: [@Infinityx_20257](https://instagram.com/Infinityx_20257)
- **GitHub**: [adilfayyaz/xwirless](https://github.com/adilfayyaz/xwirless)
- **Issues**: [GitHub Issues](https://github.com/adilfayyaz/xwirless/issues)

---

**Remember: Educational use only on authorized networks!** 🛡️