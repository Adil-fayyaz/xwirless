#!/bin/bash
# X WIRELESS - Quick Start Script
# Created by: Adil Fayyaz
# Instagram: @Infinityx_20257

echo "X WIRELESS - Quick Start"
echo "========================"
echo "Created by: Adil Fayyaz"
echo "Instagram: @Infinityx_20257"
echo ""

# Check if we're in the correct directory
if [ ! -f "interface_english.py" ]; then
    echo "ERROR: interface_english.py not found"
    echo "Make sure you're in the xwirless directory"
    echo ""
    echo "To clone the repository:"
    echo "git clone https://github.com/Adil-fayyaz/xwirless.git"
    echo "cd xwirless"
    echo "./quick_start.sh"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 not installed"
    echo "Install with: sudo apt install python3 python3-pip"
    exit 1
fi

# Check dependencies
echo "Checking dependencies..."
python3 -c "import click, pydantic, requests" 2>/dev/null || {
    echo "Installing dependencies..."
    pip3 install click pydantic requests
}

# Start interface
echo ""
echo "Starting X WIRELESS..."
echo "===================="
echo ""

python3 interface_english.py
