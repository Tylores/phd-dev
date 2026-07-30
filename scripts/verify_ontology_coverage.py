#!/usr/bin/env python3
"""
Verification & Benchmark Tool: XSD vs OWL Turtle Ontology Coverage

Compares terms defined in an IEEE 2030.5 / SEP 2 XML Schema (sep.xsd)
against classes and properties serialized in an OWL 2.0 Turtle ontology (.ttl).
"""

import sys
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def parse_xsd_terms(xsd_path: Path):
    """
    Parses complexTypes, elements, and simpleTypes from sep.xsd.
    """
    tree = ET.parse(xsd_path)
    root = tree.getroot()
    
    # XML Schema namespace
    ns = {"xs": "http://www.w3.org/2001/XMLSchema"}
    
    complex_types = set()
    elements = set()
    element_properties = set()
    inheritance_map = {}
    
    for ct in root.findall(".//xs:complexType", ns):
        name = ct.get("name")
        if name:
            complex_types.add(name)
            
            # Check extension base (subclass / inheritance)
            ext = ct.find(".//xs:extension", ns)
            if ext is not None:
                base = ext.get("base")
                if base:
                    base_clean = base.split(":")[-1]
                    inheritance_map[name] = base_clean
                    
            # Check child elements (properties)
            for elem in ct.findall(".//xs:element", ns):
                ename = elem.get("name")
                if ename:
                    element_properties.add(ename)

    for el in root.findall("xs:element", ns):
        name = el.get("name")
        if name:
            elements.add(name)
            
    return {
        "complex_types": complex_types,
        "elements": elements,
        "element_properties": element_properties,
        "inheritance_map": inheritance_map
    }

def parse_ttl_terms(ttl_path: Path):
    """
    Parses owl:Class, owl:ObjectProperty, and owl:DatatypeProperty from a Turtle file.
    Supports rdflib if installed, falls back to regex matching.
    """
    classes = set()
    object_properties = set()
    datatype_properties = set()
    
    content = ttl_path.read_text(encoding="utf-8")
    
    # Simple regex extraction for local names
    # Match <...#Name> a owl:Class
    class_matches = re.findall(r"<[^>]+#([A-Za-z0-9_]+)>\s+a\s+owl:Class", content)
    classes.update(class_matches)
    
    # Match <...#Name> a owl:ObjectProperty
    obj_matches = re.findall(r"<[^>]+#([A-Za-z0-9_]+)>\s+a\s+owl:ObjectProperty", content)
    object_properties.update(obj_matches)
    
    # Match <...#Name> a owl:DatatypeProperty
    data_matches = re.findall(r"<[^>]+#([A-Za-z0-9_]+)>\s+a\s+owl:DatatypeProperty", content)
    datatype_properties.update(data_matches)
    
    # Try rdflib for full triple parsing if available
    try:
        import rdflib
        g = rdflib.Graph()
        g.parse(data=content, format="turtle")
        
        OWL = rdflib.Namespace("http://www.w3.org/2002/07/owl#")
        for s in g.subjects(rdflib.RDF.type, OWL.Class):
            name = str(s).split("#")[-1].split("/")[-1]
            if name:
                classes.add(name)
        for s in g.subjects(rdflib.RDF.type, OWL.ObjectProperty):
            name = str(s).split("#")[-1].split("/")[-1]
            if name:
                object_properties.add(name)
        for s in g.subjects(rdflib.RDF.type, OWL.DatatypeProperty):
            name = str(s).split("#")[-1].split("/")[-1]
            if name:
                datatype_properties.add(name)
    except ImportError:
        pass

    return {
        "classes": classes,
        "object_properties": object_properties,
        "datatype_properties": datatype_properties
    }

def generate_report(xsd_info, ttl_info, verbose=False):
    xsd_types = xsd_info["complex_types"]
    ttl_classes = ttl_info["classes"]
    
    matched_classes = xsd_types.intersection(ttl_classes)
    missing_classes = sorted(list(xsd_types - ttl_classes))
    extra_ttl_classes = sorted(list(ttl_classes - xsd_types))
    
    total_xsd = len(xsd_types)
    total_matched = len(matched_classes)
    coverage_pct = (total_matched / total_xsd * 100.0) if total_xsd > 0 else 0.0
    
    print("=" * 65)
    print("      IEEE 2030.5 XSD vs OWL ONTOLOGY COVERAGE REPORT")
    print("=" * 65)
    print(f"XSD ComplexTypes Total : {total_xsd}")
    print(f"OWL Classes Found      : {len(ttl_classes)}")
    print(f"Matched Classes        : {total_matched}")
    print(f"Class Coverage Rate    : {coverage_pct:.2f}%")
    print("-" * 65)
    print(f"OWL ObjectProperties   : {len(ttl_info['object_properties'])}")
    print(f"OWL DatatypeProperties : {len(ttl_info['datatype_properties'])}")
    print("-" * 65)
    
    if missing_classes:
        print(f"\nMissing XSD ComplexTypes ({len(missing_classes)} total):")
        sample_missing = missing_classes[:25]
        for m in sample_missing:
            print(f"  - {m}")
        if len(missing_classes) > 25:
            print(f"  ... and {len(missing_classes) - 25} more.")
            
    if extra_ttl_classes:
        print(f"\nOWL Classes not directly in XSD ComplexTypes ({len(extra_ttl_classes)} total):")
        for e in extra_ttl_classes[:10]:
            print(f"  + {e}")

    print("=" * 65)
    return {
        "total_xsd": total_xsd,
        "total_matched": total_matched,
        "coverage_pct": coverage_pct,
        "missing_count": len(missing_classes)
    }

def main():
    parser = argparse.ArgumentParser(description="Verify XSD coverage in OWL Turtle ontology.")
    parser.add_argument("--xsd", default="egot/sep/sep.xsd", help="Path to sep.xsd schema")
    parser.add_argument("--ttl", default="notes/ieee-std-2030-5-2023.ttl", help="Path to IEEE 2030.5 .ttl ontology")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    xsd_path = Path(args.xsd)
    ttl_path = Path(args.ttl)
    
    if not xsd_path.exists():
        print(f"Error: XSD file not found at '{xsd_path}'", file=sys.stderr)
        sys.exit(1)
        
    if not ttl_path.exists():
        print(f"Error: TTL file not found at '{ttl_path}'", file=sys.stderr)
        sys.exit(1)
        
    xsd_info = parse_xsd_terms(xsd_path)
    ttl_info = parse_ttl_terms(ttl_path)
    
    generate_report(xsd_info, ttl_info, args.verbose)

if __name__ == "__main__":
    main()
