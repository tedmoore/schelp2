# Minimal Sphinx configuration to be copied into docs/conf.py by build_docs.sh
import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------
project = 'SuperCollider Docs'
author = 'SuperCollider Contributors'
copyright = f"{datetime.now().year}, {author}"


# -- General configuration ---------------------------------------------------
# Extensions for better search, hosting, and documentation UX
# (No autodoc/napoleon since we're documenting SuperCollider, not Python)
extensions = [
    'myst_parser',                  # Parse Markdown (.md) files
    'sphinx.ext.autosectionlabel',  # Enable cross-references to section titles
    'sphinx_copybutton',            # Add copy button to code blocks
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Enable autosectionlabel so cross-references can target section titles
autosectionlabel_prefix_document = True

# -- Search Configuration ---------------------------------------------------
# Ensure search works properly on GitHub Pages
html_use_index = True
html_split_index = False
html_copy_source = True
html_show_sourcelink = False

# -- MyST Parser Configuration -----------------------------------------------
# Configure MyST to work better with standard Markdown syntax
myst_enable_extensions = [
    "colon_fence",      # Allow ::: fences (in addition to ```)
    "deflist",          # Definition lists
    "fieldlist",        # Field lists
    "html_image",       # HTML img tags
    "linkify",          # Auto-detect URLs
    "replacements",     # Text replacements
    "smartquotes",      # Smart quotes
    "strikethrough",    # ~~text~~
    "tasklist",         # - [ ] task lists
]

# Allow standard Markdown links to work as cross-references
myst_heading_anchors = 3  # Auto-generate anchors for headings up to h3

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']  # Use 'static' instead of '_static'

# Additional theme options for better search and navigation
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# -- Helpful defaults -------------------------------------------------------
# Use a consistent source suffix and master doc
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
language = 'en'  # Set language for search indexing

# Optional: customize the setup function if needed
# def setup(app):
#     pass

