# Changelog

All notable changes to X WIRELESS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of X WIRELESS
- Wi-Fi network scanning capabilities
- Multiple output formats (JSON, Markdown, CSV)
- Inventory database with change tracking
- Safety features and legal compliance
- Comprehensive test suite
- CLI interface with Click
- GitHub Actions CI/CD pipeline

### Security
- Mandatory legal warning before use
- Target validation (localhost/internal only)
- Dry-run mode for safe testing
- Sandbox mode for offline testing
- No offensive capabilities (cracking, deauth, injection)

## [1.0.0] - 2024-12-01

### Added
- **Core Features**:
  - Wi-Fi network discovery using `iwlist` and `nmcli`
  - Automatic interface detection
  - Robust parsing with Pydantic models
  - Encryption detection (Open, WEP, WPA, WPA2, WPA3)
  - Signal level and quality analysis

- **Reporting**:
  - JSON output with metadata
  - Markdown reports with tables
  - CSV export for analysis
  - Author badge integration
  - GitHub Gist upload capability

- **Inventory Management**:
  - Local JSON database
  - Scan history tracking
  - Network change detection
  - Comparison between scans
  - Statistics and analytics

- **Safety Features**:
  - Legal compliance warnings
  - Target validation
  - Dry-run simulation mode
  - Sandbox testing with sample data
  - Comprehensive logging

- **CLI Interface**:
  - Click-based command interface
  - Multiple output formats
  - Verbose logging options
  - System information display
  - Version information

- **Testing**:
  - Comprehensive test suite
  - Sample data for testing
  - Coverage reporting
  - Sandbox mode testing
  - CI/CD integration

- **Documentation**:
  - Detailed README with examples
  - Contributing guidelines
  - Security policy
  - Installation instructions
  - Legal disclaimers

### Technical Details
- **Python**: 3.10+ compatibility
- **Dependencies**: click, pydantic, requests
- **Platform**: Linux (Ubuntu, Kali, etc.)
- **License**: MIT
- **Author**: Adil Fayyaz

### Legal Compliance
- Educational use only
- No offensive capabilities
- Mandatory authorization confirmation
- Local/internal network restrictions only
- Comprehensive legal warnings

---

## Version History

- **1.0.0**: Initial release with core functionality
- **Future versions**: Will follow semantic versioning

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Adil Fayyaz**  
Follow on Instagram: [@Infinityx_20257](https://instagram.com/Infinityx_20257)