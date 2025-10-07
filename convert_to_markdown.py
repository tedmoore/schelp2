#!/usr/bin/env python3
"""
Convert .schelp files to Markdown using the parser and Jinja2 templates.
"""

import sys
import argparse
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
from schelp_parser import SchelpParser


def convert_to_markdown(schelp_file: str, template_file: str = None, output_file: str = None) -> str:
    """
    Convert a .schelp file to Markdown.
    
    Args:
        schelp_file: Path to the .schelp file
        template_file: Path to the Jinja2 template (optional)
        output_file: Path for the output file (optional, defaults to stdout)
    """
    # Parse the .schelp file
    parser = SchelpParser()
    ast = parser.parse_file(schelp_file)
    
    # Load template
    if template_file:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    else:
        # Use default template
        template_file_path = Path(__file__).parent / 'template.md'
        if template_file_path.exists():
            with open(template_file_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
        else:
            # Minimal inline template
            template_content = """# {{ doc.metadata.title }}

{% if doc.metadata.summary %}
{{ doc.metadata.summary }}
{% endif %}

{% for block in doc.content %}
{{ block }}
{% endfor %}
"""
    
    # Create Jinja2 environment and template
    template = Template(template_content)
    
    # Render the template
    markdown = template.render(doc=ast)
    
    # Output
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Converted {schelp_file} -> {output_file}", file=sys.stderr)
    else:
        print(markdown)
    
    return markdown


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Convert SuperCollider .schelp files to Markdown'
    )
    parser.add_argument(
        'input',
        help='Input .schelp file'
    )
    parser.add_argument(
        '-t', '--template',
        help='Jinja2 template file (optional, uses default if not specified)',
        default=None
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file (optional, prints to stdout if not specified)',
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        convert_to_markdown(args.input, args.template, args.output)
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
