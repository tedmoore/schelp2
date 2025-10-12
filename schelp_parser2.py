import argparse
import re

BLOCK_TAGS = [
    "section",
    "subsection",
    "subsubsection",
    "code",
    "note",
    "title",
    "summary",
    "categories",
    "list",
    "numberedlist",
    "definitionlist",
    "table",
    "method",
    "classmethods",
    "copymethod",
    "warning",
    "private",
    "instancemethods",
    "class",
    "examples"
]
    
INLINE_TAGS = [
    "emphasis",
    "link",
    "strong",
    "code",
    "math",
    "teletype"
]

def get_blocks(content: str) -> list:
    blocks = []
    
    previous_block_start = None
    previous_block_tag = None
    
    for i, line in enumerate(content):
        # Strip the line first to check for block tags regardless of indentation
        result = re.match(r'^([A-Za-z0-9]+)::', line.strip(), re.IGNORECASE)
        if result:
            tag = result.group(1).lower()
            
            if tag in BLOCK_TAGS:
                if previous_block_start is not None:
                    block_content = content[previous_block_start:i]
                    # print(f"{previous_block_tag} from line {previous_block_start+1} with {len(block_content)} lines")
                    blocks.append((previous_block_tag, block_content))
                previous_block_start = i
                previous_block_tag = tag
    
    # Don't forget the last block
    if previous_block_start is not None:
        block_content = content[previous_block_start:]
        # print(f"{previous_block_tag} from line {previous_block_start+1} with {len(block_content)} lines")
        blocks.append((previous_block_tag, block_content))
            
    return blocks

def parse_for_inline_tags(text: str) -> list:
    if not text:
        return []
    
    result = []
    position = 0
    text_length = len(text)
    
    tag_pattern = r'([A-Za-z0-9]+)::'
    while position < text_length:
        match = re.search(tag_pattern, text[position:], re.IGNORECASE)
        if match:
            tag = match.group(1).lower()
            if tag in INLINE_TAGS:
                start = position + match.start()
                end = position + match.end()
                
                # Add preceding text as a plain text item
                if start > position:
                    result.append({"type": "text", "content": text[position:start]})
                
                # Find the end of the inline tag content
                content_start = end
                content_end = text.find('::', content_start)
                if content_end == -1:
                    content_end = text_length
                
                content = text[content_start:content_end].strip()
                
                # Recursively parse inline tags within this tag's content
                if content:
                    parsed_content = parse_for_inline_tags(content)
                    result.append({"type": tag, "content": parsed_content})
                else:
                    result.append({"type": tag, "content": content})
                
                position = content_end + 2
                
            else:
                # Not an inline tag, skip it (it's probably a block tag reference)
                position = position + match.end()
            
        else:
            # No more tags found, add the rest of the text
            if position < text_length:
                result.append({"type": "text", "content": text[position:]})
            break
    
    return result

def parse_title_block(lines: list) -> dict:
    if lines and len(lines) > 0:
        title_line = lines[0]
        title = title_line.split("::",1)[1].strip()
        return {"type": "title", "title": title}
    return {"type": "title", "title": "No Title"}

def parse_section_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "section", "content": content}

def parse_subsection_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "subsection", "content": content}

def parse_subsubsection_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    return {"type": "subsubsection", "content": content}

def parse_code_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    # note: code has a closing ::
    return {"type": "code", "content": content}

def parse_note_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    return {"type": "note", "content": content}

def parse_summary_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    return {"type": "summary", "content": content}

def parse_categories_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    return {"type": "categories", "content": content}

def parse_list_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    # note: list has a closing ::
    return {"type": "list", "content": content}

def parse_numberedlist_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    # note: numberedlist has a closing ::
    return {"type": "numberedlist", "content": content}

def parse_definitionlist_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    # note: definitionlist has a closing ::
    return {"type": "definitionlist", "content": content}

def parse_table_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    # note: table has a closing ::
    return {"type": "table", "content": content}

def parse_method_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    return {"type": "method", "content": content}

def parse_classmethods_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    return {"type": "classmethods", "content": content}

def parse_copymethod_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    return {"type": "copymethod", "content": content}

def parse_warning_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    # note: warning has a closing ::
    return {"type": "warning", "content": content}

def parse_private_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    return {"type": "private", "content": content}

def parse_instancemethods_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    return {"type": "instancemethods", "content": content}

def parse_math_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    # note: math has a closing ::
    return {"type": "math", "content": content}

def parse_examples_block(lines: list) -> dict:
    # treat examples like a section
    return {"type": "section", "content": "Examples:"}

BLOCK_PARSERS = {
    "title": parse_title_block,
    "class": parse_title_block, # treat class like a title
    "section": parse_section_block,
    "subsection": parse_subsection_block,
    "subsubsection": parse_subsubsection_block,
    "code": parse_code_block,
    "note": parse_note_block,
    "summary": parse_summary_block,
    "categories": parse_categories_block,
    "list": parse_list_block,
    "numberedlist": parse_numberedlist_block,
    "definitionlist": parse_definitionlist_block,
    "table": parse_table_block,
    "method": parse_method_block,
    "classmethods": parse_classmethods_block,
    "copymethod": parse_copymethod_block,
    "warning": parse_warning_block,
    "private": parse_private_block,
    "instancemethods": parse_instancemethods_block,
    "math": parse_math_block,
    "examples": parse_examples_block,
}

def parse_file(input_file: str, output_file: str):
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().splitlines()

    blocks = get_blocks(content)

    parsed_blocks = [BLOCK_PARSERS[b[0]](b[1]) for b in blocks]

    # for pb in parsed_blocks:
    #     print(pb)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',help='input .schelp file'
    )
    parser.add_argument(
       '--json', help='output .json file', default=None
    )
    args = parser.parse_args()
    parse_file(args.i, args.json)