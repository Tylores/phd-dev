"""
Module 4: Agentic Auditing Skeleton.
Provides an interface to query the Knowledge Graph for a requirement, term, or section,
gather all structurally and semantically linked nodes, and format a markdown payload
prepped with an expert-level system prompt ready for LLM critique.
"""

import json
import logging

logger = logging.getLogger("Auditor")
logger.setLevel(logging.INFO)

AUDIT_PROMPT_TEMPLATE = """You are an expert Systems Architect and Senior Security Engineer specializing in smart grid communications, mTLS security, and IEEE 2030.5 / SEP 2 protocol implementation.

Your task is to audit the selected requirement(s) extracted from a dense technical standard, analyzing them for semantic consistency, ambiguity, and implementation feasibility.

================================================================================
1. TARGET REQUIREMENT(S) TO AUDIT
================================================================================
{target_requirements}

================================================================================
2. HIERARCHICAL & STRUCTURAL CONTEXT
================================================================================
{structural_context}

================================================================================
3. SEMANTICALLY & STRUCTURALLY LINKED RULES
================================================================================
{linked_rules}

================================================================================
4. KEY CONCEPTS & TERMS INVOLVED
================================================================================
{referenced_terms}

================================================================================
5. AUTOMATICALLY FLAGGED POTENTIAL CONFLICTS
================================================================================
{potential_conflicts}

================================================================================
CRITIQUE INSTRUCTIONS FOR THE LLM AUDITOR:
================================================================================
Perform a rigorous, production-grade critique covering the following areas:

1. **Ambiguity & Testability Analysis**:
   - Assess if the requirement uses vague words (e.g., "appropriate", "efficient", "rapidly") without defining quantitative metrics or ranges.
   - Determine if the requirement can be verified via automated conformance testing.

2. **Logical Consistency & Conflict Resolution**:
   - Evaluate the target requirement against the linked rules and potential conflicts.
   - Identify contradictions (e.g., a "shall" contradicting a "shall not" or "may" on the same term in a different section).
   - Pinpoint gaps or omissions in the surrounding context.

3. **Smart Grid & IEEE 2030.5 Protocol Feasibility**:
   - Discuss how this requirement affects system state machines, transaction integrity, transport security (mTLS), messaging latency, or payloads (e.g., XML/EXI structures in IEEE 2030.5).
   - Highlight potential race conditions, timing failures (timeouts, heartbeats), or security vulnerabilities introduced by this specification.

4. **Proposed Revisions**:
   - Draft a revised version of the target requirement(s) that removes all ambiguities and resolves any identified contradictions.
   - Provide concrete, deterministic, and clear language.
"""

class RequirementAuditor:
    """
    Traverses the knowledge graph to extract context for a specific query
    and compiles the audit prompt payload.
    """
    def __init__(self, knowledge_graph):
        self.kg = knowledge_graph
        self.nodes = {n["id"]: n for n in knowledge_graph.get("nodes", [])}
        
        # Build index of edges for fast traversal
        self.out_edges = {}
        self.in_edges = {}
        for edge in knowledge_graph.get("edges", []):
            src, tgt = edge["source"], edge["target"]
            self.out_edges.setdefault(src, []).append(edge)
            self.in_edges.setdefault(tgt, []).append(edge)

    def query_context(self, query):
        """
        Queries the knowledge graph by requirement ID (e.g. 'REQ-001'),
        term name (e.g. 'heartbeat'), or section number (e.g. '2.0').
        Returns a dictionary containing target nodes and all relevant linked items.
        """
        query_strip = query.strip()
        target_nodes = []
        
        # 1. Resolve query to nodes
        if query_strip in self.nodes:
            target_nodes.append(self.nodes[query_strip])
        else:
            # Try matching Term name (e.g. TERM-termname) or Section number (e.g. SEC-secnum)
            term_id = f"TERM-{query_strip.lower()}"
            sec_id = f"SEC-{query_strip}"
            if term_id in self.nodes:
                target_nodes.append(self.nodes[term_id])
            elif sec_id in self.nodes:
                target_nodes.append(self.nodes[sec_id])
            else:
                # Try partial match on term names or sections
                for n_id, node in self.nodes.items():
                    label = node.get("label")
                    props = node.get("properties", {})
                    if label == "Term" and props.get("name", "").lower() == query_strip.lower():
                        target_nodes.append(node)
                    elif label == "Section" and props.get("section_number") == query_strip:
                        target_nodes.append(node)
                        
        if not target_nodes:
            logger.warning(f"No node matching query '{query}' was found in the Knowledge Graph.")
            return None
            
        linked_requirements = []
        linked_sections = []
        linked_terms = []
        conflicts = []
        
        visited = set(n["id"] for n in target_nodes)
        
        # 2. Gather context based on query node type
        for target_node in target_nodes:
            node_id = target_node["id"]
            node_label = target_node["label"]
            
            # Case A: Query is a Requirement node
            if node_label == "Requirement":
                # Get the section containing it (Incoming CONTAINS)
                for edge in self.in_edges.get(node_id, []):
                    if edge["type"] == "CONTAINS" and edge["source"].startswith("SEC-"):
                        sec_node = self.nodes.get(edge["source"])
                        if sec_node and sec_node["id"] not in visited:
                            linked_sections.append(sec_node)
                            visited.add(sec_node["id"])
                            
                # Get terms referenced (Outgoing REFERENCES to Terms)
                # Also get other requirements referencing the same terms
                # Get explicit cross-references (Outgoing/Incoming REFERENCES to other sections/reqs)
                # Get conflicts (CONFLICTS_WITH)
                
                # Check outgoing edges
                for edge in self.out_edges.get(node_id, []):
                    target_id = edge["target"]
                    edge_type = edge["type"]
                    
                    if edge_type == "REFERENCES" and target_id.startswith("TERM-"):
                        term_node = self.nodes.get(target_id)
                        if term_node and target_id not in visited:
                            linked_terms.append(term_node)
                            visited.add(target_id)
                            # Find peer requirements referencing this term
                            for peer_edge in self.in_edges.get(target_id, []):
                                peer_id = peer_edge["source"]
                                if peer_id != node_id and peer_id.startswith("REQ-"):
                                    peer_req = self.nodes.get(peer_id)
                                    if peer_req and peer_id not in visited:
                                        linked_requirements.append(peer_req)
                                        visited.add(peer_id)
                                        
                    elif edge_type == "REFERENCES" and target_id.startswith("SEC-"):
                        ref_sec = self.nodes.get(target_id)
                        if ref_sec and target_id not in visited:
                            linked_sections.append(ref_sec)
                            visited.add(target_id)
                            
                    elif edge_type == "REFERENCES" and target_id.startswith("REQ-"):
                        ref_req = self.nodes.get(target_id)
                        if ref_req and target_id not in visited:
                            linked_requirements.append(ref_req)
                            visited.add(target_id)
                            
                # Check conflicts
                for edge in self.out_edges.get(node_id, []):
                    if edge["type"] == "CONFLICTS_WITH":
                        conflicts.append(edge)
                        peer_id = edge["target"]
                        peer_node = self.nodes.get(peer_id)
                        if peer_node and peer_id not in visited:
                            linked_requirements.append(peer_node)
                            visited.add(peer_id)
                            
                for edge in self.in_edges.get(node_id, []):
                    if edge["type"] == "CONFLICTS_WITH":
                        conflicts.append(edge)
                        peer_id = edge["source"]
                        peer_node = self.nodes.get(peer_id)
                        if peer_node and peer_id not in visited:
                            linked_requirements.append(peer_node)
                            visited.add(peer_id)

            # Case B: Query is a Term node
            elif node_label == "Term":
                # Find all requirements referencing this term (Incoming REFERENCES)
                for edge in self.in_edges.get(node_id, []):
                    if edge["type"] == "REFERENCES" and edge["source"].startswith("REQ-"):
                        req_node = self.nodes.get(edge["source"])
                        if req_node and req_node["id"] not in visited:
                            linked_requirements.append(req_node)
                            visited.add(req_node["id"])
                            
                            # Also get the section of that requirement
                            for sec_edge in self.in_edges.get(req_node["id"], []):
                                if sec_edge["type"] == "CONTAINS" and sec_edge["source"].startswith("SEC-"):
                                    sec_node = self.nodes.get(sec_edge["source"])
                                    if sec_node and sec_node["id"] not in visited:
                                        linked_sections.append(sec_node)
                                        visited.add(sec_node["id"])

            # Case C: Query is a Section node
            elif node_label == "Section":
                # Find all requirements contained (Outgoing CONTAINS to Requirement)
                for edge in self.out_edges.get(node_id, []):
                    target_id = edge["target"]
                    if edge["type"] == "CONTAINS":
                        if target_id.startswith("REQ-"):
                            req_node = self.nodes.get(target_id)
                            if req_node and target_id not in visited:
                                linked_requirements.append(req_node)
                                visited.add(target_id)
                        elif target_id.startswith("SEC-"):
                            child_sec = self.nodes.get(target_id)
                            if child_sec and target_id not in visited:
                                linked_sections.append(child_sec)
                                visited.add(target_id)
                                
        return {
            "targets": target_nodes,
            "linked_requirements": linked_requirements,
            "linked_sections": linked_sections,
            "linked_terms": linked_terms,
            "conflicts": conflicts
        }

    def generate_audit_payload(self, query):
        """
        Queries the knowledge graph and compiles a formatted Markdown audit payload.
        """
        ctx = self.query_context(query)
        if not ctx:
            return f"Error: No matching node found for query '{query}' in the Knowledge Graph."
            
        # Format targets
        targets_md = []
        for target in ctx["targets"]:
            label = target["label"]
            props = target["properties"]
            if label == "Requirement":
                targets_md.append(f"- **{target['id']}** [{props.get('constraint_type')} in Section {props.get('section_number')}, Page {props.get('page_number')}]:\n  \"{props.get('text')}\"")
            elif label == "Term":
                targets_md.append(f"- **Term '{props.get('name')}'**: Mentions frequency = {props.get('frequency')}")
            elif label == "Section":
                targets_md.append(f"- **Section {props.get('section_number')}**: \"{props.get('title')}\"")
                
        target_requirements_str = "\n".join(targets_md)
        
        # Format structural hierarchy
        hierarchy_md = []
        for sec in ctx["linked_sections"]:
            props = sec["properties"]
            hierarchy_md.append(f"- Section {props.get('section_number')}: \"{props.get('title')}\"")
        structural_context_str = "\n".join(hierarchy_md) if hierarchy_md else "No direct structural context linked."
        
        # Format linked rules
        rules_md = []
        for req in ctx["linked_requirements"]:
            props = req["properties"]
            rules_md.append(f"- **{req['id']}** [Section {props.get('section_number')} - {props.get('constraint_type')}]: \"{props.get('text')}\"")
        linked_rules_str = "\n".join(rules_md) if rules_md else "No semantically or structurally linked requirements found."
        
        # Format terms
        terms_md = []
        for term in ctx["linked_terms"]:
            props = term["properties"]
            terms_md.append(f"- **{props.get('name')}** (Frequency: {props.get('frequency')})")
        referenced_terms_str = "\n".join(terms_md) if terms_md else "No specific technical terms mapped."
        
        # Format conflicts
        conflicts_md = []
        for edge in ctx["conflicts"]:
            props = edge.get("properties", {})
            conflicts_md.append(f"- Conflict between **{edge['source']}** and **{edge['target']}** on term **'{props.get('shared_term')}'**:\n  *Reason: {props.get('reason')}*")
        potential_conflicts_str = "\n".join(conflicts_md) if conflicts_md else "No explicit conflicts detected in this context segment."
        
        # Fill template
        payload = AUDIT_PROMPT_TEMPLATE.format(
            target_requirements=target_requirements_str,
            structural_context=structural_context_str,
            linked_rules=linked_rules_str,
            referenced_terms=referenced_terms_str,
            potential_conflicts=potential_conflicts_str
        )
        
        return payload
