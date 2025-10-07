#!/usr/bin/env python3
"""
Batch convert multiple .schelp files to JSON and Markdown.
"""

import sys
import argparse
from pathlib import Path
from typing import List
import json
from jinja2 import Template
from schelp_parser import SchelpParser


def ast_to_markdown(ast: dict) -> str:
    """
    Convert an AST to Markdown using the template.md file.
    
    Args:
        ast: The parsed AST dictionary
        
    Returns:
        Markdown content as string
    """
    template_file_path = Path(__file__).parent / 'template.md'
    
    if template_file_path.exists():
        with open(template_file_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    else:
        raise FileNotFoundError(f"Template file not found: {template_file_path}")
    
    template = Template(template_content)
    return template.render(doc=ast)


def find_schelp_files(directory: str, recursive: bool = True) -> List[Path]:
    """
    Find all .schelp files in a directory.
    
    Args:
        directory: Directory to search
        recursive: Whether to search recursively
        
    Returns:
        List of Path objects for .schelp files
    """
    dir_path = Path(directory)
    
    if recursive:
        return list(dir_path.rglob('*.schelp'))
    else:
        return list(dir_path.glob('*.schelp'))


def batch_parse(input_dir: str, output_dir: str = None, 
                json_output: bool = False, markdown_output: bool = False,
                recursive: bool = True, debug: bool = False):
    """
    Parse all .schelp files in a directory.
    
    Args:
        input_dir: Input directory containing .schelp files
        output_dir: Output directory for converted files
        json_output: Whether to output JSON files
        markdown_output: Whether to output Markdown files  
        recursive: Whether to search recursively
        debug: Whether to enable debug output
    """
    parser = SchelpParser(debug=debug)
    schelp_files = find_schelp_files(input_dir, recursive)
    
    if not schelp_files:
        print(f"No .schelp files found in {input_dir}", file=sys.stderr)
        return [], []
    
    print(f"Found {len(schelp_files)} .schelp files")
    
    results = []
    errors = []
    
    for schelp_file in schelp_files:
        try:
            print(f"Parsing {schelp_file}...", end=' ')
            ast = parser.parse_file(str(schelp_file))
            
            output_files = []
            
            if output_dir and (json_output or markdown_output):
                # Create base output path
                base_output_path = Path(output_dir)
                base_output_path.mkdir(parents=True, exist_ok=True)
                
                # Generate relative path for maintaining directory structure
                relative_path = schelp_file.relative_to(input_dir)
                
                # Output JSON if requested
                if json_output:
                    json_dir = base_output_path / 'json'
                    json_file = json_dir / relative_path.with_suffix('.json')
                    json_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(ast, f, indent=2)
                    output_files.append(f"JSON: {json_file}")
                
                # Output Markdown if requested
                if markdown_output:
                    md_dir = base_output_path / 'md'
                    md_file = md_dir / relative_path.with_suffix('.md')
                    md_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Convert AST to Markdown
                    markdown_content = ast_to_markdown(ast)
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    output_files.append(f"MD: {md_file}")
                
                if output_files:
                    print(f"✓ -> {', '.join(output_files)}")
                else:
                    print("✓")
            else:
                print("✓")
            
            results.append({
                'file': str(schelp_file),
                'success': True,
                'ast': ast
            })
            
        except Exception as e:
            print(f"✗ Error: {e}")
            errors.append({
                'file': str(schelp_file),
                'error': str(e)
            })
    
    # Print summary
    print(f"\n{'=' * 60}")
    print(f"Summary: {len(results)} successful, {len(errors)} errors")
    print(f"{'=' * 60}")
    
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  {error['file']}: {error['error']}")
    
    return results, errors


def generate_index(results: List[dict], output_file: str):
    """
    Generate an index of all parsed files.
    
    Args:
        results: List of parsing results
        output_file: Output file path
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# SuperCollider Documentation Index\n\n")
        
        # Group by category
        by_category = {}
        for result in results:
            ast = result['ast']
            categories = ast['metadata'].get('categories', ['Uncategorized'])
            title = ast['metadata'].get('title', 'Untitled')
            summary = ast['metadata'].get('summary', '')
            
            for category in categories:
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append({
                    'title': title,
                    'summary': summary,
                    'file': result['file']
                })
        
        # Write index
        for category in sorted(by_category.keys()):
            f.write(f"## {category}\n\n")
            for item in sorted(by_category[category], key=lambda x: x['title']):
                f.write(f"- **{item['title']}**")
                if item['summary']:
                    f.write(f" - {item['summary']}")
                f.write(f" ([source]({item['file']}))\n")
            f.write("\n")
    
    print(f"Index written to {output_file}")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Batch parse SuperCollider .schelp files'
    )
    parser.add_argument(
        'input_dir',
        help='Input directory containing .schelp files'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output directory for JSON AST files',
        default=None
    )
    parser.add_argument(
        '-i', '--index',
        help='Generate an index file',
        default=None
    )
    parser.add_argument(
        '--no-recursive',
        help='Do not search recursively',
        action='store_true'
    )
    parser.add_argument(
        '--json',
        help='Output JSON AST files',
        action='store_true'
    )
    parser.add_argument(
        '--markdown', '--md',
        help='Output Markdown files',
        action='store_true'
    )
    parser.add_argument(
        '--debug',
        help='Enable debug output',
        action='store_true'
    )
    
    args = parser.parse_args()
    
    try:
        results, errors = batch_parse(
            args.input_dir,
            args.output,
            args.json,
            args.markdown,
            not args.no_recursive,
            args.debug
        )
        
        if args.index and results:
            generate_index(results, args.index)
        
        sys.exit(0 if not errors else 1)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
