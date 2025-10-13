#!/usr/bin/env python3
"""
Python wrapper for the scdoc_parse_dump C++ program.
This module provides a simple interface to parse SCDoc (.schelp) files
using the C++ parser and return the results as Python dictionaries.
"""

import subprocess
import json
import os
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any, Literal

# Path to the C++ parser executable
SCDOC_PARSER = Path(__file__).parent / "SCDoc" / "scdoc_parse_dump"

ParseMode = Literal["full", "partial", "metadata"]

class SCDocParseError(Exception):
    """Raised when the SCDoc parser encounters an error."""
    pass


def parse_schelp_file(
    input_file: str,
    mode: ParseMode = "full",
    output_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Parse an SCDoc (.schelp) file using the C++ parser.
    
    Args:
        input_file: Path to the .schelp file to parse
        mode: Parsing mode - one of "full", "partial", or "metadata"
            - "full": Parse the complete document (default)
            - "partial": Parse body only (skip metadata)
            - "metadata": Parse metadata only (skip body)
        output_file: Optional path to save the JSON output.
                    If None, a temporary file is used.
    
    Returns:
        A dictionary containing the parsed document structure
    
    Raises:
        FileNotFoundError: If input_file or the parser executable doesn't exist
        SCDocParseError: If the parser encounters an error
        subprocess.CalledProcessError: If the parser returns a non-zero exit code
    """
    
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Validate parser executable exists
    if not SCDOC_PARSER.exists():
        raise FileNotFoundError(
            f"SCDoc parser not found at: {SCDOC_PARSER}\n"
            f"Make sure to build the parser first by running: cd SCDoc && ./build_parser.sh"
        )
    
    # Build command
    cmd = [str(SCDOC_PARSER)]
    
    # Add mode flag if not full
    if mode == "partial":
        cmd.append("--partial")
    elif mode == "metadata":
        cmd.append("--metadata")
    elif mode != "full":
        raise ValueError(f"Invalid mode: {mode}. Must be 'full', 'partial', or 'metadata'")
    
    # Handle output file
    temp_file_created = False
    if output_file is None:
        # Create a temporary file
        fd, output_file = tempfile.mkstemp(suffix=".json", prefix="scdoc_")
        os.close(fd)  # Close the file descriptor
        temp_file_created = True
    
    try:
        # Add JSON output flag
        cmd.extend(["--json", output_file])
        
        # Add input file
        cmd.append(input_file)
        
        # Run the parser
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check for errors in stderr (parser writes info to stderr)
        if "ERROR:" in result.stderr:
            raise SCDocParseError(f"Parser error: {result.stderr}")
        
        # Read and return the JSON output
        with open(output_file, 'r', encoding='utf-8') as f:
            parsed_data = json.load(f)
        
        return parsed_data
        
    except subprocess.CalledProcessError as e:
        error_msg = f"Parser failed with exit code {e.returncode}"
        if e.stderr:
            error_msg += f"\nStderr: {e.stderr}"
        if e.stdout:
            error_msg += f"\nStdout: {e.stdout}"
        raise SCDocParseError(error_msg) from e
    
    finally:
        # Clean up temporary file if we created one
        if temp_file_created and os.path.exists(output_file):
            try:
                os.unlink(output_file)
            except OSError:
                pass  # Ignore cleanup errors


def get_node_text(node: Dict[str, Any]) -> str:
    """
    Extract the text content from a DocNode.
    
    Args:
        node: A parsed DocNode dictionary
    
    Returns:
        The text content of the node, or empty string if none exists
    """
    return node.get("text", "")


def get_node_children(node: Dict[str, Any]) -> list:
    """
    Get the children of a DocNode.
    
    Args:
        node: A parsed DocNode dictionary
    
    Returns:
        A list of child nodes, or empty list if none exist
    """
    return node.get("children", [])


def print_tree(node: Dict[str, Any], indent: int = 0):
    """
    Pretty-print the document tree structure.
    
    Args:
        node: A parsed DocNode dictionary
        indent: Current indentation level (used for recursion)
    """
    if node is None:
        return
    
    prefix = "  " * indent
    node_id = node.get("id", "unknown")
    text = node.get("text", "")
    
    # Print node info
    if text:
        # Truncate long text for display
        display_text = text[:50] + "..." if len(text) > 50 else text
        display_text = display_text.replace("\n", "\\n")
        print(f"{prefix}{node_id}: {display_text}")
    else:
        print(f"{prefix}{node_id}")
    
    # Recursively print children
    for child in node.get("children", []):
        print_tree(child, indent + 1)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Parse SCDoc (.schelp) files using the C++ parser"
    )
    parser.add_argument(
        "input_file",
        help="Path to the .schelp file to parse"
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        help="Output JSON file (optional, prints to stdout if not specified)"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["full", "partial", "metadata"],
        default="full",
        help="Parsing mode (default: full)"
    )
    parser.add_argument(
        "-t", "--tree",
        action="store_true",
        help="Print the document tree structure"
    )
    
    args = parser.parse_args()
    
    try:
        # Parse the file
        result = parse_schelp_file(
            args.input_file,
            mode=args.mode,
            output_file=args.output_file
        )
        
        if args.tree:
            # Print tree structure
            print_tree(result)
        elif not args.output_file:
            # Print JSON to stdout if no output file specified
            print(json.dumps(result, indent=2))
        else:
            print(f"Successfully parsed {args.input_file}")
            print(f"Output written to: {args.output_file}")
            
    except (FileNotFoundError, SCDocParseError) as e:
        print(f"Error: {e}")
        exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        exit(130)
