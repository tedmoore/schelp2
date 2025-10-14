#!/usr/bin/env python3
"""
Example script showing how to use the scdoc_node_template.md Jinja2 template
with the JSON structure from scdoc_to_json.py
"""

import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def json_to_md(json_file, output_file=None):
    """
    Render an SCDoc node JSON structure to Markdown using Jinja2.
    
    Args:
        json_file: Path to JSON file from scdoc_to_json.py
        output_file: Optional output markdown file path
    
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
    
    # Load the template
    template = env.get_template("scdoc_node_template.md")
    
    # Render the template with the document data
    rendered = template.render(doc=doc)
    
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
    
    args = parser.parse_args()
    
    try:
        rendered = json_to_md(args.json_file, args.output_file)
        
        if not args.output_file:
            print(rendered)
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
