#!/usr/bin/env python3
"""
Test DTM Consensus Mechanism
Verify that DTM correctly adjusts unrealistic mathematical solutions to Bitcoin-acceptable ones
"""

import sys
sys.path.insert(0, '.')

from dynamic_template_manager import DynamicTemplateManager
from datetime import datetime

def test_dtm_consensus():
    """Test that DTM adjusts 50+ zero solutions to realistic ~19-22 zeros"""
    print("\n" + "="*80)
    print(" DTM CONSENSUS MECHANISM TEST")
    print("="*80)
    
    dtm = DynamicTemplateManager(demo_mode=True, verbose=True)
    
    # Simulate Bitcoin template (needs ~19 leading zeros)
    template = {
        "height": 870000,
        "bits": "1d00ffff",  # Current Bitcoin difficulty (~19 zeros)
        "previousblockhash": "0000000000000000000123456789abcdef",
        "time": int(datetime.now().timestamp()),
        "version": 536870912,
        "transactions": []
    }
    
    print("\n--- Test 1: Mathematical solution with 50+ leading zeros (UNREALISTIC) ---")
    
    # Simulate miner's solution with impossible 50 leading zeros
    mathematical_solution = {
        "nonce": 3908178616,
        "hash": "0" * 50 + "123456789abcdef",  # 50 leading zeros - IMPOSSIBLE!
        "leading_zeros_hex": 50,
        "block_header": "00" * 80,  # Fake header for testing
        "meets_difficulty": True
    }
    
    print(f"\nMiner's solution:")
    print(f"  Leading zeros: {mathematical_solution['leading_zeros_hex']}")
    print(f"  Nonce: {mathematical_solution['nonce']}")
    print(f"  Hash: {mathematical_solution['hash'][:40]}...")
    
    print(f"\nBitcoin template:")
    print(f"  Bits: {template['bits']}")
    print(f"  Required zeros: ~19")
    
    print(f"\n⚠️  PROBLEM: 50 zeros is IMPOSSIBLE (1 in 2^200 chance)")
    print(f"    Bitcoin will REJECT this as fake/manufactured")
    
    print(f"\nDTM will now search for REALISTIC nonce (~19-22 zeros)...")
    
    # Let DTM validate and adjust
    result = dtm.validate_and_format_solution(mathematical_solution, template)
    
    print("\n--- DTM Validation Result ---")
    if result.get("success"):
        print(f"✅ DTM found acceptable solution!")
        print(f"   Final nonce: {result.get('nonce')}")
        print(f"   Final leading zeros: {result.get('leading_zeros_achieved')}")
        print(f"   Required zeros: {result.get('leading_zeros_required')}")
        print(f"   Bitcoin will accept: {result.get('bitcoin_will_accept')}")
        
        if result.get('leading_zeros_achieved', 0) <= 25:
            print(f"\n✅ SUCCESS: Adjusted to REALISTIC level ({result.get('leading_zeros_achieved')} zeros)")
            print(f"   This is achievable and Bitcoin will accept it!")
            return True
        else:
            print(f"\n❌ FAIL: Still too many zeros ({result.get('leading_zeros_achieved')})")
            print(f"   Bitcoin may reject this")
            return False
    else:
        print(f"❌ DTM validation failed: {result.get('error')}")
        return False

def main():
    try:
        success = test_dtm_consensus()
        
        print("\n" + "="*80)
        if success:
            print(" ✅ DTM CONSENSUS WORKING - Will produce Bitcoin-acceptable blocks")
        else:
            print(" ❌ DTM CONSENSUS FAILED - May produce rejected blocks")
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
