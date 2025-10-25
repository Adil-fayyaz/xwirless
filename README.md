# X WIRELESS

<div align="center">

![X WIRELESS Logo](https://img.shields.io/badge/X%20WIRELESS-WiFi%20Audit-blue?style=for-the-badge&logo=wifi)

**Created by Adil Fayyaz**  
**Follow on Instagram: [@Infinityx_20257](https://instagram.com/Infinityx_20257)**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educational Use](https://img.shields.io/badge/Use-Educational%20Only-red.svg)](https://github.com/adilfayyaz/xwirless)

</div>

---

## ⚠️ IMPORTANT LEGAL NOTICE

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY**

- ✅ **ONLY** use on networks you **OWN**
- ✅ **ONLY** use with **EXPLICIT WRITTEN AUTHORIZATION**
- ❌ **NEVER** use for unauthorized access
- ❌ **NEVER** use for illegal activities

**The authors are NOT responsible for misuse of this tool.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Safety Features](#safety-features)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

**X WIRELESS** is an advanced Wi-Fi audit and inventory tool designed exclusively for educational purposes and testing on owned networks. It provides comprehensive network discovery, analysis, and reporting capabilities while maintaining strict safety-by-design principles.

### Key Principles

- **Safety First**: Built with legal compliance and safety in mind
- **Educational Focus**: Designed for learning and authorized testing
- **No Offensive Capabilities**: No cracking, deauth, or injection features
- **Transparent Operation**: Clear logging and dry-run capabilities

## ✨ Features

### 🔒 Safety Features
- **Legal Warning**: Mandatory confirmation before use
- **Dry-Run Mode**: Simulate operations without executing commands
- **Sandbox Mode**: Test with sample data offline
- **Target Validation**: Restricts to localhost and internal networks only

### 📡 Network Discovery
- **Auto-Detection**: Automatically finds wireless interfaces
- **Comprehensive Scanning**: Uses safe system tools (`iwlist`, `nmcli`)
- **Robust Parsing**: Pydantic models for reliable data extraction
- **Encryption Detection**: Identifies Open, WEP, WPA, WPA2, WPA3

### 📊 Reporting & Analysis
- **Multiple Formats**: JSON, Markdown, CSV output
- **Rich Metadata**: Timestamps, interface info, tool version
- **Author Badge**: Includes creator attribution
- **Gist Upload**: Optional GitHub Gist integration

### 💾 Inventory Management
- **Local Database**: JSON-based inventory storage
- **Scan History**: Track networks over time
- **Change Detection**: Compare scans and highlight differences
- **Network Tracking**: Monitor SSID, signal, and encryption changes

### 🛠️ Developer Features
- **Comprehensive Testing**: Full test suite with sample data
- **Type Safety**: MyPy type checking
- **Code Quality**: Black formatting, Flake8 linting
- **CI/CD**: GitHub Actions automation

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Linux system (Ubuntu, Kali, etc.)
- Wireless tools installed

### System Dependencies

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install wireless-tools network-manager python3-venv

# Kali Linux
sudo apt update
sudo apt install wireless-tools network-manager python3-venv
```

### Python Installation

```bash
# Clone repository
git clone https://github.com/adilfayyaz/xwirless.git
cd xwirless

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install package
pip install -e .

# Or install from PyPI (when available)
pip install xwirless
```

### Quick Install Script

```bash
# Download and run install script
curl -fsSL https://raw.githubusercontent.com/adilfayyaz/xwirless/main/install.sh | bash
```

## 🎯 Quick Start

### Basic Scan

```bash
# Run a basic scan (will show legal warning)
python -m xwirless scan

# Scan with specific interface
python -m xwirless scan --interface wlan0

# Generate JSON report
python -m xwirless scan --format json --output scan_results
```

### Dry-Run Mode (Safe Testing)

```bash
# Simulate scan without executing commands
python -m xwirless scan --dry-run --format md
```

### Sandbox Mode (Offline Testing)

```bash
# Use sample data for testing
python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json
```

## 📖 Usage Examples

### Comprehensive Scan with Database Storage

```bash
# Scan and save to inventory database
python -m xwirless scan --save-db --format all --output comprehensive_scan

# View inventory statistics
python -m xwirless inventory

# Compare two scans
python -m xwirless diff scan_20241201_143022 scan_20241201_150045
```

### Report Generation

```bash
# Generate Markdown report with author badge
python -m xwirless scan --format md --badge --output report

# Generate CSV for analysis
python -m xwirless scan --format csv --output networks.csv

# Upload to GitHub Gist (requires token)
python -m xwirless scan --upload --gist-token YOUR_GITHUB_TOKEN
```

### Advanced Usage

```bash
# Verbose logging
python -m xwirless scan --verbose --log-file scan.log

# Show system information
python -m xwirless info

# Show version information
python -m xwirless version
```

## 🛡️ Safety Features

### Legal Compliance

The tool enforces legal compliance through:

1. **Mandatory Legal Warning**: Users must confirm ownership/authorization
2. **Target Restrictions**: Only allows localhost and internal networks
3. **No Offensive Capabilities**: No cracking, deauth, or injection features
4. **Transparent Operation**: All actions are logged and auditable

### Safety Modes

- **Dry-Run**: `--dry-run` simulates operations without executing commands
- **Sandbox**: `--sandbox` uses sample data for offline testing
- **Verbose Logging**: `--verbose` provides detailed operation logs

### Educational Use Guidelines

1. **Only use on networks you own**
2. **Get written permission for any testing**
3. **Follow all applicable laws and regulations**
4. **Use responsibly and ethically**

## 🧪 Testing

### Run Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=xwirless --cov-report=html

# Test specific module
pytest tests/test_parser.py -v
```

### Test in Sandbox Mode

```bash
# Test CLI with sample data
python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --dry-run
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup

```bash
# Fork and clone repository
git clone https://github.com/YOUR_USERNAME/xwirless.git
cd xwirless

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code Standards

- **Formatting**: Use Black (`black xwirless tests`)
- **Linting**: Use Flake8 (`flake8 xwirless tests`)
- **Type Checking**: Use MyPy (`mypy xwirless`)
- **Testing**: Write tests for new features

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Reporting Issues

- Use GitHub Issues for bug reports
- Provide detailed reproduction steps
- Include system information (`python -m xwirless info`)
- Follow the issue template

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Educational Use Disclaimer

This software is designed EXCLUSIVELY for educational purposes and testing on networks you own or have explicit written authorization to test. The authors are NOT responsible for any misuse of this software.

## 📞 Support

- **Author**: Adil Fayyaz
- **Instagram**: [@Infinityx_20257](https://instagram.com/Infinityx_20257)
- **Issues**: [GitHub Issues](https://github.com/adilfayyaz/xwirless/issues)
- **Documentation**: [Project Wiki](https://github.com/adilfayyaz/xwirless/wiki)

---

<div align="center">

**Remember: Use responsibly and only on authorized networks!**

Made with ❤️ by [Adil Fayyaz](https://instagram.com/Infinityx_20257)

</div>