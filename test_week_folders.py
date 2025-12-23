#!/usr/bin/env python3
"""
Test script to verify week folder hierarchy is working correctly
Tests all 4 modes: demo, test, staging, live
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, '.')

from Singularity_Dave_Brainstem_UNIVERSE_POWERED import (
    brain_set_mode,
    brain_save_ledger,
    brain_save_math_proof,
    brain_save_submission,
    brain_save_system_report,
    brain_save_system_error,
    brain_get_hierarchical_path_info,
    brain_get_base_path
)

def test_week_folder_hierarchy(mode):
    """Test that week folders are created correctly for a given mode"""
    print(f"\n{'='*80}")
    print(f"TESTING MODE: {mode.upper()}")
    print(f"{'='*80}")
    
    # Set mode
    brain_set_mode(mode, "TestComponent")
    base_path = brain_get_base_path()
    print(f"Base path: {base_path}")
    
    # Get hierarchical info
    path_info = brain_get_hierarchical_path_info()
    print(f"\nHierarchical path info:")
    for key, value in path_info.items():
        print(f"  {key}: {value}")
    
    # Test data
    test_entry = {
        "test_id": "week_folder_test",
        "timestamp": datetime.now().isoformat(),
        "mode": mode,
        "leading_zeros": 19,
        "meets_difficulty": True,
        "nonce": 123456789,
        "block_hash": "0000000000000000000abcdef"
    }
    
    print(f"\n--- Testing Ledger ---")
    ledger_result = brain_save_ledger(test_entry, "TestComponent")
    if ledger_result.get("success"):
        print(f"✅ Ledger saved successfully")
        print(f"   Global path: {ledger_result['global_path']}")
        
        # Check for week folder in hierarchical paths
        if 'hierarchical' in ledger_result:
            for level, result in ledger_result['hierarchical'].items():
                if result.get('success'):
                    path = result.get('path', '')
                    if '/W' in path:
                        print(f"   ✅ Week folder found in {level}: {path}")
    else:
        print(f"❌ Ledger save failed: {ledger_result.get('error')}")
    
    print(f"\n--- Testing Math Proof ---")
    proof_result = brain_save_math_proof(test_entry, "TestComponent")
    if proof_result.get("success"):
        print(f"✅ Math proof saved successfully")
        print(f"   Global path: {proof_result['global_path']}")
    else:
        print(f"❌ Math proof save failed: {proof_result.get('error')}")
    
    print(f"\n--- Testing Submission ---")
    submission_result = brain_save_submission(test_entry, "TestComponent")
    if submission_result.get("success"):
        print(f"✅ Submission saved successfully")
        print(f"   Global path: {submission_result['global_path']}")
    else:
        print(f"❌ Submission save failed: {submission_result.get('error')}")
    
    print(f"\n--- Testing System Report ---")
    report_result = brain_save_system_report(test_entry, "TestComponent", "status")
    if report_result.get("success"):
        print(f"✅ System report saved successfully")
    else:
        print(f"❌ System report save failed: {report_result.get('error')}")
    
    print(f"\n--- Testing Error Report ---")
    error_result = brain_save_system_error(test_entry, "TestComponent")
    if error_result.get("success"):
        print(f"✅ Error report saved successfully")
    else:
        print(f"❌ Error report save failed: {error_result.get('error')}")
    
    # Verify folder structure exists
    print(f"\n--- Verifying Week Folder Structure ---")
    expected_week_path = Path(f"{base_path}/Ledgers/{path_info['year']}/{path_info['month']}/{path_info['week']}")
    if expected_week_path.exists():
        print(f"✅ Week folder exists: {expected_week_path}")
        
        # List contents
        print(f"\n   Week folder contents:")
        for item in expected_week_path.iterdir():
            if item.is_dir():
                print(f"     📁 {item.name}/ (folder)")
            else:
                print(f"     📄 {item.name}")
    else:
        print(f"❌ Week folder NOT found: {expected_week_path}")
    
    return True

def main():
    print("\n" + "="*80)
    print(" WEEK FOLDER HIERARCHY TEST - ALL MODES")
    print("="*80)
    
    modes = ["demo", "test", "staging", "live"]
    
    for mode in modes:
        try:
            test_week_folder_hierarchy(mode)
        except Exception as e:
            print(f"\n❌ ERROR testing {mode} mode: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*80)
    print(" TEST COMPLETE")
    print("="*80)
    print("\nTo verify manually:")
    print("  Demo:    ls -la 'Test/Demo/Mining/Ledgers/*/*/W*/'")
    print("  Test:    ls -la 'Test/Test mode/Mining/Ledgers/*/*/W*/'")
    print("  Staging: ls -la 'Mining/Ledgers/*/*/W*/'")
    print("  Live:    ls -la 'Mining/Ledgers/*/*/W*/'")
    print()

if __name__ == "__main__":
    main()
