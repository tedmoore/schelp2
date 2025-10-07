#!/usr/bin/env python3
"""
Convert .schelp files to Markdown using the parser and Jinja2 templates.
"""

import sys
import argparse
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
from schelp_parser import SchelpParser


def _get_template_environment(template_path: Path) -> Environment:
    """Create a Jinja2 environment capable of resolving partial includes."""
    search_path = template_path.parent
    loader = FileSystemLoader(str(search_path))
    return Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)


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
        template_path = Path(template_file)
        if not template_path.exists():
            raise FileNotFoundError(f"Template file not found: {template_file}")
    else:
        # Use default template bundled with the project
        template_path = Path(__file__).parent / 'templates' / 'template.md'

    template = None
    if template_path.exists():
        env = _get_template_environment(template_path)
        template = env.get_template(template_path.name)
    else:
        # Minimal inline template as a fallback if the file is missing
        template = Template("""# {{ doc.metadata.title }}

{% if doc.metadata.summary %}
{{ doc.metadata.summary }}
{% endif %}

{% for block in doc.content %}
{{ block }}
{% endfor %}
""")
    
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
