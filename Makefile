# Makefile for SuperCollider Sphinx Documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -j auto
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build
PYTHON        ?= python3

# Put it first so that "make" without argument is like "make help".
help:
	@echo "SuperCollider Documentation Build"
	@echo "=================================="
	@echo ""
	@echo "Available targets:"
	@echo "  html       - Build HTML documentation (default)"
	@echo "  github     - Build for GitHub Pages (includes .nojekyll)"
	@echo "  clean      - Remove build artifacts"
	@echo "  install    - Install Python dependencies"
	@echo "  serve      - Serve docs locally on port 8000"
	@echo "  livehtml   - Auto-rebuild on changes (requires sphinx-autobuild)"

.PHONY: help html github clean install serve livehtml

# Install Python dependencies
install:
	@echo "📦 Installing Python dependencies..."
	@pip install -q -r requirements.txt

# Build HTML documentation
html:
	@echo "🏗️  Building HTML documentation..."
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "✅ Build complete!"
	@echo "📂 Output directory: $(BUILDDIR)/html/"
	@echo "🌐 Run 'make serve' to view locally"

# Build for GitHub Pages (includes .nojekyll file)
github: html
	@echo "📄 Creating .nojekyll for GitHub Pages..."
	@touch "$(BUILDDIR)/html/.nojekyll"
	@echo "✅ GitHub Pages build complete!"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf $(BUILDDIR)/*
	@rm -f docs/conf.py
	@echo "✅ Clean complete."

# Serve documentation locally
serve:
	@echo "🌐 Serving documentation on http://localhost:8000"
	@echo "   Press Ctrl+C to stop"
	@cd $(BUILDDIR)/html && $(PYTHON) -m http.server 8000

# Live server for development (requires sphinx-autobuild)
livehtml:
	@echo "🔄 Starting live rebuild server..."
	@sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
