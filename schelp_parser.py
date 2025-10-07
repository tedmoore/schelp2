#!/usr/bin/env python3
"""
SuperCollider Help File (.schelp) Parser

Parses .schelp files (RST-like format) into an Abstract Syntax Tree (AST)
represented as a Python dictionary for conversion to Markdown using Jinja2.
"""

import re
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path


class SchelpParser:
    """Parser for SuperCollider .schelp documentation files."""
    
    # Block-level tags
    BLOCK_TAGS = [
        'class', 'title', 'summary', 'categories', 'related',
        'description', 'classmethods', 'instancemethods',
        'method', 'argument', 'returns', 'examples',
        'section', 'subsection', 'note', 'warning',
        'definitionlist', 'numberedlist', 'list', 'table',
        'private', 'discussion', 'image'
    ]
    
    # Inline tags
    INLINE_TAGS = [
        'link', 'code', 'emphasis', 'strong', 'teletype'
    ]
    
    def __init__(self, debug=False):
        self.lines = []
        self.current_line = 0
        self.debug = debug
        self.ast = {
            'type': 'document',
            'metadata': {},
            'content': []
        }
    
    def _debug_print(self, message, level=0):
        """Print debug message with indentation."""
        if self.debug:
            indent = "  " * level
            print(f"{indent}DEBUG: {message}")
    
    def parse_file(self, filepath: str) -> Dict[str, Any]:
        """
        Parse a .schelp file and return its AST.
        
        Args:
            filepath: Path to the .schelp file
            
        Returns:
            Dictionary representing the document AST
        """
        self._debug_print(f"Starting to parse file: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self._debug_print(f"File loaded, content length: {len(content)} chars")
        return self.parse(content)
    
    def parse(self, content: str) -> Dict[str, Any]:
        """
        Parse .schelp content and return its AST.
        
        Args:
            content: The .schelp file content as a string
            
        Returns:
            Dictionary representing the document AST
        """
        self._debug_print("Starting parse method")
        self.lines = content.split('\n')
        self.current_line = 0
        
        self._debug_print(f"Split into {len(self.lines)} lines")
        
        self.ast = {
            'type': 'document',
            'metadata': {},
            'content': []
        }
        
        while self.current_line < len(self.lines):
            self._debug_print(f"Main loop: line {self.current_line}/{len(self.lines)}: {repr(self._current()[:50])}", 1)
            try:
                self._parse_block()
            except Exception as e:
                self._debug_print(f"Error in _parse_block at line {self.current_line}: {e}")
                raise
        
        self._debug_print("Parse completed successfully")
        return self.ast
    
    def _current(self) -> str:
        """Get current line."""
        if self.current_line < len(self.lines):
            return self.lines[self.current_line]
        return ''
    
    def _peek(self, offset: int = 1) -> str:
        """Peek at a line ahead."""
        idx = self.current_line + offset
        if idx < len(self.lines):
            return self.lines[idx]
        return ''
    
    def _advance(self, count: int = 1):
        """Advance the line counter."""
        self.current_line += count
    
    def _parse_block(self):
        """Parse a block-level element."""
        line = self._current().strip()
        self._debug_print(f"_parse_block: processing line {self.current_line}: {repr(line[:100])}", 2)
        
        # Skip empty lines
        if not line:
            self._debug_print("_parse_block: skipping empty line", 3)
            self._advance()
            return
        
        # Check for block tags (tag::)
        tag_match = re.match(r'^(\w+)::\s*(.*?)$', line)
        if tag_match:
            tag_name = tag_match.group(1).lower()  # Convert to lowercase for consistent processing
            tag_value = tag_match.group(2).strip()
            self._debug_print(f"_parse_block: found tag '{tag_name}' with value '{tag_value}'", 3)
            try:
                self._parse_tag_block(tag_name, tag_value)
            except Exception as e:
                self._debug_print(f"Error in _parse_tag_block for {tag_name}: {e}")
                raise
            return
        
        # Check for code blocks (start with whitespace or tab)
        if line.startswith(('\t', '    ')) or (self._current().startswith((' ', '\t')) and self._current().strip()):
            self._debug_print("_parse_block: parsing as code block", 3)
            self._parse_code_block()
            return
        
        # Regular paragraph
        self._debug_print("_parse_block: parsing as paragraph", 3)
        self._parse_paragraph()
    
    def _parse_tag_block(self, tag_name: str, tag_value: str):
        """Parse a tag block (e.g., class::, method::, etc.)."""
        self._debug_print(f"_parse_tag_block: processing {tag_name} with value '{tag_value}'", 3)
        self._advance()
        
        # Metadata tags (top-level document info)
        if tag_name in ['class', 'title']:
            self.ast['metadata']['title'] = tag_value
            self.ast['metadata']['type'] = tag_name
        
        elif tag_name == 'summary':
            self.ast['metadata']['summary'] = tag_value
        
        elif tag_name == 'categories':
            self.ast['metadata']['categories'] = [
                cat.strip() for cat in tag_value.split(',') if cat.strip()
            ]
        
        elif tag_name == 'related':
            self.ast['metadata']['related'] = self._parse_related(tag_value)
        
        # Content blocks
        elif tag_name == 'description':
            block = {
                'type': 'section',
                'tag': 'description',
                'title': 'Description',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'classmethods':
            block = {
                'type': 'section',
                'tag': 'classmethods',
                'title': 'Class Methods',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'instancemethods':
            block = {
                'type': 'section',
                'tag': 'instancemethods',
                'title': 'Instance Methods',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'method':
            self._debug_print(f"_parse_tag_block: parsing method '{tag_value}'", 4)
            block = {
                'type': 'method',
                'name': tag_value,
                'arguments': [],
                'returns': None,
                'content': []
            }
            try:
                method_content = self._parse_method_content()
                self._debug_print(f"_parse_tag_block: method '{tag_value}' content parsed successfully", 4)
                block.update(method_content)
            except Exception as e:
                self._debug_print(f"Error parsing method '{tag_value}' content: {e}")
                raise
            self.ast['content'].append(block)
        
        elif tag_name == 'argument':
            # Arguments are typically parsed within method context
            block = {
                'type': 'argument',
                'name': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'returns':
            block = {
                'type': 'returns',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'examples':
            block = {
                'type': 'section',
                'tag': 'examples',
                'title': 'Examples',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'section':
            block = {
                'type': 'section',
                'tag': 'section',
                'title': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'subsection':
            block = {
                'type': 'subsection',
                'title': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'note':
            block = {
                'type': 'admonition',
                'admonition_type': 'note',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'warning':
            block = {
                'type': 'admonition',
                'admonition_type': 'warning',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'definitionlist':
            block = {
                'type': 'definition_list',
                'items': self._parse_definition_list()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'numberedlist':
            block = {
                'type': 'numbered_list',
                'items': self._parse_list()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'list':
            block = {
                'type': 'list',
                'items': self._parse_list()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'private':
            block = {
                'type': 'private',
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'code':
            # Handle code:: tags specially
            block = {
                'type': 'code_block',
                'content': self._parse_code_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'image':
            block = self._parse_image(tag_value)
            self.ast['content'].append(block)
        
        else:
            # Generic tag block
            block = {
                'type': 'tag_block',
                'tag': tag_name,
                'value': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
    
    def _parse_related(self, value: str) -> List[str]:
        """Parse the related:: field."""
        # Split by comma and clean up
        items = []
        for item in value.split(','):
            item = item.strip()
            if item:
                # Extract class name from Classes/ClassName format
                if '::' in item:
                    item = item.split('::')[-1]
                items.append(item)
        return items
    
    def _parse_block_content(self) -> List[Dict[str, Any]]:
        """Parse content until the next tag or dedent."""
        content = []
        
        while self.current_line < len(self.lines):
                
            line = self._current()
            
            # Stop at next tag
            if re.match(r'^\w+::', line.strip(), re.IGNORECASE):
                break
            
            # Stop at blank line followed by a tag
            if not line.strip():
                next_line = self._peek()
                if next_line and re.match(r'^\w+::', next_line.strip(), re.IGNORECASE):
                    self._advance()
                    break
            
            # Parse different content types
            stripped = line.strip()
            
            if not stripped:
                self._advance()
                # Skip blank lines between paragraphs
                continue
            
            # Check for code block (code:: marker or indented)
            if stripped == 'code::':
                content.append(self._parse_code_block())
                continue
            
            if line.startswith(('\t', '    ')) or (line and line[0] in ' \t' and stripped):
                content.append(self._parse_code_block())
                continue
            
            # Check for list item (##)
            if stripped.startswith('##'):
                item_content = stripped[2:].strip()
                content.append({
                    'type': 'list_item',
                    'content': self._parse_inline(item_content)
                })
                self._advance()
                continue
            
            # Check for numbered list item with numberedlist:: format
            if stripped.startswith('#'):
                item_content = stripped[1:].strip()
                content.append({
                    'type': 'list_item',
                    'content': self._parse_inline(item_content)
                })
                self._advance()
                continue
            
            # Skip standalone :: (code block end marker)
            if stripped == '::':
                self._advance()
                continue
            
            # Regular paragraph
            para = self._parse_paragraph()
            if para:
                content.append(para)
        
        return content
    
    def _parse_method_content(self) -> Dict[str, Any]:
        """Parse method-specific content including arguments and returns."""
        self._debug_print("_parse_method_content: starting", 5)
        result = {
            'arguments': [],
            'returns': None,
            'content': []
        }
        
        loop_count = 0
        while self.current_line < len(self.lines):
            loop_count += 1
            if loop_count > 1000:  # Safety check for infinite loops
                self._debug_print(f"_parse_method_content: INFINITE LOOP DETECTED! Breaking at line {self.current_line}")
                break
                
            line = self._current().strip()
            self._debug_print(f"_parse_method_content: loop {loop_count}, line {self.current_line}: {repr(line[:80])}", 6)
            
            # Stop at next method or major section (including examples)
            if re.match(r'^(method|classmethods|instancemethods|section|examples)::', line, re.IGNORECASE):
                self._debug_print(f"_parse_method_content: stopping at tag: {line}", 6)
                break
            
            # Parse argument (case-insensitive)
            if line.lower().startswith('argument::'):
                arg_name = line[line.lower().find('argument::')+10:].strip()
                self._debug_print(f"_parse_method_content: parsing argument '{arg_name}'", 6)
                self._advance()
                arg_content = []
                
                # Collect argument description
                arg_loop_count = 0
                while self.current_line < len(self.lines):
                    arg_loop_count += 1
                    if arg_loop_count > 100:
                        self._debug_print(f"_parse_method_content: argument parsing loop safety break at line {self.current_line}")
                        break
                        
                    arg_line = self._current().strip()
                    self._debug_print(f"_parse_method_content: arg loop {arg_loop_count}, line {self.current_line}: {repr(arg_line[:50])}", 7)
                    # Stop at any tag (especially examples::)
                    if re.match(r'^\w+::', arg_line, re.IGNORECASE):
                        self._debug_print(f"_parse_method_content: argument parsing stopped at tag: {arg_line}", 7)
                        break
                    if not arg_line:
                        self._debug_print("_parse_method_content: argument parsing skipping empty line", 7)
                        self._advance()
                        continue
                    
                    arg_content.append(self._parse_inline(arg_line))
                    self._advance()
                
                self._debug_print(f"_parse_method_content: argument '{arg_name}' parsed with {len(arg_content)} content items", 6)
                result['arguments'].append({
                    'name': arg_name,
                    'description': arg_content
                })
                continue
            
            # Parse returns (case-insensitive)
            if line.lower().startswith('returns::'):
                self._debug_print("_parse_method_content: parsing returns section", 6)
                self._advance()
                returns_content = []
                
                returns_loop_count = 0
                while self.current_line < len(self.lines):
                    returns_loop_count += 1
                    if returns_loop_count > 100:
                        self._debug_print(f"_parse_method_content: returns parsing loop safety break at line {self.current_line}")
                        break
                        
                    ret_line = self._current().strip()
                    self._debug_print(f"_parse_method_content: returns loop {returns_loop_count}, line {self.current_line}: {repr(ret_line[:50])}", 7)
                    # Stop at any tag (especially examples::)
                    if re.match(r'^\w+::', ret_line, re.IGNORECASE):
                        self._debug_print(f"_parse_method_content: returns parsing stopped at tag: {ret_line}", 7)
                        break
                    if not ret_line:
                        self._debug_print("_parse_method_content: returns parsing skipping empty line", 7)
                        self._advance()
                        continue
                    
                    returns_content.append(self._parse_inline(ret_line))
                    self._advance()
                
                self._debug_print(f"_parse_method_content: returns parsed with {len(returns_content)} content items", 6)
                result['returns'] = returns_content
                continue
            
            # Other content
            # Other content
            if not line:
                self._debug_print("_parse_method_content: skipping empty line", 6)
                self._advance()
                continue
            
            # Check if this is actually a tag that should end method parsing
            if re.match(r'^\w+::', line, re.IGNORECASE):
                self._debug_print(f"_parse_method_content: ending at tag: {line}", 6)
                break
            
            self._debug_print(f"_parse_method_content: processing other content: {repr(line[:50])}", 6)
            
            if line.startswith(('\t', ' ')):
                self._debug_print("_parse_method_content: parsing code block", 6)
                result['content'].append(self._parse_code_block())
            else:
                self._debug_print("_parse_method_content: parsing paragraph", 6)
                para = self._parse_paragraph()
                if para:
                    result['content'].append(para)
        
        self._debug_print(f"_parse_method_content: finished with {len(result['arguments'])} args, {len(result['content'])} content items", 5)
        return result

    def _parse_definition_list(self) -> List[Dict[str, Any]]:
        """Parse a definition list (## term || definition)."""
        items = []
        
        while self.current_line < len(self.lines):
            line = self._current().strip()
            
            # Stop at next tag or empty line followed by tag
            if not line or re.match(r'^\w+::', line, re.IGNORECASE):
                break
            
            # Parse definition item (## term || definition)
            if line.startswith('##'):
                item_text = line[2:].strip()
                if '||' in item_text:
                    term, definition = item_text.split('||', 1)
                    items.append({
                        'term': self._parse_inline(term.strip()),
                        'definition': self._parse_inline(definition.strip())
                    })
                self._advance()
            else:
                break
        
        return items
    
    def _parse_list(self) -> List[Dict[str, Any]]:
        """Parse a list (## item)."""
        items = []
        
        while self.current_line < len(self.lines):
            line = self._current().strip()
            
            # Stop at next tag
            if not line or re.match(r'^\w+::', line, re.IGNORECASE):
                break
            
            # Parse list item
            if line.startswith('##'):
                item_content = line[2:].strip()
                items.append(self._parse_inline(item_content))
                self._advance()
            else:
                break
        
        return items
    
    def _parse_paragraph(self) -> Optional[Dict[str, Any]]:
        """Parse a paragraph of text."""
        para_lines = []
        
        while self.current_line < len(self.lines):
            line = self._current()
            stripped = line.strip()
            
            # Stop conditions
            if not stripped:
                self._advance()
                break
            
            # Only stop on actual block-level tags, not inline tags
            block_tag_match = re.match(r'^(\w+)::', stripped, re.IGNORECASE)
            if block_tag_match:
                tag_name = block_tag_match.group(1).lower()
                if tag_name in self.BLOCK_TAGS:
                    break
            
            if line.startswith(('\t', '    ')):
                break
            
            para_lines.append(stripped)
            self._advance()
        
        if not para_lines:
            return None
        
        text = ' '.join(para_lines)
        return {
            'type': 'paragraph',
            'content': self._parse_inline(text)
        }
    
    def _parse_code_block(self) -> Dict[str, Any]:
        """Parse a code block (indented text)."""
        code_lines = []
        
        # Check if it starts with code::
        first_line = self._current().strip()
        if first_line == 'code::':
            self._advance()
        
        while self.current_line < len(self.lines):
            line = self._current()
            
            # Stop at :: on its own line (end marker)
            if line.strip() == '::':
                self._advance()
                break
            
            # Stop at dedent or new tag
            if line.strip() and not line.startswith(('\t', ' ')):
                if re.match(r'^\w+::', line.strip(), re.IGNORECASE):
                    break
                # If not indented and not empty, might be end of code block
                if code_lines and not line[0].isspace():
                    break
            
            # Empty line within code block
            if not line.strip():
                code_lines.append('')
                self._advance()
                continue
            
            # Add code line (preserve indentation within the block)
            code_lines.append(line.rstrip())
            self._advance()
        
        # Remove common leading whitespace
        if code_lines:
            # Find minimum indentation
            min_indent = float('inf')
            for line in code_lines:
                if line.strip():
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)
            
            if min_indent != float('inf'):
                code_lines = [line[min_indent:] if len(line) > min_indent else line 
                              for line in code_lines]
        
        return {
            'type': 'code_block',
            'content': '\n'.join(code_lines)
        }
    
    def _parse_image(self, value: str) -> Dict[str, Any]:
        """Parse an image tag."""
        # Format: path#caption
        parts = value.split('#', 1)
        return {
            'type': 'image',
            'path': parts[0].strip(),
            'caption': parts[1].strip() if len(parts) > 1 else ''
        }
    
    def _parse_code_block_content(self) -> str:
        """Parse code block content until :: end marker."""
        code_lines = []
        
        while self.current_line < len(self.lines):
            line = self._current()
            
            # Stop at :: on its own line (end marker)
            if line.strip() == '::':
                self._advance()
                break
            
            # Stop at new tag
            if line.strip() and re.match(r'^\w+::', line.strip(), re.IGNORECASE):
                break
            
            # Add the line (preserve original formatting)
            code_lines.append(line.rstrip())
            self._advance()
        
        # Join lines and clean up
        content = '\n'.join(code_lines)
        
        # Remove leading/trailing empty lines
        content = content.strip()
        
        return content
    
    def _parse_inline(self, text: str) -> List[Dict[str, Any]]:
        """
        Parse inline formatting like link::, code::, emphasis::, strong::.
        
        Returns a list of text and inline element dictionaries.
        """
        if not text:
            return []
        
        result = []
        current_pos = 0
        
        # Pattern for inline tags: tagname::content::
        # Also handle link::Classes/ClassName:: format
        pattern = r'(\w+)::(.*?)(?:::|\s|$)'
        
        for match in re.finditer(pattern, text):
            tag_name = match.group(1)
            tag_content = match.group(2)
            
            # Add any text before this tag
            if match.start() > current_pos:
                plain_text = text[current_pos:match.start()]
                if plain_text:
                    result.append({'type': 'text', 'content': plain_text})
            
            # Check if it's a known inline tag
            if tag_name in self.INLINE_TAGS or tag_name == 'link':
                if tag_name == 'link':
                    result.append({
                        'type': 'link',
                        'target': tag_content,
                        'text': tag_content.split('/')[-1] if '/' in tag_content else tag_content
                    })
                elif tag_name == 'code':
                    result.append({
                        'type': 'inline_code',
                        'content': tag_content
                    })
                elif tag_name == 'emphasis':
                    result.append({
                        'type': 'emphasis',
                        'content': tag_content
                    })
                elif tag_name == 'strong':
                    result.append({
                        'type': 'strong',
                        'content': tag_content
                    })
                else:
                    result.append({
                        'type': tag_name,
                        'content': tag_content
                    })
                
                current_pos = match.end()
            else:
                # Not an inline tag, treat as plain text
                pass
        
        # Add any remaining text
        if current_pos < len(text):
            remaining = text[current_pos:]
            if remaining:
                result.append({'type': 'text', 'content': remaining})
        
        # If no inline elements were found, return the whole text
        if not result:
            result.append({'type': 'text', 'content': text})
        
        return result


def main():
    """Example usage."""
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: python schelp_parser.py <file.schelp>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    parser = SchelpParser()
    
    try:
        ast = parser.parse_file(filepath)
        print(json.dumps(ast, indent=2))
    except Exception as e:
        print(f"Error parsing file: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
