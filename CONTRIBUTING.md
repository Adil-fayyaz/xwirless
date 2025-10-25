# Contributing to X WIRELESS

Thank you for your interest in contributing to X WIRELESS! This document provides guidelines for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Legal Considerations](#legal-considerations)

## 🤝 Code of Conduct

By participating in this project, you agree to abide by our code of conduct:

- **Be respectful** and inclusive
- **Focus on educational value** and legal compliance
- **No offensive capabilities** - we maintain strict safety standards
- **Transparent communication** about changes and their purpose

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Linux system (Ubuntu, Kali, etc.)
- Basic understanding of Wi-Fi networking

### Development Setup

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/xwirless.git
   cd xwirless
   ```

2. **Set up development environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install in development mode
   pip install -e ".[dev]"
   ```

3. **Install pre-commit hooks**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## 🔧 Development Setup

### Project Structure

```
xwirless/
├── xwirless/           # Main package
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py          # CLI interface
│   ├── scanner.py      # Wi-Fi scanning
│   ├── parser.py       # Output parsing
│   ├── report.py       # Report generation
│   ├── db.py          # Database management
│   ├── safety.py      # Safety validation
│   └── utils.py       # Utility functions
├── tests/              # Test suite
│   ├── test_xwirless.py
│   └── samples/       # Sample data
├── .github/workflows/  # CI/CD
├── docs/              # Documentation
└── README.md
```

### Development Dependencies

```bash
pip install pytest pytest-cov black flake8 mypy pre-commit
```

## 📝 Contributing Process

### 1. Create an Issue

Before making changes, please:

- **Check existing issues** to avoid duplicates
- **Create an issue** describing your proposed changes
- **Wait for discussion** and approval before starting work

### 2. Create a Branch

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or bugfix branch
git checkout -b bugfix/issue-number
```

### 3. Make Changes

- **Follow code standards** (see below)
- **Add tests** for new functionality
- **Update documentation** as needed
- **Ensure legal compliance** - no offensive capabilities

### 4. Test Your Changes

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=xwirless --cov-report=html

# Test CLI
python -m xwirless scan --dry-run --sandbox tests/samples/sample_iwlist.txt

# Lint code
flake8 xwirless tests

# Type check
mypy xwirless

# Format code
black xwirless tests
```

### 5. Submit Pull Request

- **Fill out the PR template**
- **Reference related issues**
- **Provide clear description** of changes
- **Include test results**

## 📏 Code Standards

### Python Style

- **Follow PEP 8** guidelines
- **Use Black** for formatting (line length: 88)
- **Use type hints** with MyPy validation
- **Write docstrings** for all functions and classes

### Code Quality

```bash
# Format code
black xwirless tests

# Lint code
flake8 xwirless tests

# Type check
mypy xwirless
```

### Naming Conventions

- **Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **Files**: `snake_case.py`

## 🧪 Testing Guidelines

### Test Structure

```python
class TestFeatureName:
    """Test feature functionality."""
    
    def test_basic_functionality(self):
        """Test basic feature behavior."""
        # Arrange
        # Act
        # Assert
    
    def test_edge_cases(self):
        """Test edge cases and error conditions."""
        pass
```

### Test Requirements

- **Unit tests** for all new functions
- **Integration tests** for CLI commands
- **Sandbox mode tests** using sample data
- **Coverage target**: 80%+ for new code

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_parser.py -v

# With coverage
pytest tests/ --cov=xwirless --cov-report=html

# Test CLI
python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --dry-run
```

## 📚 Documentation

### Code Documentation

- **Docstrings**: Use Google style
- **Type hints**: Include for all functions
- **Comments**: Explain complex logic

### User Documentation

- **README updates**: For new features
- **CLI help**: Comprehensive help text
- **Examples**: Usage examples in docstrings

### Example Docstring

```python
def scan_networks(self, interface: Optional[str] = None) -> str:
    """Scan for Wi-Fi networks using safe system tools.
    
    Args:
        interface: Network interface to use. If None, auto-detects.
        
    Returns:
        Raw scan output from iwlist command.
        
    Raises:
        RuntimeError: If no interface found or scan fails.
        
    Example:
        >>> scanner = WiFiScanner()
        >>> output = scanner.scan_networks("wlan0")
        >>> "Cell" in output
        True
    """
```

## ⚖️ Legal Considerations

### Safety Requirements

- **No offensive capabilities**: No cracking, deauth, injection
- **Educational focus**: All features must serve educational purposes
- **Legal compliance**: Ensure all changes maintain legal compliance
- **Safety-by-design**: Maintain safety features and warnings

### Prohibited Changes

- ❌ Adding packet injection capabilities
- ❌ Implementing cracking algorithms
- ❌ Adding deauth attack features
- ❌ Removing safety warnings or validations
- ❌ Adding remote access capabilities

### Required Changes

- ✅ Maintain legal warnings
- ✅ Preserve safety validations
- ✅ Keep educational focus
- ✅ Ensure transparent operation

## 🐛 Bug Reports

When reporting bugs, please include:

1. **System information**: `python -m xwirless info`
2. **Python version**: `python --version`
3. **Steps to reproduce**
4. **Expected vs actual behavior**
5. **Error messages** (if any)
6. **Log files** (if verbose mode used)

## 💡 Feature Requests

For feature requests, please:

1. **Check existing issues** first
2. **Describe the educational value**
3. **Explain use cases**
4. **Ensure legal compliance**
5. **Consider implementation complexity**

## 📞 Support

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For general questions
- **Email**: For security concerns (see security policy)

## 🏆 Recognition

Contributors will be recognized in:

- **README.md**: Contributor list
- **Release notes**: For significant contributions
- **GitHub**: Contributor statistics

---

**Thank you for contributing to X WIRELESS!**

Remember: Keep it educational, keep it legal, keep it safe! 🛡️