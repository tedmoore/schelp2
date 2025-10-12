#!/bin/bash
# Build script for SuperCollider Sphinx Documentation

set -e  # Exit on error

echo "🔧 SuperCollider Documentation Build Script"
echo "==========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "generate_sphinx_index.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -q -r requirements.txt

# Generate index
echo "📝 Generating Sphinx index..."
python3 generate_sphinx_index.py

# Copy root config.py into docs/conf.py so users can wipe docs/ safely
if [ -f "config.py" ]; then
    echo "📋 Copying root config.py into docs/conf.py (backing up existing conf.py if present)..."
    if [ -f "docs/conf.py" ]; then
        timestamp=$(date +%Y%m%d%H%M%S)
        echo "   Backing up existing docs/conf.py to docs/conf.py.bak.$timestamp"
        cp docs/conf.py docs/conf.py.bak.$timestamp
    fi
    cp config.py docs/conf.py
else
    echo "⚠️  Warning: root config.py not found; proceeding without copying."
fi

# Build documentation
echo "🏗️  Building HTML documentation..."
echo "   (This may take 2-3 minutes for 1100+ files...)"
cd docs
# Use parallel build with -j auto for faster builds
sphinx-build -b html . _build/html -j auto

# Create .nojekyll for GitHub Pages
touch _build/html/.nojekyll

echo ""
echo "✅ Build complete!"
echo ""
echo "📂 Output directory: docs/_build/html/"
echo "🌐 Open docs/_build/html/index.html in your browser to view"
echo ""
echo "To serve locally, run:"
echo "  cd docs/_build/html && python3 -m http.server 8000"
echo ""
