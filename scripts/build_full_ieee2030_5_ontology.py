#!/usr/bin/env python3
"""
Full IEEE 2030.5 Ontology Generator using OwlScribe & XSD Parsing

Parses all complexTypes, inheritance structures, elements, and attributes
from egot/sep/sep.xsd, aligns key concepts with SAREF, SOSA, and SAREF4GRID,
and generates the complete W3C OWL 2.0 Turtle ontology notes/ieee-std-2030-5-2023.ttl.
"""

import sys
import os
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

# Base upper ontology mappings
UPPER_ONTOLOGY_MAPPINGS = [
    {"term": "EndDevice", "target_iri": "https://saref.etsi.org/core/Device", "mapping_type": "subClassOf"},
    {"term": "EnergyServicesInterface", "target_iri": "https://saref.etsi.org/core/Device", "mapping_type": "subClassOf"},
    {"term": "UsagePoint", "target_iri": "https://saref.etsi.org/saref4grid/PowerGridNode", "mapping_type": "subClassOf"},
    {"term": "Reading", "target_iri": "http://www.w3.org/ns/sosa/Observation", "mapping_type": "subClassOf"},
    {"term": "MeterReading", "target_iri": "https://saref.etsi.org/core/Measurement", "mapping_type": "subClassOf"},
    {"term": "DERControl", "target_iri": "https://saref.etsi.org/core/Command", "mapping_type": "subClassOf"},
]

XSD_PRIMITIVE_TYPE_MAP = {
    "xs:string": "http://www.w3.org/2001/XMLSchema#string",
    "xs:boolean": "http://www.w3.org/2001/XMLSchema#boolean",
    "xs:integer": "http://www.w3.org/2001/XMLSchema#integer",
    "xs:int": "http://www.w3.org/2001/XMLSchema#int",
    "xs:long": "http://www.w3.org/2001/XMLSchema#long",
    "xs:unsignedInt": "http://www.w3.org/2001/XMLSchema#unsignedInt",
    "xs:unsignedShort": "http://www.w3.org/2001/XMLSchema#unsignedShort",
    "xs:unsignedByte": "http://www.w3.org/2001/XMLSchema#unsignedByte",
    "xs:unsignedLong": "http://www.w3.org/2001/XMLSchema#unsignedLong",
    "xs:hexBinary": "http://www.w3.org/2001/XMLSchema#hexBinary",
    "xs:dateTime": "http://www.w3.org/2001/XMLSchema#dateTime",
    "xs:byte": "http://www.w3.org/2001/XMLSchema#byte",
    "xs:short": "http://www.w3.org/2001/XMLSchema#short",
}

def parse_xsd_full(xsd_path: Path):
    tree = ET.parse(xsd_path)
    root = tree.getroot()
    ns = {"xs": "http://www.w3.org/2001/XMLSchema"}
    
    classes = []
    object_properties = []
    data_properties = []
    
    known_complex_types = set()
    for ct in root.findall(".//xs:complexType", ns):
        name = ct.get("name")
        if name:
            known_complex_types.add(name)
            
    for ct in root.findall(".//xs:complexType", ns):
        name = ct.get("name")
        if not name:
            continue
            
        doc_elem = ct.find("xs:annotation/xs:documentation", ns)
        comment = doc_elem.text.strip() if doc_elem is not None and doc_elem.text else f"IEEE 2030.5 type {name}"
        
        parent_class = None
        ext = ct.find(".//xs:extension", ns)
        if ext is not None:
            base = ext.get("base")
            if base:
                parent_class = base.split(":")[-1]
                
        classes.append({
            "name": name,
            "parent_class": parent_class,
            "comment": comment
        })
        
        # Parse elements inside this complexType
        for elem in ct.findall(".//xs:element", ns):
            ename = elem.get("name")
            etype = elem.get("type")
            if not ename or not etype:
                continue
                
            clean_type = etype.split(":")[-1]
            edoc = elem.find("xs:annotation/xs:documentation", ns)
            ecomment = edoc.text.strip() if edoc is not None and edoc.text else f"Property {ename} of {name}"
            
            if clean_type in known_complex_types:
                prop_name = f"has{ename[0].upper()}{ename[1:]}" if not ename.startswith("has") else ename
                object_properties.append({
                    "name": prop_name,
                    "domain": name,
                    "range": clean_type,
                    "comment": ecomment
                })
            elif etype in XSD_PRIMITIVE_TYPE_MAP or etype.startswith("xs:"):
                xsd_range = XSD_PRIMITIVE_TYPE_MAP.get(etype, "http://www.w3.org/2001/XMLSchema#string")
                data_properties.append({
                    "name": ename,
                    "domain": name,
                    "range": xsd_range,
                    "comment": ecomment
                })
                
    return classes, object_properties, data_properties

def call_owlscribe_generate(input_payload):
    owlscribe_bin = Path("/home/tslay/dev/OwlScribe/target/debug/owlscribe")
    if not owlscribe_bin.exists():
        # Build OwlScribe if needed
        subprocess.run(["cargo", "build"], cwd="/home/tslay/dev/OwlScribe", check=True)

    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "generate_owl_ontology",
            "arguments": input_payload
        }
    }
    input_data = json.dumps(req) + "\n"
    proc = subprocess.Popen(
        [str(owlscribe_bin)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd="/home/tslay/dev/OwlScribe"
    )
    stdout, stderr = proc.communicate(input=input_data)
    if proc.returncode != 0:
        raise RuntimeError(f"OwlScribe failed:\nStderr: {stderr}\nStdout: {stdout}")

    json_lines = [line.strip() for line in stdout.splitlines() if line.strip().startswith("{")]
    if not json_lines:
        raise RuntimeError(f"No JSON response from OwlScribe:\nStdout: {stdout}\nStderr: {stderr}")

    resp = json.loads(json_lines[-1])
    if "error" in resp:
        raise RuntimeError(f"RPC error: {resp['error']}")

    result = resp.get("result", {})
    if result.get("is_error"):
        raise RuntimeError(f"Tool error: {result.get('content')}")

    text_content = result["content"][0]["text"]
    return json.loads(text_content)

def main():
    xsd_path = Path("egot/sep/sep.xsd")
    ttl_out_path = Path("notes/ieee-std-2030-5-2023.ttl")
    
    print("Parsing sep.xsd structure...")
    classes, object_properties, data_properties = parse_xsd_full(xsd_path)
    print(f"Extracted {len(classes)} classes, {len(object_properties)} object properties, {len(data_properties)} data properties from XSD.")
    
    payload = {
        "ontology_iri": "https://smartgrid.ieee.org/2030-5/2023#",
        "prefix": "ieee2030_5",
        "format": "turtle",
        "imports": [
            "https://saref.etsi.org/saref4grid/",
            "http://www.w3.org/ns/sosa/",
            "https://saref.etsi.org/core/"
        ],
        "classes": classes,
        "object_properties": object_properties,
        "data_properties": data_properties,
        "class_mappings": UPPER_ONTOLOGY_MAPPINGS
    }
    
    print("Calling OwlScribe generate_owl_ontology tool...")
    res = call_owlscribe_generate(payload)
    
    serialized_ttl = res.get("serialized_ontology", "")
    if not serialized_ttl:
        raise ValueError("Serialized ontology output was empty!")
        
    ttl_out_path.write_text(serialized_ttl, encoding="utf-8")
    print(f"Successfully serialized {res.get('class_count')} classes, {res.get('object_property_count')} object properties, {res.get('data_property_count')} data properties to '{ttl_out_path}'.")

if __name__ == "__main__":
    main()
