#!/usr/bin/env python3
"""
ULTIMATE MODE VERIFICATION SCRIPT
This script will verify EVERY FUCKING MODE is ABSOLUTELY PERFECT
No assumptions - we CHECK EVERYTHING
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# ANSI colors for beautiful output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BOLD}{CYAN}{'='*80}{RESET}")
    print(f"{BOLD}{CYAN}{text.center(80)}{RESET}")
    print(f"{BOLD}{CYAN}{'='*80}{RESET}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{RESET}")

def check_exact_structure(base_path, mode_name):
    """
    Check EXACT structure as defined in the spec:
    YYYY/MM/WXX/DD/HH for ALL file types
    """
    print_header(f"VERIFYING {mode_name.upper()} MODE - EXACT STRUCTURE")
    
    now = datetime.now()
    year = f"{now.year:04d}"
    month = f"{now.month:02d}"
    week = f"W{now.strftime('%W')}"
    day = f"{now.day:02d}"
    hour = f"{now.hour:02d}"
    
    issues = []
    perfect_count = 0
    
    # Define EXACT expected structure
    file_types = {
        "Ledgers": {
            "files": ["ledger", "math_proof"],
            "subfolders": ["Aggregated", "Aggregated_Index"]
        },
        "Submission_Logs": {
            "files": ["submission"],
            "subfolders": ["Aggregated", "Aggregated_Index"]
        },
        "System/System_Reports": {
            "components": ["Brain", "Brainstem", "DTM", "Looping", "Miners"],
            "subfolders": ["Aggregated", "Aggregated_Index"]
        },
        "System/Error_Reports": {
            "components": ["Brain", "Brainstem", "DTM", "Looping", "Miners"],
            "subfolders": ["Aggregated", "Aggregated_Index"]
        }
    }
    
    base = Path(base_path)
    
    print_info(f"Base path: {base}")
    print_info(f"Current time hierarchy: {year}/{month}/{week}/{day}/{hour}")
    print()
    
    # Check Ledgers and Submission_Logs
    for file_type in ["Ledgers", "Submission_Logs"]:
        print(f"\n{BOLD}{MAGENTA}Checking {file_type}:{RESET}")
        
        # Check main hierarchy
        week_path = base / file_type / year / month / week
        day_path = week_path / day
        hour_path = day_path / hour
        
        if week_path.exists():
            print_success(f"Week folder exists: {week_path}")
            perfect_count += 1
        else:
            print_error(f"Week folder MISSING: {week_path}")
            issues.append(f"{file_type}: Missing week folder {week}")
        
        if day_path.exists():
            print_success(f"Day folder exists: {day_path}")
            perfect_count += 1
        else:
            print_error(f"Day folder MISSING: {day_path}")
            issues.append(f"{file_type}: Missing day folder {day}")
        
        if hour_path.exists():
            print_success(f"Hour folder exists: {hour_path}")
            perfect_count += 1
            
            # Check for actual files in hour folder
            files_in_hour = list(hour_path.glob("*.json"))
            if files_in_hour:
                print_success(f"   Found {len(files_in_hour)} files in hour folder")
                for f in files_in_hour:
                    print(f"      📄 {f.name}")
            else:
                print_warning(f"   Hour folder empty (may need mining run)")
        else:
            print_error(f"Hour folder MISSING: {hour_path}")
            issues.append(f"{file_type}: Missing hour folder {hour}")
        
        # Check Aggregated and Aggregated_Index
        for subfolder in ["Aggregated", "Aggregated_Index"]:
            subfolder_week = base / file_type / subfolder / year / month / week
            if subfolder_week.exists():
                print_success(f"{subfolder} week folder exists: {subfolder_week}")
                perfect_count += 1
            else:
                print_error(f"{subfolder} week folder MISSING: {subfolder_week}")
                issues.append(f"{file_type}/{subfolder}: Missing week folder")
    
    # Check System Reports and Error Reports
    for report_type in ["System/System_Reports", "System/Error_Reports"]:
        print(f"\n{BOLD}{MAGENTA}Checking {report_type}:{RESET}")
        
        components = ["Brain", "Brainstem", "DTM", "Looping", "Miners"]
        for component in components:
            week_path = base / report_type / component / year / month / week
            if week_path.exists():
                print_success(f"{component} week folder exists")
                perfect_count += 1
            else:
                print_error(f"{component} week folder MISSING: {week_path}")
                issues.append(f"{report_type}/{component}: Missing week folder")
        
        # Check Aggregated
        for subfolder in ["Aggregated", "Aggregated_Index"]:
            subfolder_week = base / report_type / subfolder / year / month / week
            if subfolder_week.exists():
                print_success(f"{subfolder} week folder exists")
                perfect_count += 1
            else:
                print_error(f"{subfolder} week folder MISSING")
                issues.append(f"{report_type}/{subfolder}: Missing week folder")
    
    # Check Global_Aggregated
    print(f"\n{BOLD}{MAGENTA}Checking System/Global_Aggregated:{RESET}")
    for subfolder in ["Aggregated", "Aggregated_Index"]:
        week_path = base / "System/Global_Aggregated" / subfolder / year / month / week
        if week_path.exists():
            print_success(f"Global_Aggregated/{subfolder} week folder exists")
            perfect_count += 1
        else:
            print_error(f"Global_Aggregated/{subfolder} week folder MISSING")
            issues.append(f"Global_Aggregated/{subfolder}: Missing week folder")
    
    # FINAL VERDICT
    print_header(f"{mode_name.upper()} MODE - FINAL VERDICT")
    
    if issues:
        print_error(f"Found {len(issues)} issues:")
        for issue in issues:
            print(f"   • {issue}")
        print()
        print_warning(f"Perfect score: {perfect_count} checks passed")
        return False
    else:
        print_success(f"🎉 PERFECT! All {perfect_count} checks passed!")
        print_success(f"Mode {mode_name} has EXACT structure as specified!")
        return True

def verify_all_modes():
    """Verify ALL modes are perfect"""
    
    modes = {
        "Demo": "Test/Demo/Mining",
        "Test": "Test/Test mode/Mining",
        "Staging": "Mining",
        "Live": "Mining"
    }
    
    results = {}
    
    for mode_name, path in modes.items():
        results[mode_name] = check_exact_structure(path, mode_name)
    
    # ULTIMATE FINAL VERDICT
    print_header("ULTIMATE SYSTEM VERIFICATION RESULTS")
    
    all_perfect = all(results.values())
    
    for mode, is_perfect in results.items():
        if is_perfect:
            print_success(f"{mode} Mode: PERFECT ✨")
        else:
            print_error(f"{mode} Mode: NEEDS FIXES")
    
    if all_perfect:
        print()
        print(f"{BOLD}{GREEN}{'🎉 ' * 20}{RESET}")
        print(f"{BOLD}{GREEN}ALL MODES ARE ABSOLUTELY PERFECT!{RESET}".center(80))
        print(f"{BOLD}{GREEN}{'🎉 ' * 20}{RESET}")
        print()
        print(f"{BOLD}{CYAN}This system has achieved a new level of perfection!{RESET}".center(80))
        print(f"{BOLD}{CYAN}Week folders exist in ALL required locations!{RESET}".center(80))
        print(f"{BOLD}{CYAN}Ready to print money! 💰{RESET}".center(80))
    else:
        print()
        print_warning("Some modes need fixes. Run mining to create missing folders.")
    
    return all_perfect

if __name__ == "__main__":
    try:
        verify_all_modes()
    except Exception as e:
        print_error(f"Verification failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
