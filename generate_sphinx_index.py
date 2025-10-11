#!/usr/bin/env python3
"""
Generate Sphinx index.rst file from the markdown files in output/md
"""

import os
from pathlib import Path

def get_markdown_files(base_path):
    """Get all markdown files organized by category"""
    categories = {}
    base = Path(base_path)
    
    for category in ['Classes', 'Guides', 'Tutorials', 'Reference', 'Overviews', 'Other']:
        category_path = base / category
        if category_path.exists():
            files = sorted([
                f.relative_to(base).as_posix()
                for f in category_path.rglob('*.md')
            ])
            if files:
                categories[category] = files
    
    # Check for Help.md in the root
    help_file = base / 'Help.md'
    if help_file.exists():
        categories['Root'] = ['Help.md']
    
    return categories

def create_index_rst(output_path, md_base_path):
    """Create the index.rst file"""
    
    categories = get_markdown_files(md_base_path)
    
    content = """SuperCollider Help Documentation
===================================

Welcome to the SuperCollider help documentation! This is a comprehensive reference
for the SuperCollider audio synthesis environment.

SuperCollider is a platform for audio synthesis and algorithmic composition, used by
musicians, artists, and researchers working with sound. It is free and open source software
available for Windows, macOS, and Linux.

.. note::
   This documentation is automatically generated from SuperCollider's .schelp files.
   For the latest information, visit the `SuperCollider website <https://supercollider.github.io/>`_.

Getting Started
---------------

If you're new to SuperCollider, start with the :doc:`Getting Started tutorials <Tutorials/Getting-Started/00-Getting-Started-With-SC>`.

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Main Documentation
   
   Help

"""
    
    # Add each category as a separate toctree
    category_titles = {
        'Classes': 'Classes Reference',
        'Guides': 'User Guides',
        'Tutorials': 'Tutorials',
        'Reference': 'Language Reference',
        'Overviews': 'Overview Topics',
        'Other': 'Other Documentation'
    }
    
    # For large categories (like Classes), we'll create sub-index pages
    for category, files in categories.items():
        if category == 'Root':
            continue
            
        title = category_titles.get(category, category)
        
        if category == 'Classes' and len(files) > 50:
            # Create alphabetical sub-indices for Classes
            content += f"""
.. toctree::
   :maxdepth: 2
   :caption: {title}
   :glob:
   
   {category}/[A-C]*
   {category}/[D-F]*
   {category}/[G-I]*
   {category}/[J-L]*
   {category}/[M-O]*
   {category}/[P-R]*
   {category}/[S-U]*
   {category}/[V-Z]*

"""
        else:
            # Regular toctree for smaller categories
            content += f"""
.. toctree::
   :maxdepth: 1
   :caption: {title}
   :glob:
   
   {category}/*

"""
    
    content += """
Search
------

* :ref:`genindex`
* :ref:`search`

Additional Resources
--------------------

* `SuperCollider Homepage <https://supercollider.github.io/>`_
* `SuperCollider Forum <https://scsynth.org/>`_
* `SuperCollider on GitHub <https://github.com/supercollider/supercollider>`_
* `SuperCollider Wiki <https://github.com/supercollider/supercollider/wiki>`_

License
-------

SuperCollider is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software Foundation.

This documentation is licensed under a Creative Commons Attribution Share Alike 3.0 license.
"""
    
    # Write the index.rst file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated index.rst with {sum(len(f) for f in categories.values())} documentation files")
    for category, files in categories.items():
        print(f"  {category}: {len(files)} files")

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    docs_dir = script_dir / 'docs'
    md_dir = script_dir / 'output' / 'md'
    
    create_index_rst(docs_dir / 'index.rst', md_dir)
    print(f"\nIndex file created at: {docs_dir / 'index.rst'}")
