# CURRENT FOLDER STRUCTURE - REVIEW AND MARK WHAT TO KEEP/REMOVE

**INSTRUCTIONS:** 
- Put ✅ next to folders that should STAY
- Put ❌ next to folders that should be REMOVED
- Add notes about what's missing

---

## Mining/

```
Mining/
├── Aggregated/                    ←  noooooo
├── Aggregated_Index/              ← noooooo
├── Global_Aggregated/             ← noooooo
│   ├── Aggregated/                ← 
│   └── Aggregated_Index/          ← 
│
├── Ledgers/
    aggerated     (YYYY/MM/WXX/DD/HH hierarch nested folers with fiels at each level
    glboal file  (YYYY/MM/WXX/DD/HH hierarch nested folers with fiels at each level

    aggerated inex
    glboal file

│   ├── global_ledger.json         ← 
│   ├── global_math_proof.json     ← 
│   ├── 2025/12/W50/18/23/         ← (YYYY/MM/WXX/DD/HH hierarchy - has yearly_ledger.json, monthly_ledger.json, etc.)
│   ├── Aggregated/                ← 
│   │   └── 2025/12/W50/18/23/     ← (has aggregated files in hierarchy)
│   └── Aggregated_Index/          ← 
│       └── 2025/12/W50/18/23/     ← (has aggregated_index files in hierarchy)
│
├── Submission_Logs/
│   ├── global_submission_log.json ← MISSING - does not exist
│   ├── 2025/12/W50/18/23/         ← (YYYY/MM/WXX/DD/HH hierarchy - has yearly_submission.json, etc.)
│   ├── Aggregated/  
glboal file   ← 
│   │   └── 2025/12/W50/18/23/     ← (has aggregated files in hierarchy)
│   └── Aggregated_Index/ 
global file
│       └── 2025/12/W50/18/23/     ← (has aggregated_index files in hierarchy)
│
└── Temporary Template/            ← there fuckign shoudl be minign process oflder when looping fuckign statit. yes when th etemparoy tempael folder is made it wont' ahve the process fodler s bu tlooping shoudl fuckign make those.
```

---

## System/

```
System/
├── System_Reports/
│   ├── Aggregated/                ← 
│   │   ├── global_aggregated_report.json   ← 
│   │   └── 2025/12/W50/18/23/     ← (has aggregated files in hierarchy)
│   │
│   ├── Aggregated_Index/          ← 
│   │   ├── global_aggregated_index.json    ← 
│   │   └── 2025/12/W50/18/23/     ← (has aggregated_index files in hierarchy)
│   │
│   ├── Brain/
│   │   ├── global_brain_report.json        ← 
│   │   ├── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy - has yearly_brain_report.json, etc.)
│   │   ├── Aggregated/            ← no
│   │   └── Aggregated_Index/      ← no 
│   │
│   ├── Brainstem/
│   │   ├── global_brainstem_report.json    ← 
│   │   ├── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
│   │   ├── Aggregated/           no 
│   │   └── Aggregated_Index/   no ← 
│   │
│   ├── DTM/
│   │   ├── global_dtm_report.json          ← 
│   │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
│   │
│   ├── Looping/
│   │   ├── global_looping_report.json      ← 
│   │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
│   │
│   └── Miners/
│       ├── global_miners_report.json       ← 
│       ├── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
│       ├── Aggregated/            ← 
│       └── Aggregated_Index/      ← 
│
└── Error_Reports/
    ├── Aggregated/                ← 
    │   ├── global_aggregated_error.json    ← 
    │   └── 2025/12/W50/18/23/     ← (has aggregated files in hierarchy)
    │
    ├── Aggregated_Index/          ← 
    │   ├── global_aggregated_index.json    ← 
    │   └── 2025/12/W50/18/23/     ← (has aggregated_index files in hierarchy)
    │
    ├── Brain/
    │   ├── global_brain_error.json         ← 
    │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
    │
    ├── Brainstem/
    │   ├── global_brainstem_error.json     ← 
    │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
    │
    ├── DTM/
    │   ├── global_dtm_error.json           ← 
    │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
    │
    ├── Looping/
    │   ├── global_looping_error.json       ← 
    │   └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
    │
    └── Miners/
        ├── global_miners_error.json        ← 
        └── 2025/12/W50/18/23/     ← (YYYY/MM/WXX/DD/HH hierarchy)
```
also in system ├── Global_Aggregated/             ← 
│   ├── Aggregated/                ←  global file YYYY/MM/WXX/DD/HH hierarchy)
│   └── Aggregated_Index/          ← global file YYYY/MM/WXX/DD/HH hierarchy)
---

## FILE CREATORS (who makes what):

- **Looping**: submission_log files, system_report (looping), error_report (looping)
- **DTM**: math_proof files, ledger files, system_report (dtm), error_report (dtm)
- **Production Miner**: solution files, system_report (miners), error_report (miners)
- **Brainstem**: system_report (brainstem), error_report (brainstem)
- **Brain**: system_report (brain), error_report (brain), ALL aggregated reports, ALL aggregated_index reports

---

## EDIT THIS FILE AND SAVE YOUR CHANGES
