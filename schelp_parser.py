#!/usr/bin/env python3
"""
SuperCollider Help File (.schelp) Parser

Parses .schelp files (RST-like format) into an Abstract Syntax Tree (AST)
represented as a Python dictionary for conversion to Markdown using Jinja2.
"""

import re
from typing import Dict, List, Any, Optional, Callable, Tuple
from pathlib import Path


class ParserError(RuntimeError):
    """Base class for parser errors."""


class UnknownBlockTagError(ParserError):
    """Raised when an unknown block-level tag is encountered."""

    def __init__(self, tag: str, line_number: int, line_content: str):
        super().__init__(
            f"Unknown block tag '{tag}' on line {line_number}: {line_content.strip()}"
        )
        self.tag = tag
        self.line_number = line_number
        self.line_content = line_content


class UnknownInlineTagError(ParserError):
    """Raised when an unknown inline tag is encountered."""

    def __init__(self, tag: str, line_number: int, line_content: str):
        super().__init__(
            f"Unknown inline tag '{tag}' on line {line_number}: {line_content.strip()}"
        )
        self.tag = tag
        self.line_number = line_number
        self.line_content = line_content


class SchelpParser:
    """Parser for SuperCollider .schelp documentation files."""
    
    # Block-level tags
    BLOCK_TAGS = set([
        'class', 'title', 'summary', 'categories', 'related',
        'description', 'classmethods', 'instancemethods',
        'method', 'argument', 'returns', 'examples',
        'section', 'subsection', 'warning', 'subsubsection',
        'definitionlist', 'numberedlist', 'list', 'table',
        'private', 'discussion', 'image', 'code', 'teletype', 'math',
        'tree', 'classtree','keyword', 'discussion',
        'copymethod', 'redirect', 'note'
    ])
    
    # Inline tags
    INLINE_TAGS = set([
        'link', 'code', 'emphasis', 'strong', 'teletype', 'math',
        'tree', 'footnote', 'list', 'soft', 'copymethod',
        'classtree', 'keyword', 'anchor', 'bindaddress', 'fill',
        'warning', 'next', 'must',
        'postinlinewarnings', 'table'
    ])
    
    def __init__(self, debug: bool = False, strict: bool = True):
        self.lines = []
        self.current_line = 0
        self.debug = debug
        self.strict = strict
        self.ast = {
            'type': 'document',
            'metadata': {},
            'content': []
        }
        # Pre-compute supported block tags including metadata tags
        self._metadata_tags = {'class', 'title', 'summary', 'categories', 'related'}
        self._supported_block_tags = set(self.BLOCK_TAGS) | self._metadata_tags
        self._inline_open_pattern = re.compile(r'([A-Za-z][\w-]*)::', re.IGNORECASE)
        self._special_inline_block_tags = {'footnote', 'code', 'table', 'list', 'tree', 'classtree'}
    
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

    def _is_block_tag_line(self, line: str) -> bool:
        """Determine if a line begins with a known block-level tag."""
        match = re.match(r'^(\w+)::', line.strip(), re.IGNORECASE)
        if not match:
            return False
        tag_name = match.group(1).lower()
        return tag_name in self._supported_block_tags
    
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
            if tag_name in self._supported_block_tags:
                self._debug_print(f"_parse_block: found block tag '{tag_name}' with value '{tag_value}'", 3)
                try:
                    self._parse_tag_block(tag_name, tag_value)
                except Exception as e:
                    self._debug_print(f"Error in _parse_tag_block for {tag_name}: {e}")
                    raise
                return
            if tag_name in self.INLINE_TAGS and '::' in tag_value:
                self._debug_print(f"_parse_block: treating inline-style tag '{tag_name}' as paragraph content", 3)
                # Fall through to paragraph parsing
            else:
                if self.strict:
                    raise UnknownBlockTagError(tag_name, self.current_line + 1, self._current())
                self._debug_print(f"_parse_block: treating unknown tag '{tag_name}' as paragraph (non-strict mode)", 3)
        
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
        
        elif tag_name == 'keyword':
            keywords = [kw.strip() for kw in tag_value.split(',') if kw.strip()]
            if keywords:
                existing = self.ast['metadata'].setdefault('keywords', [])
                existing.extend(keywords)

        elif tag_name == 'anchor':
            block = {
                'type': 'anchor',
                'name': tag_value
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

        elif tag_name == 'subsubsection':
            block = {
                'type': 'subsubsection',
                'title': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)

        elif tag_name == 'discussion':
            block = {
                'type': 'section',
                'tag': 'discussion',
                'title': 'Discussion' if not tag_value else tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'note':
            # Parse note as delimited block with inline content
            # We need to go back one line since _advance() was already called
            self.current_line -= 1
            inline_content = self._parse_delimited_inline_block()
            block = {
                'type': 'admonition',
                'admonition_type': 'note',
                'content': [{'type': 'paragraph', 'content': inline_content}]
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'warning':
            # Parse warning as delimited block with inline content
            # We need to go back one line since _advance() was already called
            self.current_line -= 1
            inline_content = self._parse_delimited_inline_block()
            block = {
                'type': 'admonition',
                'admonition_type': 'warning',
                'content': [{'type': 'paragraph', 'content': inline_content}]
            }
            self.ast['content'].append(block)
        
        elif tag_name == 'definitionlist':
            items, attachments = self._parse_definition_list()
            block = {
                'type': 'definition_list',
                'items': items
            }
            if attachments:
                block['attachments'] = attachments
            self.ast['content'].append(block)
        
        elif tag_name == 'numberedlist':
            items, attachments = self._parse_list()
            block = {
                'type': 'numbered_list',
                'items': items
            }
            if attachments:
                block['attachments'] = attachments
            self.ast['content'].append(block)
        
        elif tag_name == 'list':
            items, attachments = self._parse_list()
            block = {
                'type': 'list',
                'items': items
            }
            if attachments:
                block['attachments'] = attachments
            self.ast['content'].append(block)

        elif tag_name == 'table':
            block = self._parse_table(tag_value)
            self.ast['content'].append(block)

        elif tag_name == 'tree':
            block = self._parse_tree_block(tag_value)
            self.ast['content'].append(block)

        elif tag_name == 'classtree':
            block = self._parse_class_tree_block(tag_value)
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

        elif tag_name == 'teletype':
            block = {
                'type': 'code_block',
                'format': 'teletype',
                'content': self._parse_code_block_content()
            }
            self.ast['content'].append(block)

        elif tag_name == 'math':
            block = self._parse_math_block()
            self.ast['content'].append(block)

        elif tag_name == 'footnote':
            block = self._parse_footnote_block()
            self.ast['content'].append(block)
        
        elif tag_name == 'image':
            block = self._parse_image(tag_value)
            self.ast['content'].append(block)
        
        elif tag_name in self._generic_block_tags:
            block = {
                'type': 'tag_block',
                'tag': tag_name,
                'value': tag_value,
                'content': self._parse_block_content()
            }
            self.ast['content'].append(block)

        else:
            if self.strict:
                raise UnknownBlockTagError(tag_name, self.current_line, self._current())
            # Generic tag block fallback (non-strict mode)
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
                item = {
                    'type': 'link',
                    'target': item,
                    'text': item,
                }
                items.append(item)
        return items
    
    def _parse_block_content(self) -> List[Dict[str, Any]]:
        """Parse content until the next tag or dedent."""
        content = []
        
        while self.current_line < len(self.lines):
                
            line = self._current()
            
            # Stop at next tag
            if self._is_block_tag_line(line):
                break
            
            # Stop at blank line followed by a tag
            if not line.strip():
                next_line = self._peek()
                if next_line and self._is_block_tag_line(next_line):
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
                inline_nodes = self._parse_inline(item_content, self.current_line + 1)
                clean_nodes, pending_nodes = self._split_pending_from_inline(inline_nodes)
                content.append({
                    'type': 'list_item',
                    'content': clean_nodes
                })
                self._advance()
                self._handle_pending_blocks(pending_nodes, content)
                continue
            
            # Check for numbered list item with numberedlist:: format
            if stripped.startswith('#'):
                item_content = stripped[1:].strip()
                content.append({
                    'type': 'list_item',
                    'content': self._parse_inline(item_content, self.current_line + 1)
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
                clean, pending = self._split_pending_from_inline(para['content'])
                para['content'] = clean
                if para['content']:
                    content.append(para)
                self._handle_pending_blocks(pending, content)
        
        return content

    def _parse_delimited_inline_block(self) -> List[Dict[str, Any]]:
        """
        Parse content within a delimited block (note::, warning::, etc.)
        that ends with :: and may contain inline tags.
        
        Returns a list of parsed inline elements.
        """
        content_parts = []
        
        # Check if content is on the same line as the tag
        current = self._current().strip()
        tag_match = re.match(r'^\w+::\s*(.*)', current)
        if tag_match and tag_match.group(1):
            # Content starts on the same line
            rest_of_line = tag_match.group(1)
            # Check if it also closes on the same line
            if rest_of_line.endswith('::'):
                # Single-line delimited block
                inline_content = rest_of_line[:-2].strip()
                self._advance()
                return self._parse_inline(inline_content, self.current_line)
            else:
                # Multi-line starting on same line
                content_parts.append(rest_of_line)
                self._advance()
        else:
            # Content starts on the next line
            self._advance()
        
        # Collect lines until closing ::
        while self.current_line < len(self.lines):
            line = self._current()
            stripped = line.strip()
            
            # Check for closing ::
            if stripped == '::':
                self._advance()
                break
            
            # Check if line ends with ::
            if stripped.endswith('::') and not stripped.endswith(':::'):
                # Remove the closing ::
                content_parts.append(stripped[:-2].strip())
                self._advance()
                break
            
            # Stop at another block tag (safety measure)
            if self._is_block_tag_line(line):
                break
            
            if stripped:
                content_parts.append(stripped)
            
            self._advance()
        
        # Join all content and parse as inline
        full_content = ' '.join(content_parts)
        return self._parse_inline(full_content, self.current_line) if full_content else []

    def _split_pending_from_inline(self, inline_nodes: List[Dict[str, Any]]):
        """Separate pending block markers from inline nodes."""
        pending = []
        clean = []
        for node in inline_nodes:
            if isinstance(node, dict) and node.get('type') == 'pending_block':
                pending.append(node)
            else:
                clean.append(node)
        return clean, pending

    def _handle_pending_blocks(self, pending_nodes: List[Dict[str, Any]], container: List[Dict[str, Any]]):
        """Parse pending blocks indicated by inline markers and append them to container."""
        for node in pending_nodes:
            block = self._parse_pending_block(node)
            if block:
                container.append(block)

    def _parse_pending_block(self, node: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Dispatch parsing for inline markers that open block-level content."""
        tag = node.get('tag')
        value = node.get('value', '')

        if tag == 'code':
            return self._parse_code_block()
        if tag == 'footnote':
            return self._parse_footnote_block()
        if tag == 'table':
            return self._parse_table(value)
        if tag == 'list':
            items, attachments = self._parse_list()
            block = {
                'type': 'list',
                'items': items
            }
            if attachments:
                block['attachments'] = attachments
            return block
        if tag == 'tree':
            return self._parse_tree_block(value)
        if tag == 'classtree':
            return self._parse_class_tree_block(value)
        return None

    def _parse_footnote_block(self) -> Dict[str, Any]:
        """Parse a footnote block delimited by :: markers."""
        content: List[Dict[str, Any]] = []

        while self.current_line < len(self.lines):
            line = self._current().strip()

            if line == '::':
                self._advance()
                break

            if not line:
                self._advance()
                continue

            if self._is_block_tag_line(line):
                break

            para = self._parse_paragraph()
            if para:
                clean, pending = self._split_pending_from_inline(para['content'])
                para['content'] = clean
                if para['content']:
                    content.append(para)
                self._handle_pending_blocks(pending, content)

        return {
            'type': 'footnote',
            'content': content
        }
    
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
                
            raw_line = self._current()

            # Split trailing argument declarations that share a line with text
            if 'argument::' in raw_line and not raw_line.lstrip().lower().startswith('argument::'):
                prefix, remainder = raw_line.split('argument::', 1)
                self.lines[self.current_line] = prefix.rstrip()
                self.lines.insert(self.current_line + 1, f"argument::{remainder.strip()}")
                if not self.lines[self.current_line]:
                    self._advance()
                continue

            line = raw_line.strip()
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
                        
                    raw_arg_line = self._current()

                    if 'argument::' in raw_arg_line and not raw_arg_line.lstrip().lower().startswith('argument::'):
                        prefix, remainder = raw_arg_line.split('argument::', 1)
                        self.lines[self.current_line] = prefix.rstrip()
                        self.lines.insert(self.current_line + 1, f"argument::{remainder.strip()}")
                        if not self.lines[self.current_line]:
                            self._advance()
                        continue

                    if 'returns::' in raw_arg_line and not raw_arg_line.lstrip().lower().startswith('returns::'):
                        prefix, remainder = raw_arg_line.split('returns::', 1)
                        self.lines[self.current_line] = prefix.rstrip()
                        self.lines.insert(self.current_line + 1, f"returns::{remainder.strip()}")
                        if not self.lines[self.current_line]:
                            self._advance()
                        continue

                    arg_line = raw_arg_line.strip()
                    self._debug_print(f"_parse_method_content: arg loop {arg_loop_count}, line {self.current_line}: {repr(arg_line[:50])}", 7)
                    # Stop at any tag (especially examples::)
                    if self._is_block_tag_line(arg_line):
                        self._debug_print(f"_parse_method_content: argument parsing stopped at tag: {arg_line}", 7)
                        break
                    if not arg_line:
                        self._debug_print("_parse_method_content: argument parsing skipping empty line", 7)
                        self._advance()
                        continue
                    
                    arg_content.append(self._parse_inline(arg_line, self.current_line + 1))
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
                        
                    raw_ret_line = self._current()

                    if 'returns::' in raw_ret_line and not raw_ret_line.lstrip().lower().startswith('returns::'):
                        prefix, remainder = raw_ret_line.split('returns::', 1)
                        self.lines[self.current_line] = prefix.rstrip()
                        self.lines.insert(self.current_line + 1, f"returns::{remainder.strip()}")
                        if not self.lines[self.current_line]:
                            self._advance()
                        continue

                    ret_line = raw_ret_line.strip()
                    self._debug_print(f"_parse_method_content: returns loop {returns_loop_count}, line {self.current_line}: {repr(ret_line[:50])}", 7)
                    # Stop at any tag (especially examples::)
                    if self._is_block_tag_line(ret_line):
                        self._debug_print(f"_parse_method_content: returns parsing stopped at tag: {ret_line}", 7)
                        break
                    if not ret_line:
                        self._debug_print("_parse_method_content: returns parsing skipping empty line", 7)
                        self._advance()
                        continue
                    
                    returns_content.append(self._parse_inline(ret_line, self.current_line + 1))
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
            if self._is_block_tag_line(line):
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

    def _parse_definition_list(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Parse a definition list (## term || definition)."""
        items = []
        attachments: List[Dict[str, Any]] = []
        
        while self.current_line < len(self.lines):
            line = self._current().strip()
            
            # Stop at next tag or empty line followed by tag
            if not line or self._is_block_tag_line(line):
                break
            
            # Parse definition item (## term || definition)
            if line.startswith('##'):
                item_text = line[2:].strip()
                pending_nodes: List[Dict[str, Any]] = []
                if '||' in item_text:
                    term, definition = item_text.split('||', 1)
                    term_inline = self._parse_inline(term.strip(), self.current_line + 1)
                    def_inline = self._parse_inline(definition.strip(), self.current_line + 1)
                    clean_term, term_pending = self._split_pending_from_inline(term_inline)
                    clean_def, def_pending = self._split_pending_from_inline(def_inline)
                    items.append({
                        'term': clean_term,
                        'definition': clean_def
                    })
                    pending_nodes = term_pending + def_pending
                self._advance()
                for pending in pending_nodes:
                    block = self._parse_pending_block(pending)
                    if block:
                        attachments.append(block)
            else:
                break
        
        return items, attachments
    
    def _parse_list(self) -> Tuple[List[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        """Parse a list (## item)."""
        items: List[List[Dict[str, Any]]] = []
        attachments: List[Dict[str, Any]] = []
        
        while self.current_line < len(self.lines):
            line = self._current().strip()
            
            # Stop at next tag
            if not line or self._is_block_tag_line(line):
                break
            
            # Parse list item
            if line.startswith('##'):
                item_content = line[2:].strip()
                inline_nodes = self._parse_inline(item_content, self.current_line + 1)
                clean_nodes, pending_nodes = self._split_pending_from_inline(inline_nodes)
                items.append(clean_nodes)
                self._advance()
                for pending in pending_nodes:
                    block = self._parse_pending_block(pending)
                    if block:
                        attachments.append(block)
            else:
                break
        
        return items, attachments

    def _parse_table(self, title: str) -> Dict[str, Any]:
        """Parse a simple table (rows separated by newlines, cells by ||)."""
        rows: List[List[str]] = []

        while self.current_line < len(self.lines):
            line = self._current()
            stripped = line.strip()

            # Stop at next tag or blank line followed by tag
            if not stripped:
                self._advance()
                next_line = self._current() if self.current_line < len(self.lines) else ''
                if next_line and re.match(r'^\w+::', next_line.strip(), re.IGNORECASE):
                    break
                continue

            if re.match(r'^\w+::', stripped, re.IGNORECASE):
                break

            cells = [cell.strip() for cell in re.split(r'\s*\|\|\s*', stripped)]
            rows.append(cells)
            self._advance()

        return {
            'type': 'table',
            'title': title,
            'rows': rows
        }

    def _parse_tree_block(self, title: str) -> Dict[str, Any]:
        """Parse a tree:: block preserving its textual structure."""
        lines: List[str] = []
        title = title.strip()

        while self.current_line < len(self.lines):
            line = self._current()
            stripped_line = line.rstrip('\n')
            stripped = stripped_line.strip()

            if not stripped:
                next_line = self._peek()
                self._advance()
                if next_line and self._is_tree_content_line(next_line):
                    lines.append('')
                    continue
                break

            if self._is_tree_content_line(line):
                lines.append(stripped_line)
                self._advance()
                continue

            break

        return {
            'type': 'tree',
            'title': title,
            'content': '\n'.join(lines).strip()
        }

    def _is_tree_content_line(self, line: str) -> bool:
        """Determine if a line forms part of a tree representation."""
        if line is None:
            return False
        stripped = line.strip()
        if not stripped:
            return False
        if stripped == '::':
            return True
        if stripped.startswith('tree::'):
            return True
        if line.startswith((' ', '\t')):
            return True
        return False

    def _parse_class_tree_block(self, value: str) -> Dict[str, Any]:
        """Parse a classtree:: block (typically a single reference)."""
        return {
            'type': 'class_tree',
            'root': value.strip()
        }
    
    def _parse_paragraph(self) -> Optional[Dict[str, Any]]:
        """Parse a paragraph of text."""
        para_lines = []
        start_line = self.current_line
        
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
                if tag_name in self._supported_block_tags:
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
            'content': self._parse_inline(text, start_line + 1)
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

    def _parse_math_block(self) -> Dict[str, Any]:
        """Parse a math block delimited by math:: ... ::"""
        math_lines: List[str] = []

        while self.current_line < len(self.lines):
            line = self._current()
            stripped = line.strip()

            if stripped == '::':
                self._advance()
                break

            math_lines.append(line.rstrip())
            self._advance()

        content = '\n'.join(math_lines).strip()
        return {
            'type': 'math_block',
            'content': content
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
    
    def _parse_inline(self, text: str, line_number: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Parse inline formatting like link::, code::, emphasis::, strong::.
        
        Returns a list of text and inline element dictionaries.
        """
        if not text:
            return []
        
        result = []
        position = 0
        text_length = len(text)

        # Pre-compile inline tag handlers for clarity
        inline_handlers: Dict[str, Callable[[str], Dict[str, Any]]] = {
            'link': lambda value: {
                'type': 'link',
                'target': value.split('##')[0].strip() if '##' in value else value,
                'text': value.split('##')[1].strip() if '##' in value else value
            },
            'code': lambda value: {
                'type': 'inline_code',
                'content': value
            },
            'teletype': lambda value: {
                'type': 'inline_code',
                'content': value
            },
            'emphasis': lambda value: {
                'type': 'emphasis',
                'content': value
            },
            'strong': lambda value: {
                'type': 'strong',
                'content': value
            },
            'math': lambda value: {
                'type': 'math',
                'content': value
            },
            'note': lambda value: {
                'type': 'inline_note',
                'content': value
            },
            'tree': lambda value: {
                'type': 'inline_tree',
                'content': value
            },
            'footnote': lambda value: {
                'type': 'footnote',
                'content': value
            },
            'list': lambda value: {
                'type': 'inline_list',
                'content': value
            },
            'soft': lambda value: {
                'type': 'soft',
                'content': value
            },
            'copymethod': lambda value: {
                'type': 'copymethod',
                'content': value
            },
            'classtree': lambda value: {
                'type': 'inline_tree',
                'content': value
            },
            'keyword': lambda value: {
                'type': 'inline_keyword',
                'content': value
            },
            'anchor': lambda value: {
                'type': 'inline_anchor',
                'content': value
            },
            'bindaddress': lambda value: {
                'type': 'inline_code',
                'content': value or 'bindAddress'
            },
            'fill': lambda value: {
                'type': 'inline_code',
                'content': value or 'fill'
            },
            'warning': lambda value: {
                'type': 'inline_warning',
                'content': value
            },
            'next': lambda value: {
                'type': 'inline_code',
                'content': value or 'next'
            },
            'must': lambda value: {
                'type': 'strong',
                'content': value or 'must'
            },
            'vcf': lambda value: {
                'type': 'inline_code',
                'content': value or 'vcf'
            },
            'z': lambda value: {
                'type': 'inline_code',
                'content': value or 'z'
            },
            'vdiskin': lambda value: {
                'type': 'inline_code',
                'content': value or 'VDiskIn'
            },
            'postinlinewarnings': lambda value: {
                'type': 'inline_code',
                'content': value or 'postInlineWarnings'
            },
            'table': lambda value: {
                'type': 'inline_table',
                'content': value
            }
        }

        pattern = self._inline_open_pattern
        
        while position < text_length:
            match = pattern.search(text, position)
            if not match:
                # No more inline tags, append remaining text
                if position < text_length:
                    result.append({'type': 'text', 'content': text[position:]})
                break

            tag_name = match.group(1).lower()
            start_index = match.start()

            # Append text before the tag
            if start_index > position:
                result.append({'type': 'text', 'content': text[position:start_index]})

            # Skip matches that are part of anchors or paths (e.g., Foo#bar::)
            if start_index > 0:
                prev_char = text[start_index - 1]
                if prev_char in '#/.-:*':
                    result.append({'type': 'text', 'content': text[start_index:match.end()]})
                    position = match.end()
                    continue

            content_start = match.end()
            closing_index = text.find('::', content_start)

            if closing_index == -1:
                remainder = text[content_start:]
                if tag_name in self._special_inline_block_tags:
                    tag_value = remainder.strip()
                    result.append({
                        'type': 'pending_block',
                        'tag': tag_name,
                        'value': tag_value,
                        'line': line_number
                    })
                    position = len(text)
                    break
                if tag_name == 'keyword':
                    whitespace_match = re.match(r'\s*', remainder)
                    consumed = whitespace_match.end() if whitespace_match else 0
                    if consumed:
                        whitespace_text = remainder[:consumed]
                        if whitespace_text:
                            result.append({'type': 'text', 'content': whitespace_text})
                    trimmed = remainder[consumed:]
                    keyword_match = re.match(r'([^\s|]+)', trimmed)
                    if keyword_match:
                        value = keyword_match.group(1)
                        handler = inline_handlers.get(tag_name)
                        if handler:
                            result.append(handler(value))
                            position = content_start + consumed + keyword_match.end()
                            continue
                tag_value = remainder.strip()
                # No closing :: found - treat as unknown or malformed inline tag
                error_line = line_number if line_number is not None else self.current_line + 1
                if self.strict:
                    raise UnknownInlineTagError(tag_name, error_line, text)
                # Non-strict mode: treat the rest as text and exit loop
                result.append({'type': 'text', 'content': text[start_index:]})
                break

            tag_value = text[content_start:closing_index]
            position = closing_index + 2

            if tag_name in inline_handlers:
                handler = inline_handlers[tag_name]
                result.append(handler(tag_value))
            else:
                error_line = line_number if line_number is not None else self.current_line + 1
                if self.strict:
                    raise UnknownInlineTagError(tag_name, error_line, text)
                # In non-strict mode, keep the original text intact
                result.append({'type': 'text', 'content': text[start_index:position]})

        # Ensure we always return at least plain text
        if not result:
            result.append({'type': 'text', 'content': text})

        # Merge adjacent text nodes for cleanliness
        merged: List[Dict[str, Any]] = []
        for item in result:
            if item['type'] == 'text' and item.get('content') == '':
                continue
            if merged and merged[-1]['type'] == 'text' and item['type'] == 'text':
                merged[-1]['content'] += item['content']
            else:
                merged.append(item)

        return merged


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
