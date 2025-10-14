#!/usr/bin/env python3
"""
Example script showing how to use the scdoc_node_template.md Jinja2 template
with the JSON structure from scdoc_to_json.py
"""

import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def calculate_relative_path(from_path, to_path):
    """
    Calculate relative path from one file to another.
    
    Args:
        from_path: Source file path (e.g., "Tutorials/Mark_Polishook_tutorial")
        to_path: Target file path (e.g., "Classes/Symbol")
    
    Returns:
        Relative path string (e.g., "../../Classes/Symbol")
    """
    if not from_path or not to_path:
        return to_path
    
    # Split paths into parts
    from_parts = from_path.split('/')
    to_parts = to_path.split('/')
    
    # Calculate how many levels to go up
    levels_up = len(from_parts)
    
    # Build the relative path
    relative = '../' * levels_up + to_path
    
    return relative

def json_to_md(json_file, output_file=None, current_dir=None):
    """
    Render an SCDoc node JSON structure to Markdown using Jinja2.
    
    Args:
        json_file: Path to JSON file from scdoc_to_json.py
        output_file: Optional output markdown file path
        current_dir: Current directory path relative to docs root (e.g., "Classes" or "Tutorials/Mark_Polishook_tutorial")
    
    Returns:
        The rendered Markdown string
    """
    
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        doc = json.load(f)
    
    # Set up Jinja2 environment
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    # Add the relative path filter
    def relative_path_filter(target_path):
        """Jinja2 filter to convert absolute doc paths to relative paths"""
        return calculate_relative_path(current_dir, target_path)
    
    env.filters['relative_path'] = relative_path_filter
    
    # Load the template
    template = env.get_template("scdoc_node_template.md")
    
    # Render the template with the document data and current directory
    rendered = template.render(doc=doc, current_dir=current_dir)
    
    # Save to file if specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered)
        print(f"Successfully rendered to: {output_file}")
    
    return rendered


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Render SCDoc node JSON to Markdown using Jinja2"
    )
    parser.add_argument(
        "json_file",
        help="Path to JSON file from scdoc_to_json.py"
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        help="Output markdown file (prints to stdout if not specified)"
    )
    parser.add_argument(
        "-d", "--dir",
        dest="current_dir",
        help="Current directory path relative to docs root (e.g., 'Classes' or 'Tutorials/Mark_Polishook_tutorial')"
    )
    
    args = parser.parse_args()
    
    try:
        rendered = json_to_md(args.json_file, args.output_file, args.current_dir)
        
        if not args.output_file:
            print(rendered)
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
