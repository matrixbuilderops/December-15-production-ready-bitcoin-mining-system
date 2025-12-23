#!/usr/bin/env python3
"""
Test script to verify template hot-reload system is working correctly
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, '.')

from Singularity_Dave_Brainstem_UNIVERSE_POWERED import (
    brain_set_mode,
    brain_save_ledger,
    get_template,
    TemplateCache
)

def test_template_hot_reload():
    """Test that template changes are detected and applied automatically"""
    print("\n" + "="*80)
    print(" TEMPLATE HOT-RELOAD SYSTEM TEST")
    print("="*80)
    
    # Set mode
    brain_set_mode("demo", "HotReloadTest")
    
    # Create a test template
    template_dir = Path("System_File_Examples")
    template_dir.mkdir(exist_ok=True)
    
    test_template_path = template_dir / "global_ledger.json"
    
    # Initial template
    initial_template = {
        "metadata": {
            "file_type": "global_ledger",
            "created_by": "Brain",
            "purpose": "Track mining attempts",
            "version": "1.0",
            "test_field_v1": "This is version 1"
        },
        "total_attempts": 0,
        "entries": []
    }
    
    print("\n--- Step 1: Creating initial template ---")
    with open(test_template_path, 'w') as f:
        json.dump(initial_template, f, indent=2)
    print(f"✅ Created: {test_template_path}")
    print(f"   Version: test_field_v1")
    
    # Load template first time
    print("\n--- Step 2: Loading template (first time) ---")
    template = get_template("global_ledger.json")
    print(f"✅ Template loaded")
    print(f"   test_field_v1: {template.get('metadata', {}).get('test_field_v1', 'NOT FOUND')}")
    
    # Save a ledger entry
    print("\n--- Step 3: Saving ledger entry (uses v1 template) ---")
    test_entry = {
        "test_id": "hot_reload_test_v1",
        "timestamp": datetime.now().isoformat(),
        "nonce": 111111,
        "version": "v1"
    }
    
    result = brain_save_ledger(test_entry, "HotReloadTest")
    if result.get("success"):
        print(f"✅ Ledger saved: {result['global_path']}")
        
        # Check that file has v1 field
        with open(result['global_path'], 'r') as f:
            ledger_data = json.load(f)
        
        if 'test_field_v1' in ledger_data.get('metadata', {}):
            print(f"   ✅ Ledger has test_field_v1: {ledger_data['metadata']['test_field_v1']}")
        else:
            print(f"   ❌ Ledger missing test_field_v1")
    else:
        print(f"❌ Ledger save failed: {result.get('error')}")
    
    # Wait a moment to ensure filesystem time resolution
    print("\n--- Step 4: Waiting 2 seconds for filesystem time resolution ---")
    time.sleep(2)
    
    # Modify template
    print("\n--- Step 5: Modifying template (adding v2 field) ---")
    updated_template = initial_template.copy()
    updated_template["metadata"]["test_field_v2"] = "This is version 2 - HOT RELOADED!"
    updated_template["metadata"]["hot_reload_test"] = "SUCCESS"
    updated_template["new_top_level_field"] = "This field was added in v2"
    
    with open(test_template_path, 'w') as f:
        json.dump(updated_template, f, indent=2)
    print(f"✅ Template modified: {test_template_path}")
    print(f"   Added: test_field_v2, hot_reload_test, new_top_level_field")
    
    # Load template again (should auto-reload)
    print("\n--- Step 6: Loading template again (should detect change) ---")
    template_v2 = get_template("global_ledger.json")
    print(f"✅ Template reloaded")
    print(f"   test_field_v1: {template_v2.get('metadata', {}).get('test_field_v1', 'NOT FOUND')}")
    print(f"   test_field_v2: {template_v2.get('metadata', {}).get('test_field_v2', 'NOT FOUND')}")
    print(f"   hot_reload_test: {template_v2.get('metadata', {}).get('hot_reload_test', 'NOT FOUND')}")
    print(f"   new_top_level_field: {template_v2.get('new_top_level_field', 'NOT FOUND')}")
    
    # Save another ledger entry (should use v2 template)
    print("\n--- Step 7: Saving ledger entry (should use v2 template) ---")
    test_entry_v2 = {
        "test_id": "hot_reload_test_v2",
        "timestamp": datetime.now().isoformat(),
        "nonce": 222222,
        "version": "v2"
    }
    
    result2 = brain_save_ledger(test_entry_v2, "HotReloadTest")
    if result2.get("success"):
        print(f"✅ Ledger saved: {result2['global_path']}")
        
        # Check that file now has BOTH v1 and v2 fields (merged)
        with open(result2['global_path'], 'r') as f:
            ledger_data_v2 = json.load(f)
        
        print("\n   Checking merged fields:")
        metadata = ledger_data_v2.get('metadata', {})
        
        if 'test_field_v1' in metadata:
            print(f"   ✅ Still has test_field_v1: {metadata['test_field_v1']}")
        else:
            print(f"   ❌ Missing test_field_v1")
        
        if 'test_field_v2' in metadata:
            print(f"   ✅ Now has test_field_v2: {metadata['test_field_v2']}")
        else:
            print(f"   ❌ Missing test_field_v2 (HOT-RELOAD FAILED!)")
        
        if 'hot_reload_test' in metadata:
            print(f"   ✅ Now has hot_reload_test: {metadata['hot_reload_test']}")
        else:
            print(f"   ❌ Missing hot_reload_test")
        
        if 'new_top_level_field' in ledger_data_v2:
            print(f"   ✅ Now has new_top_level_field: {ledger_data_v2['new_top_level_field']}")
        else:
            print(f"   ❌ Missing new_top_level_field")
        
        # Check entries
        print(f"\n   Entries in ledger: {len(ledger_data_v2.get('entries', []))}")
        for entry in ledger_data_v2.get('entries', []):
            print(f"     - {entry.get('test_id')} (version: {entry.get('version')})")
    else:
        print(f"❌ Ledger save failed: {result2.get('error')}")
    
    # Final verification
    print("\n--- VERIFICATION SUMMARY ---")
    cache = TemplateCache()
    changed_templates = cache.check_for_updates()
    print(f"Changed templates detected: {len(changed_templates)}")
    
    if 'test_field_v2' in metadata and 'hot_reload_test' in metadata:
        print("\n✅ HOT-RELOAD SYSTEM WORKING!")
        print("   Template changes were detected and applied automatically")
        return True
    else:
        print("\n❌ HOT-RELOAD SYSTEM FAILED!")
        print("   Template changes were NOT detected")
        return False

def main():
    try:
        success = test_template_hot_reload()
        
        print("\n" + "="*80)
        if success:
            print(" TEST PASSED: Template hot-reload is working")
        else:
            print(" TEST FAILED: Template hot-reload is NOT working")
        print("="*80)
        print()
        
        sys.exit(0 if success else 1)
    
    except Exception as e:
        print(f"\n❌ TEST ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
