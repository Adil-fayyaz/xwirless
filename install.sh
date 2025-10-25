#!/bin/bash

# X WIRELESS - Installation Script
# Created by Adil Fayyaz
# Follow on Instagram: @Infinityx_20257

set -e

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                              X WIRELESS INSTALLER                           ║"
echo "║                                                                              ║"
echo "║  Created by: Adil Fayyaz                                                    ║"
echo "║  Follow on Instagram: @Infinityx_20257                                      ║"
echo "║                                                                              ║"
echo "║  ⚠️  EDUCATIONAL USE ONLY - LEGAL COMPLIANCE REQUIRED                       ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo "❌ Please do not run this script as root"
   echo "   The script will use sudo when needed for system packages"
   exit 1
fi

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt-get &> /dev/null; then
        OS="debian"
    elif command -v yum &> /dev/null; then
        OS="redhat"
    elif command -v pacman &> /dev/null; then
        OS="arch"
    else
        echo "❌ Unsupported Linux distribution"
        exit 1
    fi
else
    echo "❌ This script only supports Linux systems"
    exit 1
fi

echo "🔍 Detected OS: $OS"

# Check Python version
echo "🐍 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    echo "✅ Python $PYTHON_VERSION found"
    
    # Check if version is 3.10+
    if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 10) else 1)'; then
        echo "✅ Python version is compatible"
    else
        echo "❌ Python 3.10+ required, found $PYTHON_VERSION"
        echo "   Please install Python 3.10 or higher"
        exit 1
    fi
else
    echo "❌ Python 3 not found"
    echo "   Please install Python 3.10 or higher"
    exit 1
fi

# Install system dependencies
echo ""
echo "📦 Installing system dependencies..."

case $OS in
    "debian")
        echo "   Updating package list..."
        sudo apt-get update
        
        echo "   Installing wireless tools and network manager..."
        sudo apt-get install -y \
            wireless-tools \
            network-manager \
            python3-venv \
            python3-pip \
            python3-dev \
            build-essential
        
        echo "✅ System dependencies installed"
        ;;
    "redhat")
        echo "   Installing wireless tools and network manager..."
        sudo yum install -y \
            wireless-tools \
            NetworkManager \
            python3 \
            python3-pip \
            python3-devel \
            gcc
        
        echo "✅ System dependencies installed"
        ;;
    "arch")
        echo "   Installing wireless tools and network manager..."
        sudo pacman -S --noconfirm \
            wireless_tools \
            networkmanager \
            python \
            python-pip \
            base-devel
        
        echo "✅ System dependencies installed"
        ;;
esac

# Create virtual environment
echo ""
echo "🔧 Setting up Python environment..."

if [ ! -d "venv" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv venv
fi

echo "   Activating virtual environment..."
source venv/bin/activate

echo "   Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo ""
echo "📚 Installing Python dependencies..."

if [ -f "requirements.txt" ]; then
    echo "   Installing from requirements.txt..."
    pip install -r requirements.txt
else
    echo "   Installing core dependencies..."
    pip install click pydantic requests
fi

# Install package in development mode
if [ -f "pyproject.toml" ]; then
    echo "   Installing package in development mode..."
    pip install -e .
else
    echo "⚠️  pyproject.toml not found, skipping package installation"
fi

# Install development dependencies (optional)
echo ""
read -p "🔧 Install development dependencies? (pytest, black, flake8, mypy) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "   Installing development dependencies..."
    pip install pytest pytest-cov black flake8 mypy
    echo "✅ Development dependencies installed"
fi

# Run tests
echo ""
read -p "🧪 Run tests to verify installation? [Y/n]: " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    echo "   Running tests..."
    if command -v pytest &> /dev/null; then
        pytest tests/ -v --tb=short
        echo "✅ Tests completed"
    else
        echo "⚠️  pytest not available, skipping tests"
    fi
fi

# Test CLI
echo ""
echo "🚀 Testing CLI installation..."
if python3 -m xwirless --help &> /dev/null; then
    echo "✅ CLI is working correctly"
else
    echo "⚠️  CLI test failed, but installation may still be successful"
fi

# Create activation script
echo ""
echo "📝 Creating activation script..."
cat > activate_xwirless.sh << 'EOF'
#!/bin/bash
# X WIRELESS Activation Script
# Created by Adil Fayyaz

echo "🔌 Activating X WIRELESS environment..."
source venv/bin/activate
echo "✅ Environment activated!"
echo ""
echo "🚀 You can now use X WIRELESS:"
echo "   python -m xwirless --help"
echo "   python -m xwirless scan --dry-run"
echo ""
echo "⚠️  Remember: Educational use only on authorized networks!"
EOF

chmod +x activate_xwirless.sh

# Final instructions
echo ""
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                              INSTALLATION COMPLETE                           ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "🎉 X WIRELESS has been successfully installed!"
echo ""
echo "📋 Next steps:"
echo "   1. Activate the environment: source venv/bin/activate"
echo "   2. Or use the activation script: ./activate_xwirless.sh"
echo "   3. Test the installation: python -m xwirless --help"
echo "   4. Run a dry-run scan: python -m xwirless scan --dry-run"
echo ""
echo "⚠️  IMPORTANT REMINDERS:"
echo "   • This tool is for EDUCATIONAL USE ONLY"
echo "   • Only use on networks you OWN or have WRITTEN AUTHORIZATION"
echo "   • Always comply with applicable laws and regulations"
echo ""
echo "📞 Support:"
echo "   • Author: Adil Fayyaz"
echo "   • Instagram: @Infinityx_20257"
echo "   • GitHub: https://github.com/adilfayyaz/xwirless"
echo ""
echo "🔒 Stay legal, stay ethical, stay educational!"