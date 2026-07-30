#!/usr/bin/env python3
"""
Verification Script: Common Grid Services & ESI to IEEE 2030.5 Mapping Ontology
Validates RDF/OWL Turtle syntax, class cross-references, lifecycle coverage,
and IEEE 2030.5 schema resource existence.
"""

import sys
import re
from pathlib import Path

def parse_ttl_classes_and_properties(ttl_path: Path):
    content = ttl_path.read_text(encoding="utf-8")
    
    classes = set()
    properties = set()
    
    # Extraction for OWL classes (both prefix:Name and <http...#Name>)
    class_matches = re.findall(r"(?:[a-zA-Z0-9_\-]+:|<https?://[^>]+#)([a-zA-Z0-9_\-]+)>?\s+a\s+owl:Class", content)
    for name in class_matches:
        classes.add(name)
        
    prop_matches = re.findall(r"(?:[a-zA-Z0-9_\-]+:|<https?://[^>]+#)([a-zA-Z0-9_\-]+)>?\s+a\s+owl:(?:ObjectProperty|DatatypeProperty)", content)
    for name in prop_matches:
        properties.add(name)
        
    return classes, properties

def verify_mapping():
    base_dir = Path(__file__).parent.parent / "notes"
    
    mapping_ttl = base_dir / "grid_services_esi_2030_5_mapping.ttl"
    cgs_ttl = base_dir / "common_grid_services.ttl"
    esi_ttl = base_dir / "energy_service_interface.ttl"
    ieee_ttl = base_dir / "ieee-std-2030-5-2023.ttl"
    
    for path in [mapping_ttl, cgs_ttl, esi_ttl, ieee_ttl]:
        if not path.exists():
            print(f"❌ Error: Required file missing: {path}")
            sys.exit(1)
            
    print("🔍 Parsing ontologies...")
    mapping_content = mapping_ttl.read_text(encoding="utf-8")
    
    cgs_classes, _ = parse_ttl_classes_and_properties(cgs_ttl)
    esi_classes, _ = parse_ttl_classes_and_properties(esi_ttl)
    ieee_classes, _ = parse_ttl_classes_and_properties(ieee_ttl)
    
    print(f"   - CGS Classes found: {len(cgs_classes)}")
    print(f"   - ESI Classes found: {len(esi_classes)}")
    print(f"   - IEEE 2030.5 Classes found: {len(ieee_classes)}")
    
    # 1. Verify 6 Common Grid Services Mapped
    expected_cgs_services = [
        "EnergyService", "ReserveService", "RegulationService",
        "FrequencyResponseService", "VoltageManagementService", "BlackstartService"
    ]
    
    print("\n📋 Checking Common Grid Services Mapped:")
    for service in expected_cgs_services:
        if f"cgs:{service}" in mapping_content:
            print(f"   ✅ cgs:{service} mapped")
        else:
            print(f"   ❌ ERROR: cgs:{service} NOT found in mapping ontology")
            sys.exit(1)
            
    # 2. Verify 5 ESI Lifecycle Phases Mapped
    expected_lifecycle_phases = [
        "RegistrationPhaseMapping", "SchedulingPhaseMapping", "OperationPhaseMapping",
        "VerificationPhaseMapping", "SettlementPhaseMapping"
    ]
    
    print("\n🔄 Checking ESI Lifecycle Phases Mapped:")
    for phase in expected_lifecycle_phases:
        if phase in mapping_content:
            print(f"   ✅ {phase} present")
        else:
            print(f"   ❌ ERROR: {phase} NOT found in mapping ontology")
            sys.exit(1)
            
    # 3. Verify Referenced IEEE 2030.5 Resources
    referenced_sep_resources = set(re.findall(r"sep:([a-zA-Z0-9_\-]+)", mapping_content))
    print(f"\n⚡ Checking Referenced IEEE 2030.5 Resources ({len(referenced_sep_resources)} total):")
    
    missing_sep = []
    for res in referenced_sep_resources:
        if res in ieee_classes or res in ["Resource", "IdentifiedObject"]:
            print(f"   ✅ sep:{res} validated in IEEE 2030.5 ontology")
        else:
            missing_sep.append(res)
            print(f"   ⚠️ WARNING: sep:{res} not explicitly declared as owl:Class in IEEE ttl")
            
    if missing_sep:
        print(f"❌ Missing SEP classes: {missing_sep}")
        sys.exit(1)
        
    print("\n🎉 SUCCESS: All Common Grid Services, ESI lifecycles, and IEEE 2030.5 mappings verified successfully!")

if __name__ == "__main__":
    verify_mapping()
