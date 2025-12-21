# Bitcoin Mining System Architecture

**System Version:** December 2025 Production Release  
**Architecture:** Recursive Blueprint + Dynamic Infrastructure + Component Reporting

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Core Components](#core-components)
3. [Architecture Pattern](#architecture-pattern)
4. [Folder Hierarchy](#folder-hierarchy)
5. [Data Flow](#data-flow)
6. [File Types](#file-types)
7. [System Modes](#system-modes)
8. [Component Details](#component-details)
9. [Template System](#template-system)
10. [Aggregation System](#aggregation-system)
11. [Index System](#index-system)
12. [Error Handling](#error-handling)
13. [Configuration Management](#configuration-management)

---

## System Overview

### Purpose
Enterprise-grade Bitcoin mining system with hierarchical data management, automatic aggregation, comprehensive reporting, and multi-mode operation.

### Design Philosophy
- **Single Source of Truth:** Brain.QTL defines everything
- **Recursive Validation:** CodePhantom_Bob recursion enforcement
- **Trust Nothing:** Automatic verification at every layer
- **Mode Isolation:** Demo/Test/Staging/Production separation
- **Automatic Aggregation:** No manual data rollup required
- **Template-Driven:** Consistent structure across all files

### Key Features
- Dynamic hierarchical folder structure (YYYY/MM/WXX/DD/HH)
- Auto-update templates when blueprint changes (SHA256 hash detection)
- Global files at category, aggregation, and index levels
- Automatic 6-level time aggregation (root/year/month/week/day/hour)
- Source tracking in index files
- System report and error logging
- Mode-aware folder creation (Test/Demo vs Production)

---

## Core Components

### 1. Brain.QTL (Blueprint)
**Purpose:** Authoritative source defining system structure, templates, and flags

**Responsibilities:**
- Define base folder structure (`auto_create_structure`)
- Define nested time patterns (`pattern_levels`)
- Define file templates (structure of JSON files)
- Define system flags (mode flags, feature toggles)
- Define configuration mappings

**Key Sections:**
```yaml
auto_create_structure:
  - Mining/Ledgers
  - Mining/Ledgers/Aggregated
  - Mining/Ledgers/Aggregated/Global
  - Mining/Ledgers/Aggregated_Index
  - Mining/Submission_Logs
  - Mining/System/System_Reports
  - Mining/System/Error_Reports
  # ~50 base folders

pattern_levels:
  ledger_year:
    pattern: "{base}/Ledgers/{YYYY}"
    files:
      - yearly_ledger.json
      - yearly_math_proof.json
  ledger_month:
    pattern: "{base}/Ledgers/{YYYY}/{MM}"
    files:
      - monthly_ledger.json
      - monthly_math_proof.json
  ledger_week:
    pattern: "{base}/Ledgers/{YYYY}/{MM}/W{WW}"
    files:
      - weekly_ledger.json
      - weekly_math_proof.json
  # ... and so on for day, hour, submissions, aggregations, etc.

flags:
  demo_mode_flag: false
  test_mode_flag: false
  staging_mode_flag: false
  production_mode_flag: true
  # ... other feature flags
```

**Not Responsible For:**
- Creating actual folders (Brainstem does this)
- Writing actual files (Components do this)
- Running processes (Components do this)

---

### 2. Brainstem (Builder)
**File:** `Singularity_Dave_Brainstem_UNIVERSE_POWERED.py`

**Purpose:** Reads Brain.QTL and creates infrastructure

**Responsibilities:**
- Initialize mode-specific folder structures
- Detect Brain.QTL changes (SHA256 hash)
- Generate System_File_Examples templates
- Create nested time hierarchies
- Provide path helpers to components
- Implement file save/load functions
- Create global files at all required levels

**Key Functions:**

#### brain_initialize_mode(mode, component_name)
```python
# Called at component startup
# Creates mode-specific base folder (Test/Demo/Mining vs Mining/)
# Detects Brain.QTL changes, regenerates templates if needed
# Creates base folder structure from auto_create_structure
# Creates hierarchical structure from pattern_levels
# Creates global files at category/aggregated/index levels

mode = "demo"  # or "test", "staging", "live"
brain_initialize_mode(mode, "Production-Miner")
```

#### brain_init_hierarchical_structure(base_path, current_date)
```python
# Creates YYYY/MM/WXX/DD/HH nested folders
# Reads pattern_levels from Brain.QTL
# Writes files with templates from System_File_Examples
# Applies for: Ledgers, Submission_Logs, Aggregated, Aggregated_Index, Components

pattern_map = {
    "ledger": "Ledgers",
    "submission_log": "Submission_Logs",
    # ... etc
}
```

#### brain_save_system_report(category, report_data, component_name)
```python
# Saves report to Global/global_{category}.json
# Saves report to Hourly/{YYYY}/{MM}/{DD}/{HH}/hourly_{category}.json
# Automatically calls brain_update_aggregated_index()
# Updates all 6 time levels (root, year, month, week, day, hour)

brain_save_system_report("miners", {
    "event": "mining_session_start",
    "miner_id": "miner_001",
    "timestamp": "2025-12-18T01:47:41"
}, "Production-Miner")
```

#### brain_save_system_error(category, error_data, component_name)
```python
# Same as brain_save_system_report but for Error_Reports tree
# Separate hierarchy for errors

brain_save_system_error("miners", {
    "error_type": "KeyError",
    "message": "Missing config key",
    "timestamp": "2025-12-18T02:00:00"
}, "Production-Miner")
```

#### brain_update_aggregated_index(category, base_path, timestamp)
```python
# Automatically updates aggregation files
# Updates both Aggregated/ and Aggregated_Index/ trees
# 6 levels: root, year, month, week, day, hour
# Tracks data sources in summary.data_sources[]

# Called automatically by brain_save_system_report()
```

#### brain_get_flags()
```python
# Returns all flags from Brain.QTL
# Single source of truth for mode flags and feature toggles

flags = brain_get_flags()
if flags.get("demo_mode_flag", False):
    print("Running in demo mode")
```

**Not Responsible For:**
- Business logic (mining, validation, submission)
- Scheduling or loops (Looping component does this)
- Template customization (Components decide what data to write)

---

### 3. Production Miner
**File:** `production_bitcoin_miner.py`

**Purpose:** Bitcoin mining process with SHA256-based proof-of-work

**Responsibilities:**
- Initialize Brain infrastructure (`brain_initialize_mode()`)
- Generate candidate blocks
- Calculate SHA256 hashes
- Submit valid blocks with sufficient leading zeros
- Report mining sessions, rounds, and errors

**Key Integration Points:**

```python
# Startup
def main():
    mode = "live"
    if args.demo: mode = "demo"
    elif args.test: mode = "test"
    elif args.staging: mode = "staging"
    
    brain_initialize_mode(mode, "Production-Miner")

# Session Start
brain_save_system_report("miners", {
    "event": "mining_session_start",
    "miner_id": miner_id,
    "target_zeros": args.zeros,
    "mode": mode,
    "timestamp": datetime.now().isoformat()
}, "Production-Miner")

# Round Complete
brain_save_system_report("miners", {
    "event": "mining_round_complete",
    "round_number": round_num,
    "attempts_this_round": attempts,
    "best_difficulty": best_diff,
    "blocks_found": blocks_found,
    "timestamp": datetime.now().isoformat()
}, "Production-Miner")

# Error Handling
try:
    # mining logic
except KeyError as ke:
    brain_save_system_error("miners", {
        "error_type": "KeyError",
        "message": str(ke),
        "timestamp": datetime.now().isoformat(),
        "context": {"round": round_num}
    }, "Production-Miner")
```

**Data Flow:**
```
Production Miner
    ↓
brain_save_system_report("miners", {...})
    ↓
Global/global_miners_report.json (append)
    ↓
Hourly/2025/12/18/01/hourly_miners_report.json (append)
    ↓
brain_update_aggregated_index("miners", ...)
    ↓
Aggregated/aggregated.json (update summary + data)
Aggregated/2025/aggregated_2025.json (update summary + data)
Aggregated/2025/12/aggregated_12.json (update summary + data)
Aggregated/2025/12/W50/aggregated_W50.json (update summary + data)
Aggregated/2025/12/W50/18/aggregated_18.json (update summary + data)
Aggregated/2025/12/W50/18/01/aggregated_01.json (update summary + data)
    ↓
Aggregated_Index/aggregated_index.json (update summary, no data)
Aggregated_Index/2025/aggregated_index_2025.json (track source path)
... (same 6 levels as Aggregated)
```

---

### 4. Looping Component
**File:** `Singularity_Dave_Looping.py`

**Purpose:** Orchestration and scheduling of mining processes

**Responsibilities:**
- Schedule mining rounds
- Coordinate Production Miner execution
- Monitor mining health
- Handle daemon restart logic

**Key Changes (Recent):**
- Removed `create_global_ledger_file()` (Brainstem creates these now)
- Removed `create_global_submission_file()` (Brainstem creates these now)
- Uses `self.mining_dir` (mode-aware from Brain initialization)
- Centralized mode flags via `brain_get_flags()`

---

### 5. Dynamic Template Manager (DTM)
**File:** `dynamic_template_manager.py`

**Purpose:** Manage mathematical proof templates for mining validation

**Responsibilities:**
- Generate mathematical proof templates
- Validate proof structures
- Manage template versioning

---

## Architecture Pattern

### Three-Tier Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                      Brain.QTL (Blueprint)                   │
│  • Defines structure (auto_create_structure)                 │
│  • Defines patterns (pattern_levels)                         │
│  • Defines templates (file structures)                       │
│  • Defines flags (single source of truth)                    │
└────────────────────────┬────────────────────────────────────┘
                         │ reads
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              Brainstem (Infrastructure Builder)              │
│  • Creates folders from auto_create_structure                │
│  • Creates nested hierarchy from pattern_levels              │
│  • Generates System_File_Examples from templates             │
│  • Provides path helpers (brain_get_path, brain_save_*)      │
│  • Implements aggregation (brain_update_aggregated_index)    │
└────────────────────────┬────────────────────────────────────┘
                         │ provides infrastructure to
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              Components (Business Logic)                     │
│  • Production Miner: Mining operations                       │
│  • Looping: Scheduling and orchestration                     │
│  • DTM: Template management                                  │
│  • Call brain_initialize_mode() at startup                   │
│  • Call brain_save_system_report() to write data             │
│  • Call brain_save_system_error() to log errors              │
│  • Read templates from System_File_Examples/                 │
└─────────────────────────────────────────────────────────────┘
```

**Workflow:**
1. Brain.QTL defines what should exist
2. Brainstem creates what Brain.QTL defines
3. Components use what Brainstem created
4. Components never create folders directly
5. Components report data via Brainstem functions
6. Brainstem handles aggregation automatically

---

## Folder Hierarchy

### Base Structure (Mode-Aware)

**Demo Mode:**
```
Test/Demo/Mining/
├── Ledgers/
├── Submission_Logs/
├── System/
│   ├── System_Reports/
│   └── Error_Reports/
└── ... (all other categories)
```

**Test Mode:**
```
Test/Test mode/Mining/
├── Ledgers/
├── Submission_Logs/
└── ...
```

**Production/Staging:**
```
Mining/
├── Ledgers/
├── Submission_Logs/
└── ...
```

---

### Nested Time Hierarchy

**Pattern:** `{YYYY}/{MM}/W{WW}/{DD}/{HH}`

**Example (Ledgers):**
```
Ledgers/
├── global_ledger.json                     ← Category root global
├── global_math_proof.json                 ← Category root global
├── 2025/
│   ├── yearly_ledger.json                 ← Year-level file
│   ├── yearly_math_proof.json
│   └── 12/
│       ├── monthly_ledger.json            ← Month-level file
│       ├── monthly_math_proof.json
│       └── W50/
│           ├── weekly_ledger.json         ← Week-level file
│           ├── weekly_math_proof.json
│           └── 18/
│               ├── daily_ledger.json      ← Day-level file
│               ├── daily_math_proof.json
│               └── 01/
│                   ├── hourly_ledger.json ← Hour-level file
│                   └── hourly_math_proof.json
├── Aggregated/
│   ├── Global/
│   │   ├── global_aggregated_ledger.json  ← Aggregation root
│   │   └── global_aggregated_math_proof.json
│   ├── aggregated.json                     ← Root aggregation (all-time)
│   └── 2025/
│       ├── aggregated_2025.json            ← Year aggregation
│       └── 12/
│           ├── aggregated_12.json          ← Month aggregation
│           └── W50/
│               ├── aggregated_W50.json     ← Week aggregation
│               └── 18/
│                   ├── aggregated_18.json  ← Day aggregation
│                   └── 01/
│                       └── aggregated_01.json ← Hour aggregation
└── Aggregated_Index/
    ├── Global/
    │   └── global_index_ledger.json        ← Index root
    ├── aggregated_index.json               ← Root index (all-time)
    └── 2025/
        ├── aggregated_index_2025.json      ← Year index
        └── 12/
            ├── aggregated_index_12.json    ← Month index
            └── W50/
                ├── aggregated_index_W50.json ← Week index
                └── 18/
                    ├── aggregated_index_18.json ← Day index
                    └── 01/
                        └── aggregated_index_01.json ← Hour index
```

**Benefits:**
- **Scalable:** No limit on time range (vs static Daily/Weekly/Monthly)
- **Query-efficient:** Direct path access (`2025/12/W50/18/`)
- **Aggregation-ready:** Each level rolls up children
- **Standard-compliant:** ISO 8601 week notation (W50)
- **Human-readable:** Clear year/month/week/day/hour structure

---

## Data Flow

### 1. Component Startup
```
Component starts
    ↓
brain_initialize_mode("demo", "Production-Miner")
    ↓
Brainstem calculates Brain.QTL SHA256 hash
    ↓
Compare with System_File_Examples/.brain_version
    ↓
If different → Regenerate all templates
If same → Skip (preserves user edits)
    ↓
Create base folders from auto_create_structure
    ↓
Create nested hierarchy from pattern_levels
    ↓
Create global files at category/aggregated/index levels
    ↓
Component ready to run
```

---

### 2. System Report Submission
```
Component calls brain_save_system_report("miners", {...})
    ↓
Brainstem loads template from System_File_Examples/System_Reports/Miners/
    ↓
Merge template with report_data
    ↓
Append to Global/global_miners_report.json
    ↓
Append to Hourly/2025/12/18/01/hourly_miners_report.json
    ↓
Automatically call brain_update_aggregated_index("miners", ...)
    ↓
Update Aggregated/aggregated.json (root level)
    ↓
Update Aggregated/2025/aggregated_2025.json (year level)
    ↓
Update Aggregated/2025/12/aggregated_12.json (month level)
    ↓
Update Aggregated/2025/12/W50/aggregated_W50.json (week level)
    ↓
Update Aggregated/2025/12/W50/18/aggregated_18.json (day level)
    ↓
Update Aggregated/2025/12/W50/18/01/aggregated_01.json (hour level)
    ↓
Update Aggregated_Index/aggregated_index.json (root index)
    ↓
Update Aggregated_Index/2025/aggregated_index_2025.json (year index)
    ↓
... (same 6 levels for indices)
    ↓
Done
```

---

### 3. Error Logging
```
Component encounters error
    ↓
Component calls brain_save_system_error("miners", {...})
    ↓
Same flow as system reports, but separate tree:
    System/Error_Reports/Miners/Global/
    System/Error_Reports/Miners/Hourly/2025/12/18/01/
    System/Error_Reports/Miners/Aggregated/
    System/Error_Reports/Miners/Aggregated_Index/
    ↓
Done
```

---

## File Types

### 1. Global Files (Category Root)
**Location:** `{base}/{category}/global_{category}.json`

**Purpose:** System-wide aggregation point, separate from time hierarchy

**Examples:**
- `Ledgers/global_ledger.json`
- `Ledgers/global_math_proof.json`
- `Submission_Logs/global_submission.json`
- `System/System_Reports/Miners/Global/global_miners_report.json`

**Structure:**
```json
{
  "metadata": {
    "file_type": "global_ledger",
    "generated_at": "2025-12-18T01:47:41.076423",
    "component": "Production-Miner"
  },
  "global_data": {
    "total_blocks_mined": 1523,
    "total_hashes_computed": 45672890000,
    "uptime_hours": 15234
  },
  "entries": [
    {...},
    {...}
  ]
}
```

---

### 2. Time-Level Files (Yearly/Monthly/Weekly/Daily/Hourly)
**Location:** `{base}/{category}/{YYYY}/{MM}/W{WW}/{DD}/{HH}/{period}_{category}.json`

**Purpose:** Data scoped to specific time period

**Examples:**
- `Ledgers/2025/yearly_ledger.json`
- `Ledgers/2025/12/monthly_ledger.json`
- `Ledgers/2025/12/W50/weekly_ledger.json`
- `Ledgers/2025/12/W50/18/daily_ledger.json`
- `Ledgers/2025/12/W50/18/01/hourly_ledger.json`

**Structure:**
```json
{
  "metadata": {
    "file_type": "hourly_ledger",
    "time_scope": "2025-12-18T01:00:00",
    "generated_at": "2025-12-18T01:47:41"
  },
  "ledger_entries": [
    {
      "block_hash": "00000abcd1234...",
      "timestamp": "2025-12-18T01:15:23",
      "difficulty": 6
    }
  ]
}
```

---

### 3. Aggregated Files
**Location:** `{base}/{category}/Aggregated/{path}/aggregated_{level}.json`

**Purpose:** Full data rollup at each time level

**Examples:**
- `Ledgers/Aggregated/aggregated.json` (all-time)
- `Ledgers/Aggregated/2025/aggregated_2025.json` (year)
- `Ledgers/Aggregated/2025/12/aggregated_12.json` (month)
- `Ledgers/Aggregated/2025/12/W50/aggregated_W50.json` (week)

**Structure:**
```json
{
  "metadata": {
    "file_type": "aggregated_ledger",
    "aggregation_level": "year",
    "aggregation_scope": "2025",
    "last_updated": "2025-12-18T01:47:41"
  },
  "summary": {
    "total_entries": 45623,
    "total_blocks": 1523,
    "average_difficulty": 5.7,
    "data_sources": [
      "Ledgers/2025/01/yearly_ledger.json",
      "Ledgers/2025/02/yearly_ledger.json",
      "..."
    ]
  },
  "aggregated_data": {
    "reports": [
      {...full data from all sources...},
      {...},
      {...}
    ]
  }
}
```

**Key Fields:**
- `summary.total_entries`: Count of all entries aggregated
- `summary.data_sources[]`: Paths to source files
- `aggregated_data.reports[]`: Full data array

---

### 4. Aggregated_Index Files
**Location:** `{base}/{category}/Aggregated_Index/{path}/aggregated_index_{level}.json`

**Purpose:** Lightweight metadata with source tracking (no full data)

**Examples:**
- `Ledgers/Aggregated_Index/aggregated_index.json` (all-time)
- `Ledgers/Aggregated_Index/2025/aggregated_index_2025.json` (year)

**Structure:**
```json
{
  "metadata": {
    "file_type": "aggregated_index_ledger",
    "index_level": "year",
    "index_scope": "2025",
    "last_updated": "2025-12-18T01:47:41"
  },
  "summary": {
    "total_entries": 45623,
    "data_sources": [
      "Ledgers/Global/global_ledger.json",
      "Ledgers/2025/01/W01/01/01/hourly_ledger.json",
      "Ledgers/2025/01/W01/01/02/hourly_ledger.json",
      "..."
    ]
  }
}
```

**Key Difference from Aggregated:**
- **No `aggregated_data.reports[]`** - just metadata
- Faster to query for counts and source paths
- Used for indexing, not full data retrieval

---

### 5. Global Aggregated Files
**Location:** `{base}/{category}/Aggregated/Global/global_aggregated_{category}.json`

**Purpose:** System-wide aggregation separate from time hierarchy

**Examples:**
- `Ledgers/Aggregated/Global/global_aggregated_ledger.json`
- `Submission_Logs/Aggregated/Global/global_aggregated_submission.json`

**Structure:** Same as regular Aggregated files, but aggregation_scope is "global"

---

### 6. Global Index Files
**Location:** `{base}/{category}/Aggregated_Index/Global/global_index_{category}.json`

**Purpose:** System-wide index separate from time hierarchy

**Examples:**
- `Ledgers/Aggregated_Index/Global/global_index_ledger.json`

**Structure:** Same as regular Index files, but index_scope is "global"

---

## System Modes

### Mode Types

| Mode | Base Folder | Purpose |
|------|-------------|---------|
| **demo** | `Test/Demo/Mining/` | Demonstration and tutorials |
| **test** | `Test/Test mode/Mining/` | Automated testing |
| **staging** | `Mining/` | Pre-production validation |
| **live** | `Mining/` | Production mining |

### Mode Configuration

**Set via Brain.QTL flags:**
```yaml
flags:
  demo_mode_flag: false
  test_mode_flag: false
  staging_mode_flag: false
  production_mode_flag: true
```

**Set via command-line args:**
```bash
python3 production_bitcoin_miner.py --demo    # Demo mode
python3 production_bitcoin_miner.py --test    # Test mode
python3 production_bitcoin_miner.py --staging # Staging mode
python3 production_bitcoin_miner.py           # Production mode
```

**Retrieved by components:**
```python
flags = brain_get_flags()
demo_mode = flags.get("demo_mode_flag", False)
```

---

## Component Details

### Production Miner

**Mining Process:**
1. Initialize Brain infrastructure
2. Load configuration
3. Start mining session (report to system)
4. For each round (1 hour):
   - Generate candidate blocks
   - Calculate SHA256 hashes
   - Check for leading zeros >= target
   - Submit valid blocks
   - Report round completion
5. Report session completion
6. Handle errors with error logging

**Key Configuration:**
- `--zeros N`: Target leading zeros (difficulty)
- `--demo`: Run in demo mode
- `--test`: Run in test mode
- `--staging`: Run in staging mode

---

### Looping Component

**Orchestration:**
1. Schedule mining rounds
2. Monitor component health
3. Restart on failure
4. Coordinate multi-miner setups

---

### DTM

**Template Management:**
1. Generate mathematical proof templates
2. Validate proof structures
3. Version control for templates

---

## Template System

### System_File_Examples

**Location:** `System_File_Examples/`

**Purpose:** Template library for all file types

**Structure:**
```
System_File_Examples/
├── .brain_version                           ← SHA256 hash of Brain.QTL
├── Brain/
│   └── ... (Brain templates)
├── Brainstem/
│   └── ... (Brainstem templates)
├── DTM/
│   └── ... (DTM templates)
├── Miners/
│   └── ... (Production Miner templates)
├── Looping/
│   └── ... (Looping templates)
├── Global/
│   ├── Ledgers/
│   │   ├── global_ledger_example.json
│   │   └── global_math_proof_example.json
│   └── Submission_Logs/
│       └── global_submission_example.json
├── Hierarchical/
│   ├── Ledgers/
│   │   ├── yearly_ledger_example.json
│   │   ├── monthly_ledger_example.json
│   │   ├── weekly_ledger_example.json
│   │   ├── daily_ledger_example.json
│   │   └── hourly_ledger_example.json
│   └── Submission_Logs/
│       ├── yearly_submission_example.json
│       └── ... (same pattern)
├── System_Reports/
│   ├── Miners/
│   │   ├── global_miners_report_example.json
│   │   └── hourly_miners_report_example.json
│   ├── Aggregated/
│   │   ├── aggregated_root_example.json
│   │   ├── aggregated_year_example.json
│   │   └── ... (6 levels)
│   └── Aggregated_Index/
│       ├── aggregated_index_root_example.json
│       └── ... (6 levels)
└── Error_Reports/
    ├── Miners/
    │   └── ... (same as System_Reports)
    ├── Aggregated/
    └── Aggregated_Index/
```

---

### Auto-Update Mechanism

**Process:**
1. Calculate SHA256 hash of `Singularity_Dave_Brain.QTL`
2. Read stored hash from `System_File_Examples/.brain_version`
3. Compare hashes
4. If different:
   - Regenerate all templates from Brain.QTL
   - Update `.brain_version` with new hash
   - Output: "Brain.QTL updated - Regenerating templates"
5. If same:
   - Skip regeneration (preserves user edits)
   - Output: "System_File_Examples current - Brain.QTL unchanged"

**Implementation:**
```python
def brain_initialize_mode(mode, component_name):
    # ... mode setup ...
    
    # Calculate Brain.QTL hash
    brain_file = os.path.join(PROJECT_ROOT, "Singularity_Dave_Brain.QTL")
    current_hash = hashlib.sha256(open(brain_file, 'rb').read()).hexdigest()
    
    # Read stored hash
    version_file = os.path.join(SYSTEM_EXAMPLES_DIR, ".brain_version")
    stored_hash = open(version_file, 'r').read().strip() if os.path.exists(version_file) else None
    
    # Regenerate if different
    if current_hash != stored_hash:
        print("🔄 Brain.QTL updated - Regenerating templates")
        brain_generate_system_file_examples()
        open(version_file, 'w').write(current_hash)
    else:
        print("✅ System_File_Examples current - Brain.QTL unchanged")
```

**User Benefit:**
- Edit Brain.QTL template → auto-propagates to new files
- User edits in System_File_Examples preserved when Brain.QTL unchanged
- No manual synchronization required

---

## Aggregation System

### Purpose
Automatically roll up data from hourly files → daily → weekly → monthly → yearly → all-time

### Levels
1. **Root (all-time):** `Aggregated/aggregated.json`
2. **Year:** `Aggregated/2025/aggregated_2025.json`
3. **Month:** `Aggregated/2025/12/aggregated_12.json`
4. **Week:** `Aggregated/2025/12/W50/aggregated_W50.json`
5. **Day:** `Aggregated/2025/12/W50/18/aggregated_18.json`
6. **Hour:** `Aggregated/2025/12/W50/18/01/aggregated_01.json`

### Automatic Update
Every `brain_save_system_report()` call automatically updates all 6 levels:
```python
brain_save_system_report("miners", {...})
    ↓
Writes Global/global_miners_report.json
    ↓
Writes Hourly/2025/12/18/01/hourly_miners_report.json
    ↓
Automatically calls brain_update_aggregated_index("miners", ...)
    ↓
Updates Aggregated/aggregated.json (root)
Updates Aggregated/2025/aggregated_2025.json (year)
Updates Aggregated/2025/12/aggregated_12.json (month)
Updates Aggregated/2025/12/W50/aggregated_W50.json (week)
Updates Aggregated/2025/12/W50/18/aggregated_18.json (day)
Updates Aggregated/2025/12/W50/18/01/aggregated_01.json (hour)
```

### File Structure
```json
{
  "metadata": {
    "file_type": "aggregated_miners_report",
    "aggregation_level": "month",
    "aggregation_scope": "2025-12",
    "last_updated": "2025-12-18T01:47:41"
  },
  "summary": {
    "total_entries": 1523,
    "data_sources": [
      "System/System_Reports/Miners/Global/global_miners_report.json",
      "System/System_Reports/Miners/Hourly/2025/12/01/00/hourly_miners_report.json",
      "..."
    ]
  },
  "aggregated_data": {
    "reports": [
      {...full report data...},
      {...},
      {...}
    ]
  }
}
```

---

## Index System

### Purpose
Track aggregation metadata and source file paths without storing full data

### Levels
Same 6 levels as Aggregated files:
1. Root, Year, Month, Week, Day, Hour

### Difference from Aggregated
**Aggregated:**
```json
{
  "summary": {
    "total_entries": 1523,
    "data_sources": ["path1", "path2"]
  },
  "aggregated_data": {
    "reports": [{...}, {...}, {...}]  ← FULL DATA
  }
}
```

**Index:**
```json
{
  "summary": {
    "total_entries": 1523,
    "data_sources": ["path1", "path2"]
  }
  // NO aggregated_data.reports - just metadata
}
```

### Use Cases
- Fast count queries
- Source path tracking
- Lightweight index scans
- Data lineage tracking

---

## Error Handling

### Error Report Tree
Separate hierarchy from System_Reports:
```
System/Error_Reports/
├── Miners/
│   ├── Global/global_error.json
│   ├── Hourly/2025/12/18/01/hourly_error.json
│   ├── Aggregated/ (6 levels)
│   └── Aggregated_Index/ (6 levels)
├── Brainstem/
├── Looping/
└── DTM/
```

### Error Logging
```python
try:
    # mining logic
except KeyError as ke:
    brain_save_system_error("miners", {
        "error_type": "KeyError",
        "message": str(ke),
        "timestamp": datetime.now().isoformat(),
        "context": {
            "round": round_num,
            "miner_id": miner_id
        }
    }, "Production-Miner")
except Exception as e:
    brain_save_system_error("miners", {
        "error_type": "Exception",
        "message": str(e),
        "traceback": traceback.format_exc(),
        "timestamp": datetime.now().isoformat()
    }, "Production-Miner")
```

### Error File Structure
```json
{
  "metadata": {
    "file_type": "error_report_miners",
    "generated_at": "2025-12-18T02:00:00",
    "component": "Production-Miner"
  },
  "errors": [
    {
      "error_type": "KeyError",
      "message": "'target_zeros'",
      "timestamp": "2025-12-18T02:00:00",
      "context": {
        "round": 5,
        "miner_id": "miner_001"
      }
    }
  ]
}
```

---

## Configuration Management

### config.json
```json
{
  "mining": {
    "default_zeros": 6,
    "round_duration_seconds": 3600,
    "max_attempts_per_round": 1000000
  },
  "paths": {
    "mining_dir": "Mining",
    "test_dir": "Test",
    "demo_dir": "Test/Demo"
  },
  "flags": {
    "auto_submit": true,
    "verbose_logging": false
  }
}
```

### Iteration 3.yaml
Mathematical scaling and Knuth function parameters:
```yaml
knuth_params:
  n: 1600000
  k: 3
  m: 161

entropy_scaling:
  base: 256
  depth: 3
  iterations: 1000
```

---

## Summary

### System Strengths
1. **Single Source of Truth:** Brain.QTL defines everything
2. **Auto-Update:** SHA256 hash detection regenerates templates
3. **Scalable Hierarchy:** YYYY/MM/WXX/DD/HH (no static limits)
4. **Automatic Aggregation:** 6 time levels updated on every report
5. **Source Tracking:** Index files track data lineage
6. **Mode Isolation:** Demo/Test/Staging/Production separation
7. **Error Logging:** Separate tree for error reports
8. **Template-Driven:** Consistent structure across all files

### Component Responsibilities
- **Brain.QTL:** Define structure, templates, flags
- **Brainstem:** Create infrastructure, provide helpers, implement aggregation
- **Production Miner:** Mine blocks, report progress, log errors
- **Looping:** Schedule and orchestrate
- **DTM:** Manage mathematical proof templates

### Data Flow
```
Component → brain_save_system_report() → Template Merge → 
Global + Hourly → brain_update_aggregated_index() → 
Aggregated (6 levels) + Aggregated_Index (6 levels) → Done
```

### No Outstanding Issues
All gaps closed. All systems functional. Production-ready.
