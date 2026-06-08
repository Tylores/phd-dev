#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pypdf>=5.0.0",
# ]
# ///
"""
Main entrypoint for the IEEE Standards Parsing Pipeline.
Orchestrates:
1. Structural & Hierarchical Parser
2. Deterministic Rule Mining Engine
3. Semantic Linker & Knowledge Graph Exporter
4. Agentic Auditing Skeleton

Usage:
    python3 main.py --pdf <path_to_pdf> [options]
"""

import os
import sys
import json
import argparse
import logging

# Ensure local module imports work regardless of execution working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from parser import PDFParser, build_hierarchy_tree, tree_to_markdown
from rule_miner import RuleMiner
from semantic_linker import SemanticLinker
from auditing import RequirementAuditor

# Configure logging to console
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("Pipeline")

def main():
    parser = argparse.ArgumentParser(
        description="IEEE Standards Conformance & Graph-Based Extraction Pipeline"
    )
    parser.add_argument(
        "--pdf",
        type=str,
        required=True,
        help="Path to the dense technical IEEE standard PDF file"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./output_ieee_parser",
        help="Directory to save output files (default: ./output_ieee_parser)"
    )
    parser.add_argument(
        "--query-audit",
        type=str,
        help="Requirement ID (e.g. REQ-001), Term (e.g. heartbeat), or Section (e.g. 2.0) to query for LLM auditing"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress verbose logs"
    )

    args = parser.parse_args()

    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    # 1. Validation and Directory Creation
    if not os.path.exists(args.pdf):
        logger.error(f"Target PDF file not found at: {args.pdf}")
        sys.exit(1)

    out_dir = args.output_dir
    os.makedirs(out_dir, exist_ok=True)
    logger.info(f"Writing outputs to directory: {os.path.abspath(out_dir)}")

    # Define standard output paths
    blocks_path = os.path.join(out_dir, "blocks.json")
    tree_path = os.path.join(out_dir, "tree.json")
    markdown_path = os.path.join(out_dir, "document_cleaned.md")
    ledger_path = os.path.join(out_dir, "ledger.json")
    graph_path = os.path.join(out_dir, "knowledge_graph.json")

    # =========================================================================
    # Step 1: Structural & Hierarchical Parser
    # =========================================================================
    logger.info("Step 1: Running Structural & Hierarchical Parser...")
    try:
        pdf_parser = PDFParser(args.pdf)
        blocks = pdf_parser.parse()
        logger.info(f"Successfully parsed {len(blocks)} layout blocks from PDF.")
        
        # Save flat blocks
        with open(blocks_path, "w", encoding="utf-8") as f:
            json.dump(blocks, f, indent=2)
        logger.info(f"Saved layout blocks to {blocks_path}")

        # Build tree structure
        tree = build_hierarchy_tree(blocks)
        with open(tree_path, "w", encoding="utf-8") as f:
            json.dump(tree, f, indent=2)
        logger.info(f"Saved structural outline tree to {tree_path}")

        # Export to clean Markdown representation
        md_content = tree_to_markdown(tree)
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info(f"Saved reconstructed Markdown layout to {markdown_path}")

    except Exception as e:
        logger.error(f"Failure in Structural Parser: {str(e)}", exc_info=True)
        sys.exit(1)

    # =========================================================================
    # Step 2: Deterministic Rule Mining Engine
    # =========================================================================
    logger.info("Step 2: Sweeping text for compliance rules...")
    try:
        miner = RuleMiner()
        rule_ledger = miner.mine_rules(blocks)
        logger.info(f"Found {len(rule_ledger)} compliance requirement rules.")
        
        # Save ledger
        with open(ledger_path, "w", encoding="utf-8") as f:
            json.dump(rule_ledger, f, indent=2)
        logger.info(f"Saved compliance rules ledger to {ledger_path}")

    except Exception as e:
        logger.error(f"Failure in Rule Mining Engine: {str(e)}", exc_info=True)
        sys.exit(1)

    # =========================================================================
    # Step 3: Semantic Linker & Knowledge Graph Exporter
    # =========================================================================
    logger.info("Step 3: Generating relation map and Knowledge Graph...")
    try:
        linker = SemanticLinker()
        kg = linker.build_knowledge_graph(rule_ledger, blocks)
        
        node_counts = {}
        for node in kg["nodes"]:
            lbl = node["label"]
            node_counts[lbl] = node_counts.get(lbl, 0) + 1
            
        edge_counts = {}
        for edge in kg["edges"]:
            typ = edge["type"]
            edge_counts[typ] = edge_counts.get(typ, 0) + 1

        logger.info(f"Knowledge Graph constructed with:")
        for lbl, count in node_counts.items():
            logger.info(f"  - Nodes [{lbl}]: {count}")
        for typ, count in edge_counts.items():
            logger.info(f"  - Edges [{typ}]: {count}")

        # Save KG
        with open(graph_path, "w", encoding="utf-8") as f:
            json.dump(kg, f, indent=2)
        logger.info(f"Saved Knowledge Graph payload to {graph_path}")

    except Exception as e:
        logger.error(f"Failure in Semantic Linker: {str(e)}", exc_info=True)
        sys.exit(1)

    # =========================================================================
    # Step 4: Agentic Auditing Skeleton
    # =========================================================================
    if args.query_audit:
        logger.info(f"Step 4: Compiling auditing prompt for query: '{args.query_audit}'...")
        try:
            auditor = RequirementAuditor(kg)
            payload = auditor.generate_audit_payload(args.query_audit)
            
            audit_filename = f"audit_payload_{args.query_audit.replace('/', '_').replace('.', '_')}.md"
            audit_path = os.path.join(out_dir, audit_filename)
            
            with open(audit_path, "w", encoding="utf-8") as f:
                f.write(payload)
            logger.info(f"Saved ready-for-LLM auditing payload to {audit_path}")
            
            # Print a quick preview of the audit
            print("\n" + "="*80)
            print(f"AUDIT PAYLOAD COMPILED (First 400 chars):")
            print("="*80)
            print(payload[:400] + "\n...")
            print("="*80 + "\n")

        except Exception as e:
            logger.error(f"Failure in Auditing Skeleton: {str(e)}", exc_info=True)
            sys.exit(1)
            
    logger.info("Pipeline executed successfully. All stages completed.")

if __name__ == "__main__":
    main()
