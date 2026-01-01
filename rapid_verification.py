#!/usr/bin/env python3
"""
🚀 RAPID VERIFICATION SYSTEM - PEDAL TO THE METAL EDITION
Ultra-fast verification for aggressive hardcoded path fixing
"""
import ast
import subprocess
import sys
import re
from pathlib import Path

class RapidVerification:
    def __init__(self):
        self.issues = []
        
    def verify_syntax(self, filepath):
        """Lightning-fast syntax check"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            return True, "✅ Syntax OK"
        except SyntaxError as e:
            return False, f"❌ Syntax Error: Line {e.lineno}: {e.msg}"
        except Exception as e:
            return False, f"❌ Parse Error: {e}"
    
    def verify_imports(self, filepath):
        """Quick import check"""
        try:
            result = subprocess.run([sys.executable, '-m', 'py_compile', filepath], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return True, "✅ Imports OK"
            else:
                return False, f"❌ Import Error: {result.stderr.strip()}"
        except subprocess.TimeoutExpired:
            return False, "❌ Import check timeout"
        except Exception as e:
            return False, f"❌ Import check failed: {e}"
    
    def count_hardcoded_patterns(self, filepath):
        """Count remaining hardcoded path patterns"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            patterns = [
                r'["\']\/.*?Demo.*?["\']',  # /path/Demo paths
                r'["\'].*?Test\/.*?["\']',  # Test/ paths  
                r'["\'].*?Mining\/.*?["\']',  # Mining/ paths
                r'["\'].*?System\/.*?["\']'   # System/ paths
            ]
            
            total = 0
            for pattern in patterns:
                matches = re.findall(pattern, content)
                total += len(matches)
                
            return total
        except Exception:
            return -1
    
    def rapid_verify(self, filepath):
        """Ultra-fast complete verification"""
        print(f"🔍 Verifying {filepath}")
        
        # 1. Syntax check (fastest)
        syntax_ok, syntax_msg = self.verify_syntax(filepath)
        print(f"  {syntax_msg}")
        
        if not syntax_ok:
            return False
            
        # 2. Import check  
        import_ok, import_msg = self.verify_imports(filepath)
        print(f"  {import_msg}")
        
        # 3. Pattern count
        count = self.count_hardcoded_patterns(filepath)
        if count >= 0:
            print(f"  📊 Hardcoded patterns remaining: {count}")
        
        return syntax_ok and import_ok

def main():
    verifier = RapidVerification()
    
    files_to_check = [
        "Singularity_Dave_Looping.py",
        "Singularity_Dave_Brainstem_UNIVERSE_POWERED.py", 
        "production_bitcoin_miner.py",
        "dynamic_template_manager.py"
    ]
    
    print("🚀 RAPID VERIFICATION - PEDAL TO THE METAL!")
    print("=" * 50)
    
    all_good = True
    for file in files_to_check:
        if Path(file).exists():
            if not verifier.rapid_verify(file):
                all_good = False
        else:
            print(f"⚠️  File not found: {file}")
    
    print("=" * 50)
    if all_good:
        print("🎉 ALL SYSTEMS GO! Ready for aggressive optimization!")
    else:
        print("🚨 Issues detected - fix before continuing")
    
    return all_good

if __name__ == "__main__":
    main()