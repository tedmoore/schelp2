import argparse
import re
import json

# keep in alphabetical order (just for convenience)
BLOCK_TAGS = [
    "argument",
    "categories",
    "class",
    "classmethods",
    "code",
    "copymethod",
    "definitionlist",
    "description",
    "examples",
    "instancemethods",
    "list",
    "method",
    "note",
    "numberedlist",
    "private",
    "related",
    "section",
    "subsection",
    "subsubsection",
    "summary",
    "table",
    "title",
    "warning"
]

# keep in alphabetical order (just for convenience)
INLINE_TAGS = [
    "anchor",
    "code",
    "emphasis",
    "footnote",
    "link",
    "math",
    "strong",
    "teletype"
]

def parse_for_blocks(content: str) -> dict:
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
                # if content:
                #     parsed_content = parse_for_inline_tags(content)
                #     result.append({"type": tag, "content": parsed_content})
                # else:
                #     result.append({"type": tag, "content": content})
                
                result.append({"type": tag, "content": content})
                
                position = content_end + 2
                
            else:
                if tag not in BLOCK_TAGS: 
                    print(f"Warning: Unknown inline tag '{tag}' found.")
                position = position + match.end()
            
        else:
            # No more tags found, add the rest of the text
            if position < text_length:
                result.append({"type": "text", "content": text[position:]})
            break
    
    return result

def remove_closing_colons(text: str) -> str:
    return text.rsplit("::", 1)[0].strip()

def remove_opening_tag(tag: str, text: str) -> str:
    pattern = rf'^{tag}::'
    return re.sub(pattern, '', text, flags=re.IGNORECASE).strip()

def parse_title_block(lines: list) -> dict:
    if lines and len(lines) > 0:
        title_line = lines[0]
        title = title_line.split("::",1)[1].strip()
        return {"type": "title", "content": title}
    return {"type": "title", "content": "No Title"}

def parse_section_block(lines: list) -> dict:
    title = lines[0].split("::", 1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "section", "title": title, "content": content}

def parse_subsection_block(lines: list) -> dict:
    title = lines[0].split("::", 1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "subsection", "title": title, "content": content}

def parse_subsubsection_block(lines: list) -> dict:
    title = lines[0].split("::", 1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "subsubsection", "title": title, "content": content}

def parse_code_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    # code has a closing ::
    content = remove_closing_colons(content)
    return {"type": "code", "content": content}

def parse_note_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    # Remove the opening NOTE:: tag
    content = remove_opening_tag('note', content)
    content = remove_closing_colons(content)  # Remove closing :: if present
    content = parse_for_inline_tags(content)
    return {"type": "note", "content": content}

def parse_summary_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_opening_tag('summary', content)
    content = parse_for_inline_tags(content)
    return {"type": "summary", "content": content}

def parse_categories_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = remove_opening_tag('categories', content)
    content = content.split(",")
    content = [c.strip() for c in content if c.strip()]
    return {"type": "categories", "content": content}

def list_parse(text: str) -> list:
    items = text.split("##")
    items = [item.strip() for item in items if item.strip()]
    parsed_items = [parse_for_inline_tags(item) for item in items]
    return parsed_items

def parse_list_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('list', content)
    content = list_parse(content)
    return {"type": "list", "content": content}

def parse_numberedlist_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('numberedlist', content)
    content = list_parse(content)
    return {"type": "numberedlist", "content": content}

def parse_definition_list_item(item: str) -> dict:
    parts = item.split("||", 1)
    if len(parts) == 2:
        term = parts[0].strip()
        definition = parts[1].strip()
        term = parse_for_inline_tags(term)
        definition = parse_for_inline_tags(definition)
        return {"term": term, "definition": definition}
    else:
        term = item.strip()
        term = parse_for_inline_tags(term)
        return {"term": term, "definition": []}
    
def parse_definitionlist_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('definitionlist', content)
    items = content.split("##")
    items = [item.strip() for item in items if item.strip()]
    parsed_items = [parse_definition_list_item(item) for item in items]
    return {"type": "definitionlist", "content": parsed_items}

def parse_table_row(row: str) -> list:
    cells = row.split("||")
    cells = [cell.strip() for cell in cells if cell.strip()]
    cells = [parse_for_inline_tags(cell) for cell in cells]
    return cells

def parse_table_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('table', content)
    rows = content.split("##")
    rows = [row.strip() for row in rows if row.strip()]
    table = [parse_table_row(row) for row in rows]
    return {"type": "table", "content": table}

def parse_method_block(lines: list) -> dict:
    name = lines[0].split("::",1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    return {"type": "method", "name": name, "content": content}

def parse_classmethods_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_opening_tag('classmethods', content)
    content = parse_for_inline_tags(content)
    return {"type": "classmethods", "content": content}

def parse_copymethod_block(lines: list) -> dict:
    # TODO
    content = "[TODO: COPYMETHOD]\n".join(lines).strip()
    return {"type": "copymethod", "content": content}

def parse_warning_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('warning', content)
    content = parse_for_inline_tags(content)
    return {"type": "warning", "content": content}

def parse_private_block(lines: list) -> dict:
    # private method
    name = lines[0].split("::",1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    return {"type": "private", "name": name, "content": content}

def parse_instancemethods_block(lines: list) -> dict:
    content = "\n".join(lines).strip()
    content = remove_opening_tag('instancemethods', content)
    content = parse_for_inline_tags(content)
    return {"type": "instancemethods", "content": content}

def parse_math_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = remove_closing_colons(content)
    content = remove_opening_tag('math', content)
    # TODO: parse math, or let, it be raw LaTeX for Sphinx to handle?
    return {"type": "math", "content": content}

def parse_examples_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = remove_opening_tag('examples', content)
    content = parse_for_inline_tags(content)
    return {"type": "examples", "content": content}

def parse_related_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = remove_opening_tag('related', content)
    content = content.split(",")
    content = [c.strip() for c in content if c.strip()]
    return {"type": "related", "content": content}

def parse_argument_block(lines: list) -> dict:
    name = lines[0].split("::",1)[1].strip()
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "argument", "name": name, "content": content}

def parse_description_block(lines: list) -> dict:
    content = "\n".join(lines[1:]).strip()
    content = parse_for_inline_tags(content)
    return {"type": "description", "content": content}

# keep in alphabetical order (just for convenience)
BLOCK_PARSERS = {
    "argument": parse_argument_block,
    "categories": parse_categories_block,
    "class": parse_title_block, # treat class like a title
    "classmethods": parse_classmethods_block,
    "code": parse_code_block,
    "copymethod": parse_copymethod_block,
    "definitionlist": parse_definitionlist_block,
    "description": parse_description_block,
    "examples": parse_examples_block,
    "instancemethods": parse_instancemethods_block,
    "list": parse_list_block,
    "math": parse_math_block,
    "method": parse_method_block,
    "note": parse_note_block,
    "numberedlist": parse_numberedlist_block,
    "private": parse_private_block,
    "related": parse_related_block,
    "section": parse_section_block,
    "subsection": parse_subsection_block,
    "subsubsection": parse_subsubsection_block,
    "summary": parse_summary_block,
    "table": parse_table_block,
    "title": parse_title_block,
    "warning": parse_warning_block
}

def parse_file(input_file: str, output_file: str):
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # note is not allowed to be in-line...
    content = re.sub(r'([^\n])(note::)', r'\1\n\2', content, flags=re.IGNORECASE)
    content = content.splitlines()
    
    blocks = parse_for_blocks(content)
    parsed_blocks = [BLOCK_PARSERS[b[0]](b[1]) for b in blocks]
    
    # data structure with defaults
    doc = {
        "source_file": input_file,
        "metadata": {
            "title": "No title provided.",
            "summary": "No summary provided.",
            "categories": [],
            "related": [],
            "description": "No description provided."
        },
        "content": []
    }
    
    for pb in parsed_blocks:
        if pb["type"] == "title":
            doc["metadata"]["title"] = pb["content"]
        elif pb["type"] == "summary":
            doc["metadata"]["summary"] = pb["content"]
        elif pb["type"] == "categories":
            doc["metadata"]["categories"] = pb["content"]
        elif pb["type"] == "related":
            doc["metadata"]["related"] = pb["content"]
        elif pb["type"] == "description":
            doc["metadata"]["description"] = pb["content"]
        else:
            doc["content"].append(pb)
    
    # Add arguments list to methods and private methods
    # I've decided not to nest argument blocks inside method blocks
    # in this data structure because there might be code or note
    # blocks in between, and it would complicate the parsing logic.
    # Instead, we will look for argument blocks that immediately
    # follow method or private blocks and associate them accordingly
    # in an "arguments" property of the method
    # so that later they can be compared 
    # against the json built from the
    # sc class library to check for any discrepancies.
    for i, item in enumerate(doc["content"]):
        if item["type"] in ["method", "private"]:
            # Initialize arguments list
            item["arguments"] = []
            
            # Look ahead for argument blocks that follow this method
            j = i + 1
            while j < len(doc["content"]):
                if doc["content"][j]["type"] == "argument":
                    item["arguments"].append(doc["content"][j]["name"])
                    j += 1
                elif doc["content"][j]["type"] in ["method", "private", "section", "subsection", "subsubsection", "classmethods", "instancemethods"]:
                    # Hit another major block, stop collecting arguments
                    break
                else:
                    # Skip other blocks (note, code, etc.) but keep looking
                    j += 1
            
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(doc, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',help='input .schelp file'
    )
    parser.add_argument(
       '--json', help='output .json file', default=None
    )
    args = parser.parse_args()
    
    missing_parsers = set(BLOCK_TAGS) - set(BLOCK_PARSERS.keys())
    if missing_parsers:
        print(f"Warning: Missing parsers for block tags: {missing_parsers}")
        exit()
    
    parse_file(args.i, args.json)