#!/usr/bin/env python3
"""
Setup script for X WIRELESS.
Backward compatibility for older Python versions.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text().strip().split('\n')
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="xwirless",
    version="1.0.0",
    author="Adil Fayyaz",
    author_email="adilfayyaz388@gmail.com",
    description="X WIRELESS - Wi-Fi Audit & Inventory Tool for Educational Use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adilfayyaz/xwirless",
    project_urls={
        "Bug Reports": "https://github.com/adilfayyaz/xwirless/issues",
        "Source": "https://github.com/adilfayyaz/xwirless",
        "Documentation": "https://github.com/adilfayyaz/xwirless#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "xwirless=xwirless.cli:cli_main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="wifi audit inventory network security educational",
)