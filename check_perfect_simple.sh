#!/bin/bash
echo "=== CHECKING ALL MODES FOR W51 WEEK FOLDERS ==="
echo ""

for mode in "Test/Demo" "Test/Test mode" "Mining"; do
    echo "Mode: $mode"
    week_count=$(find "$mode" -path "*/W51/*" -type f 2>/dev/null | wc -l)
    week_dirs=$(find "$mode" -name "W51" -type d 2>/dev/null | wc -l)
    echo "  W51 directories: $week_dirs"
    echo "  Files in W51 folders: $week_count"
    
    # Check specific critical paths
    if [ -d "$mode/Mining/Ledgers/2025/12/W51" ]; then
        echo "  ✅ Ledgers week folder exists"
    else
        echo "  ❌ Ledgers week folder MISSING"
    fi
    
    # System path varies by mode
    if [[ "$mode" == Mining ]]; then
        sys_path="System"
    else
        sys_path="$mode/System"
    fi
    
    if [ -d "$sys_path/System_Reports/Brain/2025/12/W51" ]; then
        echo "  ✅ System Reports week folders exist"
    else
        echo "  ❌ System Reports week folders MISSING"
    fi
    echo ""
done
