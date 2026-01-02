# System Hierarchy & Lazy Update Structure

## Mode Roots
- **Test**: `Test/Test Mode/`
- **Demo**: `Test/Demo/`
- **Staging/Live**: `./` (Root)

## The Mining Tree (`Mining/`)
├── **Ledgers/**
│   ├── `global_ledger.json` (Live)
│   └── **Year/Month/Week/Day/Hourly/** (Lazy rollups)
├── **Math_Proofs/**
│   ├── `global_math_proof.json` (Live)
│   └── **Year/Month/Week/Day/Hourly/** (Lazy rollups)
├── **Submission_Logs/**
│   ├── `global_submission_log.json` (Live)
│   └── **Year/Month/Week/Day/Hourly/** (Lazy rollups)
└── **Temporary/**
    ├── **Template/**
    │   ├── `template_root.json` (The Node Template)
    │   ├── `submission_file.json` (The Final solution)
    │   └── **Process_00X/** (Permanent Miner Folders)
    │       ├── `working_template.json`
    │       └── `solution.json`
    └── **User_Look_at/** (Bad solutions / Failed consensus audits)

## The System Tree (`System/`)
├── **System_Reports/**
│   └── **Aggregated / Aggregated_Index** (Tiered: Year down to Hourly)
├── **Error_Reports/**
│   └── **Aggregated / Aggregated_Index** (Tiered: Year down to Hourly)
└── **Global_Aggregated/** (Tiered God-View Index)

## Update Strategy (Lazy Rollup)
1. **Live**: `Global` and `Hourly` updated instantly.
2. **EndOfHour**: Rollup `Hourly` -> `Day`.
3. **EndOfDay**: Rollup `Day` -> `Week`.
4. **EndOfWeek**: Rollup `Week` -> `Month`.
5. **EndOfMonth**: Rollup `Month` -> `Year`.
6. **Modes**: `--force-update`, `--auto-update-idle`, `--full-update-shutdown`.