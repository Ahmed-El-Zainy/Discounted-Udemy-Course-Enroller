#!/bin/bash
# Quick Start Script for DUCE Development Setup

set -e  # Exit on error

echo "=========================================="
echo "DUCE Development Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install build tools
echo ""
echo "Installing build tools..."
pip install build twine wheel

# Install package in editable mode
echo ""
echo "Installing DUCE in development mode..."
pip install -e .

# Verify installation
echo ""
echo "Verifying installation..."
if command -v duce &> /dev/null; then
    echo "✓ DUCE CLI installed successfully"
    duce --version
else
    echo "⚠ Warning: duce command not found in PATH"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start using DUCE:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo "  2. Run DUCE:"
echo "     duce"
echo ""
echo "To deactivate virtual environment:"
echo "  deactivate"
echo ""
