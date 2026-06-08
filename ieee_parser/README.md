# IEEE Standards Parsing & Compliance Linker Pipeline

A production-ready, modular Python tool for parsing dense IEEE technical standard PDFs, mining compliance requirements, extracting terminology concepts, and compiling Knowledge Graph representations.

---

## 1. Fast Execution Guide with `uv`

This project is fully compatible with [Astral's `uv`](https://github.com/astral-sh/uv) tool. `uv` handles Python virtual environments and dependencies automatically and on-the-fly.

### Running the Script Directly (Zero Setup)
You can run the script without any prior package installation or environment setup:
```bash
# Formatted execution using PEP 723 script metadata
uv run ieee_parser/main.py --pdf sources/energy_service_interface_guide.pdf
```

### Running an LLM Audit Query
Query a specific requirement ID, concept term, or section number to generate an LLM critique prompt context:
```bash
# Compiles a markdown prompt with surrounding structural and semantic rules
uv run ieee_parser/main.py \
  --pdf sources/energy_service_interface_guide.pdf \
  --query-audit "REQ-016"
```

---

## 2. CLI Arguments Reference

| Argument | Type | Default | Description |
|---|---|---|---|
| `--pdf` | String | **Required** | Path to the target IEEE technical standard PDF file. |
| `--output-dir` | String | `./output_ieee_parser` | Folder path where all parsed outputs will be written. |
| `--query-audit` | String | None | Requirement ID (`REQ-###`), Term name, or Section number to search in the Graph. |
| `--quiet` | Flag | False | Suppress verbose execution logs. |

---

## 3. Output Pipeline Artifacts

By default, all pipeline assets are written to `./output_ieee_parser`:

1. **`blocks.json`**: Flat list of extracted, cleaned text layout blocks (headings, paragraphs, lists, tables).
2. **`tree.json`**: Nested structural outlines showing document section parent-child hierarchy.
3. **`document_cleaned.md`**: Fully cleaned and reconstructed document text in Markdown.
4. **`ledger.json`**: Compliance requirements ledger containing IDs, constraint classifications, and hierarchies.
5. **`knowledge_graph.json`**: Standardized JSON containing graph nodes (`Requirement`, `Section`, `Term`) and edges (`CONTAINS`, `REFERENCES`, `CONFLICTS_WITH`).
6. **`audit_payload_<query>.md`**: Formatted prompt containing the queried target along with its direct structural parents, semantically linked rules, referenced terms, flagged contradictions, and system critique instructions.

---

## 4. Instructions for AI Agent Systems (AI-to-AI Guidelines)

If you are an AI developer or agent extending or working with this codebase, please follow these guidelines:

### Codebase Organization
- **Parser Logic**: To adjust headers/footers cleaning patterns or block merging rules, edit [parser.py](file:///home/tylor/phd/ieee_parser/parser.py).
- **Rule Extraction Patterns**: To add new keywords (e.g., standard RFC conformance terms), modify `RULE_PATTERNS` in [rule_miner.py](file:///home/tylor/phd/ieee_parser/rule_miner.py).
- **Concept & Stopwords Definitions**: Curated smart grid and technical terms are managed in `CURATED_TERMS` in [semantic_linker.py](file:///home/tylor/phd/ieee_parser/semantic_linker.py). General stopwords can be added to `STOPWORDS`.
- **System Prompt Templates**: The LLM critique prompt structure and evaluation instructions are defined in `AUDIT_PROMPT_TEMPLATE` within [auditing.py](file:///home/tylor/phd/ieee_parser/auditing.py).

### How to Modify Dependencies
If you need to add Python dependencies, update both:
1. The `dependencies` list in `pyproject.toml`.
2. The PEP 723 inline script header at the top of [main.py](file:///home/tylor/phd/ieee_parser/main.py):
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = [
   #     "pypdf>=5.0.0",
   #     "new-dependency>=1.0.0",
   # ]
   # ///
   ```

### Parsing Pipeline Flow Reference
When executing the pipeline programmatically, follow this object lifecycle:
```python
from parser import PDFParser, build_hierarchy_tree
from rule_miner import RuleMiner
from semantic_linker import SemanticLinker
from auditing import RequirementAuditor

# 1. Parse PDF to flat layout blocks
blocks = PDFParser("path/to/doc.pdf").parse()

# 2. Reconstruct structural tree
tree = build_hierarchy_tree(blocks)

# 3. Mine deterministic compliance rules
ledger = RuleMiner().mine_rules(blocks)

# 4. Construct Knowledge Graph
kg = SemanticLinker().build_knowledge_graph(ledger, blocks)

# 5. Extract audit prompt
auditor = RequirementAuditor(kg)
payload = auditor.generate_audit_payload("REQ-001")
```
