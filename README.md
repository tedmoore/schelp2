# schelp2

This is an initial attempt at making a *new* helpfile system for SuperCollider. It is still very much a work in progress. Collaboration is invited! Early discussions and planning can be read in [this document](https://hedgedoc.musikinformatik.net/lLCXuzXtRwu6WlPs7CixFw#) created by @capital-G.

## Plan

* [ ] Python `.schelp` to `.json` converter. The `.json` files contain an abstract syntax tree for flexible validation, formatting, etc., for the steps below.
* [ ] Python `.json` to `.md` converter. Uses jinja2 templates.
* [ ] Use docs-web-build-system to serve `.md` docs on local server (currently this repos is using Sphinx, see screenshot below for styling).
* [ ] Ability to point consume the `.md` files as an abstract syntax tree and validate it against the SuperCollider class library (this can't be done at the `.json` stage because eventually it will be preferred for docs to be written in Markdown, and therefore will never go through the `.json` stage.)
* [ ] Code blocks and examples are stored in `.scd` files so they can be tested and validated as part of the docs build process.
* [ ] "In-source" documentation. This is further down the line but eventually it would be great to write Markdown in "docstrings" in `.sc` files. `.md` files will still be used for overviews, tutorials, guides, etc.

## Contributing

Yes, please do.

## Using this Repo

### 1. Setup Python Environment

Create and activate a virtual environment:

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 2. Convert SuperCollider Help Files

Convert `.schelp` files to `.json` and `.md`:

```bash
python batch_schelp_json_md.py -i /path/to/supercollider/HelpSource -j ./json -o ./docs
```

### 3. Build Documentation

**Using Make (recommended):**

```bash
make html      # Build HTML documentation
make serve     # Serve docs locally at http://localhost:8000
make github    # Build for GitHub Pages (includes .nojekyll)
make clean     # Remove build artifacts
make install   # Install Python dependencies only
make livehtml  # Auto-rebuild on changes (requires sphinx-autobuild)
```

**Windows users:**
```cmd
make.bat html
```

**Alternative (bash script):**
```bash
./build_docs.sh
```

**Manual build (all platforms):**
```bash
# Install dependencies
pip install -r requirements.txt

# Generate index
python generate_sphinx_index.py

# Copy config
cp config.py docs/conf.py          # macOS/Linux
copy config.py docs\conf.py        # Windows

# Build HTML
cd docs
sphinx-build -b html . _build/html -j auto
cd ..

# Serve locally
cd docs/_build/html
python -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Screenshot of Sphinx 'readthedocs' styling

![Screenshot of Sphinx 'readthedocs' styling](./resources/doc-screenshot-example.jpg)