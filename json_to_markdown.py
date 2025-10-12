#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
import json

def _get_template_environment(template_path: Path) -> Environment:
    """Create a Jinja2 environment capable of resolving partial includes."""
    search_path = template_path.parent
    loader = FileSystemLoader(str(search_path))
    return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

def convert_to_markdown(schelp_json_file: str, output_file: str = None) -> str:
    """
    Convert a .schelp file to Markdown.
    
    Args:
        schelp_file: Path to the .schelp file
        template_file: Path to the Jinja2 template (optional)
        output_file: Path for the output file (optional, defaults to stdout)
    """
    
    with open(schelp_json_file, 'r', encoding='utf-8') as f:
        ast = json.load(f)
    

    template_path = Path(__file__).parent / 'templates' / 'template.md'

    template = None
    if template_path.exists():
        env = _get_template_environment(template_path)
        template = env.get_template(template_path.name)

    
    # Render the template
    markdown = template.render(doc=ast)
    
    # Output
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Converted {schelp_json_file} -> {output_file}", file=sys.stderr)
    else:
        print(markdown)
    
    return markdown

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-j',
        help='Input .json file'
    )
    parser.add_argument(
        '-o',
        help='Output file (optional, prints to stdout if not specified)',
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        convert_to_markdown(args.j, args.o)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error converting file: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
