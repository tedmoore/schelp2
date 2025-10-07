#!/usr/bin/env python3
"""
Batch convert multiple .schelp files to Markdown.
"""

import sys
import argparse
from pathlib import Path
from typing import List
import json
from schelp_parser import SchelpParser


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
                json_output: bool = False, recursive: bool = True):
    """
    Parse all .schelp files in a directory.
    
    Args:
        input_dir: Input directory containing .schelp files
        output_dir: Output directory for AST JSON files
        json_output: Whether to output JSON files
        recursive: Whether to search recursively
    """
    parser = SchelpParser(debug=True)
    schelp_files = find_schelp_files(input_dir, recursive)
    
    if not schelp_files:
        print(f"No .schelp files found in {input_dir}", file=sys.stderr)
        return
    
    print(f"Found {len(schelp_files)} .schelp files")
    
    results = []
    errors = []
    
    for schelp_file in schelp_files:
        try:
            print(f"Parsing {schelp_file}...", end=' ')
            ast = parser.parse_file(str(schelp_file))
            
            if json_output and output_dir:
                # Create output path
                output_path = Path(output_dir)
                output_path.mkdir(parents=True, exist_ok=True)
                
                # Generate output filename
                relative_path = schelp_file.relative_to(input_dir)
                json_file = output_path / relative_path.with_suffix('.json')
                json_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Write JSON
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(ast, f, indent=2)
                
                print(f"✓ -> {json_file}")
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
    
    args = parser.parse_args()
    
    try:
        results, errors = batch_parse(
            args.input_dir,
            args.output,
            args.json,
            not args.no_recursive
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
