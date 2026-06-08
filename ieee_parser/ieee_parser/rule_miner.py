"""
Module 2: Deterministic Rule Mining Engine.
Extracts sentences containing compliance keywords ("shall", "should", "may", "must", "shall not")
from structured blocks and classifies them into structured compliance rules.
Handles missing/invalid section numbers and sentence boundaries with robust heuristics.
"""

import re
import logging

# Configure local logger for rule mining engine
logger = logging.getLogger("RuleMiner")
logger.setLevel(logging.INFO)

# Regex to match potential sentence boundaries: punctuation + optional closing quote,
# followed by spacing, followed by a capital letter/quote/parenthesis.
# This avoids look-behinds completely.
BOUNDARY_REGEX = re.compile(r'([.!?]["\'”’\)]?)\s+(["\'“‘\(]?[A-Z])')

# Pattern to check if the text preceding the punctuation ends in a common abbreviation
# or a single letter/digit (e.g. section number or list prefix).
ABBREVIATION_PATTERN = re.compile(
    r'\b(?:e\.g|i\.e|vs|std|fig|no|approx|ref|et\s+al|[A-Za-z]|\d)$',
    re.IGNORECASE
)

# Rule keyword definitions with word boundaries
RULE_PATTERNS = {
    "Prohibition": [
        re.compile(r'\bshall\s+not\b', re.IGNORECASE),
        re.compile(r'\bmust\s+not\b', re.IGNORECASE),
        re.compile(r'\bshould\s+not\b', re.IGNORECASE)
    ],
    "Mandatory": [
        re.compile(r'\bshall\b', re.IGNORECASE),
        re.compile(r'\bmust\b', re.IGNORECASE)
    ],
    "Recommendation": [
        re.compile(r'\bshould\b', re.IGNORECASE)
    ],
    "Permission": [
        re.compile(r'\bmay\b', re.IGNORECASE)
    ]
}

def split_sentences(text):
    """
    Splits a paragraph block into individual sentences using a robust index-based logic
    that filters out common abbreviations and decimal numbers.
    """
    if not text:
        return []
        
    # Replace newlines with spaces for sentence processing
    text_clean = text.replace('\n', ' ')
    
    sentences = []
    start_idx = 0
    
    for match in BOUNDARY_REGEX.finditer(text_clean):
        # Text leading up to the punctuation mark of this boundary candidate
        preceding_text = text_clean[start_idx : match.start(1)].strip()
        
        # Check if the preceding text ends with an abbreviation or single letter/digit
        if ABBREVIATION_PATTERN.search(preceding_text):
            continue
            
        # Found a valid sentence boundary
        sentence = text_clean[start_idx : match.end(1)].strip()
        sentences.append(sentence)
        
        # Next sentence starts at the capital letter/quote/paren
        start_idx = match.start(2)
        
    # Append any remaining text
    remaining = text_clean[start_idx:].strip()
    if remaining:
        sentences.append(remaining)
        
    return sentences

class RuleMiner:
    """
    Scans structured blocks, extracts compliance rules, and generates a rule ledger.
    """
    def __init__(self, start_id=1):
        self.req_counter = start_id
        self.last_valid_section = "UNKNOWN"

    def mine_rules(self, blocks):
        """
        Sweeps structured blocks line-by-line / sentence-by-sentence and extracts matching requirements.
        """
        ledger = []
        
        for block_idx, block in enumerate(blocks):
            # Verify and handle section number issues
            section_number = block.get("section_number")
            if not section_number or section_number == "0.0" or section_number.strip() == "":
                # Fallback to the last known valid section, or use "UNKNOWN"
                section_number = self.last_valid_section
                logger.warning(
                    f"Block {block.get('id', block_idx)} has missing or invalid section number. "
                    f"Falling back to: '{section_number}'"
                )
            else:
                self.last_valid_section = section_number
                
            # Skip heading blocks as they don't contain requirement statements
            if block.get("type") == "heading":
                continue
                
            block_text = block.get("text", "")
            if not block_text:
                continue
                
            # Split paragraph/list/table into individual sentences
            sentences = split_sentences(block_text)
            
            for sentence in sentences:
                try:
                    matched_constraints = self._analyze_sentence(sentence)
                    if matched_constraints:
                        # Determine dominant constraint type
                        # Precedence: Prohibition > Mandatory > Recommendation > Permission
                        dominant_type = "Permission"
                        for c_type in ["Prohibition", "Mandatory", "Recommendation"]:
                            if c_type in matched_constraints:
                                dominant_type = c_type
                                break
                                
                        req_id = f"REQ-{self.req_counter:03d}"
                        self.req_counter += 1
                        
                        rule_obj = {
                            "id": req_id,
                            "section_number": section_number,
                            "parent_hierarchy": block.get("parent_hierarchy", []),
                            "heading_context": block.get("heading_context", []),
                            "constraint_type": dominant_type,
                            "all_matched_constraints": matched_constraints,
                            "text": sentence,
                            "source_block_id": block.get("id"),
                            "page_number": block.get("page_number")
                        }
                        ledger.append(rule_obj)
                        
                except Exception as e:
                    logger.error(
                        f"Error parsing text line for rules in block {block.get('id')}: {str(e)}. "
                        f"Line text: '{sentence[:50]}...'"
                    )
                    
        return ledger

    def _analyze_sentence(self, sentence):
        """
        Checks a sentence for compliance keywords and returns all matched constraint types.
        """
        matches = []
        for c_type, patterns in RULE_PATTERNS.items():
            for pattern in patterns:
                if pattern.search(sentence):
                    matches.append(c_type)
                    break  # Found match for this constraint category, move to next category
        return matches
