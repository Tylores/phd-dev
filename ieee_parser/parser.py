"""
Module 1: Structural & Hierarchical Parser for PDF documents.
Extracts text from technical PDFs, cleans headers/footers/page numbers,
identifies headings, paragraphs, lists, and tables, and constructs
a structural hierarchy where every block inherits its parent context.
"""

import os
import re
import json
import pypdf

# Regex to match headings like:
# "1.0 Introduction to ESI"
# "4.1.2 Physical layer"
# "Annex A (informative) - Title"
# "A.1 General"
HEADING_REGEX = re.compile(
    r'^\s*('
    r'(?:Annex\s+[A-Z]\b\.?\s*)?'       # Optional "Annex A"
    r'(?:\d+(?:\.\d+)+|\d+|\b[A-Z](?:\.\d+)*)'  # "1.0", "1", "A.1.2"
    r')\.?\s+([A-Z\d_].*)$'             # Heading title starting with uppercase/digit
)

# Regex to match list items like "• Bullet", "1) First", "a. Item"
LIST_PREFIX_REGEX = re.compile(
    r'^\s*('
    r'•|[*+-]|'                         # Bullet points
    r'\b\d+[\b\.)]|'                    # 1. or 1)
    r'\b[a-zA-Z][\b\.)]|'               # a. or a) or A. or A)
    r'\(\d+\)|\([a-zA-Z]\)'             # (1) or (a)
    r')\s+(.*)$'
)

def normalize_section(sec_num):
    """
    Normalizes section numbers by removing trailing zeros.
    E.g., "1.0" -> "1", "2.0.0" -> "2", "2.1.0" -> "2.1"
    This facilitates proper hierarchical prefix matching.
    """
    parts = sec_num.split('.')
    while len(parts) > 1 and parts[-1] == '0':
        parts.pop()
    return '.'.join(parts)

def is_table_row(line):
    """
    Heuristic to check if a line represents a table row.
    Detects column separators like '|' or multiple spaces (3 or more) separating words.
    """
    line_strip = line.strip()
    if '|' in line_strip:
        return True
    # Look for at least one gap of 3+ spaces separating non-space elements
    parts = re.split(r'\s{3,}', line_strip)
    return len(parts) >= 2 and all(len(p) > 0 for p in parts)

def clean_page_lines(lines):
    """
    Filters out headers, footers, and page numbers from a list of page lines.
    Maintains empty lines as they act as block separators.
    """
    cleaned = []
    for idx, line in enumerate(lines):
        line_str = line.strip()
        if not line_str:
            cleaned.append("")
            continue
            
        # Check if line consists solely of a page number (digits or Roman numerals)
        if re.match(r'^(?:\d+|[ivxldcmIVXLDCM]+)$', line_str):
            # Page numbers are usually at the very top (start) or bottom (end) of the page text
            if idx <= 2 or idx >= len(lines) - 3:
                continue
                
        # Check for common running headers/footers
        lower_line = line_str.lower()
        if "energy services interface" in lower_line or "ieee std" in lower_line or "prepared by" in lower_line:
            if idx <= 2 or idx >= len(lines) - 3:
                continue
                
        cleaned.append(line)
    return cleaned

class PDFParser:
    """
    Extracts text from PDF and parses it into a structural hierarchy of blocks.
    """
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
            
    def parse(self):
        """
        Parses the PDF page by page, cleans noise, and builds structured blocks.
        """
        pages_lines_and_types = []
        
        try:
            reader = pypdf.PdfReader(self.pdf_path)
            for page_idx, page in enumerate(reader.pages):
                page_num = page_idx + 1
                text = page.extract_text()
                if not text:
                    continue
                
                raw_lines = text.split('\n')
                cleaned_lines = clean_page_lines(raw_lines)
                
                for line in cleaned_lines:
                    line_str = line.strip()
                    if not line_str:
                        pages_lines_and_types.append((page_num, "", "empty", None))
                        continue
                    
                    # Match Heading
                    heading_match = HEADING_REGEX.match(line_str)
                    if heading_match:
                        groups = heading_match.groups()
                        pages_lines_and_types.append((page_num, line_str, "heading", groups))
                        continue
                    
                    # Match List
                    list_match = LIST_PREFIX_REGEX.match(line_str)
                    if list_match:
                        groups = list_match.groups()
                        pages_lines_and_types.append((page_num, line_str, "list_item", groups))
                        continue
                    
                    # Match Table
                    if is_table_row(line_str):
                        pages_lines_and_types.append((page_num, line_str, "table_row", None))
                        continue
                    
                    # Fallback to normal text
                    pages_lines_and_types.append((page_num, line_str, "text", None))
                    
        except Exception as e:
            raise RuntimeError(f"Error reading PDF page contents: {str(e)}")
            
        return self._assemble_blocks(pages_lines_and_types)

    def _assemble_blocks(self, lines_info):
        """
        Assembles lines into paragraphs, list items, tables, and headings,
        resolving the active hierarchy and parent context.
        """
        blocks = []
        current_block = None
        
        # Hierarchy state
        active_sections = {}  # normalized_sec_num -> (original_sec_num, heading_title)
        current_section = "0.0"
        current_parents = []
        current_context = ["Document Root"]
        
        block_id_counter = 1
        
        for page_num, line_str, line_type, groups in lines_info:
            if line_type == "empty":
                # Flush the current paragraph/list item to start a new block
                if current_block:
                    blocks.append(current_block)
                    current_block = None
                continue
                
            if line_type == "heading":
                if current_block:
                    blocks.append(current_block)
                    current_block = None
                    
                section_number = groups[0]
                heading_title = groups[1]
                
                # Normalize and update the hierarchy path
                norm = normalize_section(section_number)
                active_sections[norm] = (section_number, heading_title)
                
                # Deactivate sections that are not ancestors of the current heading
                for k in list(active_sections.keys()):
                    if not (norm.startswith(k + '.') or norm == k):
                        del active_sections[k]
                
                # Reconstruct parent hierarchy and heading context
                parts = norm.split('.')
                parent_hierarchy = []
                heading_context = []
                for i in range(1, len(parts)):
                    parent_prefix = '.'.join(parts[:i])
                    if parent_prefix in active_sections:
                        parent_hierarchy.append(active_sections[parent_prefix][0])
                        heading_context.append(active_sections[parent_prefix][1])
                
                heading_context.append(heading_title)
                
                current_section = section_number
                current_parents = parent_hierarchy
                current_context = heading_context
                
                # Headings are saved as structured blocks
                blocks.append({
                    "id": f"BLK-{block_id_counter:04d}",
                    "type": "heading",
                    "text": f"{section_number} {heading_title}",
                    "section_number": current_section,
                    "parent_hierarchy": current_parents,
                    "heading_context": current_context,
                    "page_number": page_num
                })
                block_id_counter += 1
                
            elif line_type == "list_item":
                if current_block:
                    blocks.append(current_block)
                    
                prefix = groups[0]
                content = groups[1]
                current_block = {
                    "id": f"BLK-{block_id_counter:04d}",
                    "type": "list_item",
                    "prefix": prefix,
                    "text": content,
                    "section_number": current_section,
                    "parent_hierarchy": current_parents,
                    "heading_context": current_context,
                    "page_number": page_num
                }
                block_id_counter += 1
                
            elif line_type == "table_row":
                if current_block and current_block["type"] != "table":
                    blocks.append(current_block)
                    current_block = None
                    
                if current_block is None:
                    current_block = {
                        "id": f"BLK-{block_id_counter:04d}",
                        "type": "table",
                        "rows": [line_str],
                        "text": line_str,
                        "section_number": current_section,
                        "parent_hierarchy": current_parents,
                        "heading_context": current_context,
                        "page_number": page_num
                    }
                    block_id_counter += 1
                else:
                    current_block["rows"].append(line_str)
                    current_block["text"] += "\n" + line_str
                    
            else:  # Normal text
                if current_block is None:
                    current_block = {
                        "id": f"BLK-{block_id_counter:04d}",
                        "type": "paragraph",
                        "text": line_str,
                        "section_number": current_section,
                        "parent_hierarchy": current_parents,
                        "heading_context": current_context,
                        "page_number": page_num
                    }
                    block_id_counter += 1
                elif current_block["type"] == "paragraph":
                    # Append text to active paragraph
                    current_block["text"] += " " + line_str
                elif current_block["type"] == "list_item":
                    # Append text to active list item
                    current_block["text"] += " " + line_str
                elif current_block["type"] == "table":
                    # Close table and start new paragraph
                    blocks.append(current_block)
                    current_block = {
                        "id": f"BLK-{block_id_counter:04d}",
                        "type": "paragraph",
                        "text": line_str,
                        "section_number": current_section,
                        "parent_hierarchy": current_parents,
                        "heading_context": current_context,
                        "page_number": page_num
                    }
                    block_id_counter += 1
                    
        if current_block:
            blocks.append(current_block)
            
        # Post-process to clean up duplicate spaces in paragraphs/lists
        for block in blocks:
            if block["type"] in ["paragraph", "list_item"]:
                block["text"] = re.sub(r'\s+', ' ', block["text"]).strip()
                
        return blocks

def build_hierarchy_tree(blocks):
    """
    Transforms the flat list of blocks into a nested tree structure.
    """
    root = {
        "title": "Document Root",
        "section": "0.0",
        "type": "root",
        "children": [],
        "content": []
    }
    
    path_map = {"": root}
    
    for block in blocks:
        if block["type"] == "heading":
            sec_num = block["section_number"]
            norm = normalize_section(sec_num)
            
            # Extract heading title
            title = block["text"].split(maxsplit=1)[1] if ' ' in block["text"] else block["text"]
            
            node = {
                "title": title,
                "section": sec_num,
                "type": "section",
                "children": [],
                "content": []
            }
            
            # Find the closest active parent in path_map
            parts = norm.split('.')
            parent_node = root
            for i in range(len(parts) - 1, 0, -1):
                parent_prefix = '.'.join(parts[:i])
                if parent_prefix in path_map:
                    parent_node = path_map[parent_prefix]
                    break
                    
            parent_node["children"].append(node)
            path_map[norm] = node
        else:
            sec_num = block["section_number"]
            norm = normalize_section(sec_num)
            
            parts = norm.split('.')
            target_node = root
            for i in range(len(parts), 0, -1):
                prefix = '.'.join(parts[:i])
                if prefix in path_map:
                    target_node = path_map[prefix]
                    break
                    
            target_node["content"].append(block)
            
    return root

def _tree_to_markdown_lines(node, depth=1):
    lines = []
    if node["type"] == "section":
        hashes = "#" * min(depth, 6)
        lines.append(f"{hashes} {node['section']} {node['title']}\n")
        
    for block in node["content"]:
        if block["type"] == "paragraph":
            lines.append(f"{block['text']}\n")
        elif block["type"] == "list_item":
            prefix = block.get("prefix", "-")
            lines.append(f"{prefix} {block['text']}\n")
        elif block["type"] == "table":
            lines.append(f"```\n{block['text']}\n```\n")
            
    for child in node["children"]:
        lines.extend(_tree_to_markdown_lines(child, depth + 1))
        
    return lines

def tree_to_markdown(tree):
    """
    Converts a nested hierarchy tree to a human-readable Markdown string.
    """
    md_parts = []
    for child in tree["children"]:
        md_parts.extend(_tree_to_markdown_lines(child, depth=1))
        md_parts.append("\n")
    return "\n".join(md_parts).strip()
