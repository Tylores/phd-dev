"""
Module 3: Semantic Linker & Knowledge Graph Exporter.
Analyses mined requirements and structural data, extracts key technical terms/concepts,
and exports a standardized Knowledge Graph JSON payload with Nodes and Edges.
Identifies parent-child containment, explicit references, and potential rule conflicts.
"""

import re
import logging
from collections import Counter

logger = logging.getLogger("SemanticLinker")
logger.setLevel(logging.INFO)

# List of common English stopwords to exclude from dynamic terminology extraction
STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'arent', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'cant', 'cannot', 'could',
    'couldnt', 'did', 'didnt', 'do', 'does', 'doesnt', 'doing', 'dont', 'down', 'during', 'each', 'few', 'for', 'from',
    'further', 'had', 'hadnt', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 'hes', 'her', 'here',
    'heres', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'hows', 'i', 'id', 'ill', 'im', 'ive', 'if', 'in',
    'into', 'is', 'isnt', 'it', 'its', 'itself', 'lets', 'll', 'me', 'more', 'most', 'mustnt', 'my', 'myself', 'no',
    'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out',
    'over', 'own', 're', 'same', 'shant', 'she', 'shed', 'shell', 'shes', 'shouldnt', 'so', 'some', 'such', 'than',
    'that', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'theres', 'these', 'they',
    'theyd', 'theyll', 'theyre', 'theyve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've',
    'very', 'was', 'wasnt', 'we', 'wed', 'well', 'were', 'weve', 'werent', 'what', 'whats', 'when', 'whens',
    'where', 'wheres', 'which', 'while', 'who', 'whos', 'whom', 'why', 'whys', 'with', 'wont', 'would', 'wouldnt',
    'you', 'youd', 'youll', 'youre', 'youve', 'your', 'yours', 'yourself', 'yourselves', 'will', 'shall', 'should',
    'may', 'must', 'can', 'could', 'would', 'shouldnt', 'mustnt', 'shallnt', 'definition', 'definitions', 'annex',
    'clause', 'section', 'paragraph', 'table', 'figure', 'document', 'documents', 'standard', 'standards', 'ieee'
}

# Curated IEEE standard technical terms with singular/plural regex support
CURATED_TERMS = {
    "timeout": re.compile(r'\btimeouts?\b', re.IGNORECASE),
    "heartbeat": re.compile(r'\bheartbeats?\b', re.IGNORECASE),
    "payload": re.compile(r'\bpayloads?\b', re.IGNORECASE),
    "register": re.compile(r'\bregisters?\b', re.IGNORECASE),
    "interface": re.compile(r'\binterfaces?\b', re.IGNORECASE),
    "device": re.compile(r'\bdevices?\b', re.IGNORECASE),
    "service": re.compile(r'\bservices?\b', re.IGNORECASE),
    "agreement": re.compile(r'\bagreements?\b', re.IGNORECASE),
    "protocol": re.compile(r'\bprotocols?\b', re.IGNORECASE),
    "client": re.compile(r'\bclients?\b', re.IGNORECASE),
    "server": re.compile(r'\bservers?\b', re.IGNORECASE),
    "security": re.compile(r'\bsecurity\b', re.IGNORECASE),
    "der": re.compile(r'\bders?\b', re.IGNORECASE),
    "voltage": re.compile(r'\bvoltages?\b', re.IGNORECASE),
    "frequency": re.compile(r'\bfrequenc(?:y|ies)\b', re.IGNORECASE),
    "power": re.compile(r'\bpowers?\b', re.IGNORECASE),
    "load": re.compile(r'\bloads?\b', re.IGNORECASE),
    "storage": re.compile(r'\bstorages?\b', re.IGNORECASE),
    "generation": re.compile(r'\bgenerations?\b', re.IGNORECASE),
    "inverter": re.compile(r'\binverters?\b', re.IGNORECASE),
    "connection": re.compile(r'\bconnections?\b', re.IGNORECASE),
    "capacity": re.compile(r'\bcapacities|capacity\b', re.IGNORECASE),
    "mtls": re.compile(r'\bmtls\b', re.IGNORECASE),
    "gateway": re.compile(r'\bgateways?\b', re.IGNORECASE),
    "telemetry": re.compile(r'\btelemetr(?:y|ies)\b', re.IGNORECASE)
}

# Regex to detect explicit cross-references to other sections/clauses
SECTION_REF_REGEX = re.compile(r'\b(?:[Ss]ection|[Cc]lause)\s+(\d+(?:\.\d+)*)\b')

# Regex to detect explicit cross-references to other requirements (e.g. "REQ-001")
REQ_REF_REGEX = re.compile(r'\b(REQ-\d+)\b')

class SemanticLinker:
    """
    Analyzes rule ledgers, extracts technical terms, establishes semantic relationships,
    and exports a Knowledge Graph representation.
    """
    def __init__(self, top_n_terms=20):
        self.top_n_terms = top_n_terms

    def build_knowledge_graph(self, rule_ledger, blocks):
        """
        Builds and returns a dictionary payload representing a Knowledge Graph (Nodes and Edges).
        """
        nodes = []
        edges = []
        
        # Track inserted nodes to avoid duplicates
        inserted_node_ids = set()
        
        # 1. Identify Section Titles
        section_titles = {}
        for block in blocks:
            if block["type"] == "heading":
                section_titles[block["section_number"]] = block["heading_context"][-1]
                
        # 2. Extract Terms (curated + dynamic high-frequency terms)
        extracted_terms = self._extract_terms(rule_ledger)
        
        # 3. Create Term Nodes
        term_patterns = {}
        for term, freq in extracted_terms.items():
            node_id = f"TERM-{term}"
            nodes.append({
                "id": node_id,
                "label": "Term",
                "properties": {
                    "name": term,
                    "frequency": freq
                }
            })
            inserted_node_ids.add(node_id)
            
            # Map term string to compile patterns for matching
            if term in CURATED_TERMS:
                term_patterns[term] = CURATED_TERMS[term]
            else:
                term_patterns[term] = re.compile(rf'\b{re.escape(term)}s?\b', re.IGNORECASE)
                
        # 4. Create Section Nodes and structural parent-child CONTAINS Edges
        # Pre-populate sections mentioned in ledger + headings
        sections_to_create = set()
        for block in blocks:
            sections_to_create.add(block["section_number"])
            for parent in block.get("parent_hierarchy", []):
                sections_to_create.add(parent)
        for rule in rule_ledger:
            sections_to_create.add(rule["section_number"])
            for parent in rule.get("parent_hierarchy", []):
                sections_to_create.add(parent)
                
        for sec in sorted(sections_to_create):
            if not sec or sec == "UNKNOWN":
                continue
            sec_id = f"SEC-{sec}"
            title = section_titles.get(sec, f"Section {sec}")
            
            nodes.append({
                "id": sec_id,
                "label": "Section",
                "properties": {
                    "section_number": sec,
                    "title": title
                }
            })
            inserted_node_ids.add(sec_id)
            
            # Structural containment edges: parent section contains child section
            # E.g. Parent of "2.1" is "2" (or "2.0")
            parts = sec.split('.')
            if len(parts) > 1:
                # Construct logical parent by removing the last digit
                parent_sec = '.'.join(parts[:-1])
                # If parent_sec is not in sections, try adding ".0"
                if parent_sec not in sections_to_create and f"{parent_sec}.0" in sections_to_create:
                    parent_sec = f"{parent_sec}.0"
                    
                if parent_sec in sections_to_create:
                    edges.append({
                        "source": f"SEC-{parent_sec}",
                        "target": sec_id,
                        "type": "CONTAINS",
                        "properties": {}
                    })

        # 5. Create Requirement Nodes and map relationship Edges
        term_to_reqs = {term: [] for term in term_patterns}
        
        for rule in rule_ledger:
            req_id = rule["id"]
            nodes.append({
                "id": req_id,
                "label": "Requirement",
                "properties": {
                    "text": rule["text"],
                    "constraint_type": rule["constraint_type"],
                    "section_number": rule["section_number"],
                    "page_number": rule["page_number"]
                }
            })
            inserted_node_ids.add(req_id)
            
            # Section -> CONTAINS -> Requirement Edge
            sec_id = f"SEC-{rule['section_number']}"
            if sec_id in inserted_node_ids:
                edges.append({
                    "source": sec_id,
                    "target": req_id,
                    "type": "CONTAINS",
                    "properties": {}
                })
                
            # Requirement -> REFERENCES -> Term Edges
            req_text = rule["text"]
            for term, pattern in term_patterns.items():
                if pattern.search(req_text):
                    term_id = f"TERM-{term}"
                    edges.append({
                        "source": req_id,
                        "target": term_id,
                        "type": "REFERENCES",
                        "properties": {
                            "context": "text_mention"
                        }
                    })
                    term_to_reqs[term].append(rule)
                    
            # Requirement -> REFERENCES -> Section Edges (explicit references like "refer to Section 4.2")
            sec_refs = SECTION_REF_REGEX.findall(req_text)
            for ref_sec in sec_refs:
                ref_sec_id = f"SEC-{ref_sec}"
                # If target section exists in graph, create reference link
                if ref_sec_id in inserted_node_ids:
                    edges.append({
                        "source": req_id,
                        "target": ref_sec_id,
                        "type": "REFERENCES",
                        "properties": {
                            "context": "explicit_section_ref"
                        }
                    })
                    
            # Requirement -> REFERENCES -> Requirement Edges (explicit references like "REQ-002")
            req_refs = REQ_REF_REGEX.findall(req_text)
            for ref_req in req_refs:
                if ref_req != req_id:  # Avoid self-referencing
                    edges.append({
                        "source": req_id,
                        "target": ref_req,
                        "type": "REFERENCES",
                        "properties": {
                            "context": "explicit_requirement_ref"
                        }
                    })
                    
        # 6. Detect Potential rule conflicts (CONFLICTS_WITH)
        # Standard: Requirement A (Mandatory/shall) and Requirement B (Prohibition/shall not)
        # share the same technical term.
        conflict_pairs = set()
        for term, reqs in term_to_reqs.items():
            if len(reqs) < 2:
                continue
                
            for idx1 in range(len(reqs)):
                for idx2 in range(idx1 + 1, len(reqs)):
                    r1 = reqs[idx1]
                    r2 = reqs[idx2]
                    
                    # Check for opposing constraints
                    t1, t2 = r1["constraint_type"], r2["constraint_type"]
                    is_opposing = (
                        (t1 == "Mandatory" and t2 == "Prohibition") or
                        (t1 == "Prohibition" and t2 == "Mandatory")
                    )
                    
                    if is_opposing:
                        pair_key = tuple(sorted([r1["id"], r2["id"]]))
                        if pair_key not in conflict_pairs:
                            conflict_pairs.add(pair_key)
                            edges.append({
                                "source": r1["id"],
                                "target": r2["id"],
                                "type": "CONFLICTS_WITH",
                                "properties": {
                                    "reason": f"Opposing compliance keywords ('{t1}' vs '{t2}') referencing common concept '{term}'",
                                    "shared_term": term
                                }
                            })
                            
        return {
            "nodes": nodes,
            "edges": edges
        }

    def _extract_terms(self, rule_ledger):
        """
        Identifies key technical terms dynamically by checking word frequencies,
        excluding standard stopwords, and merging with the curated list.
        """
        all_words = []
        for rule in rule_ledger:
            text = rule["text"].lower()
            # Tokenize alphabetical words with length >= 3
            words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
            filtered = [w for w in words if w not in STOPWORDS]
            all_words.extend(filtered)
            
        counter = Counter(all_words)
        
        # Grab high-frequency words
        dynamic_terms = [word for word, count in counter.most_common(self.top_n_terms)]
        
        # Merge curated list and dynamic list
        final_terms = {}
        for word in CURATED_TERMS:
            # Calculate occurrences in our token pool
            count = counter.get(word, 0)
            # Add plurals/variations check
            pattern = CURATED_TERMS[word]
            total_matches = sum(1 for rule in rule_ledger if pattern.search(rule["text"]))
            final_terms[word] = total_matches
            
        for d_word in dynamic_terms:
            if d_word not in final_terms:
                final_terms[d_word] = counter[d_word]
                
        # Sort terms by frequency
        sorted_terms = dict(sorted(final_terms.items(), key=lambda item: item[1], reverse=True))
        return sorted_terms
