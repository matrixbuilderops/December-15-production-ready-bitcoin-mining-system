# FILE UNDERSTANDING DOCS

## Purpose

This folder contains comprehensive documentation for understanding the key files in the Bitcoin Mining System. These documents are specifically written for **other agents** who need to understand, modify, or work with the system files.

## Documentation Files

### 1. [Iteration_3_yaml.md](Iteration_3_yaml.md)
**File Documented**: `Iteration 3.yaml`
**Type**: YAML Configuration
**Lines**: 88
**Understanding**: Mathematical operations using Knuth-Sorrellian-Class system with 5 operational groups (families, lanes, strides, palette, sandbox). Contains parameters for computational compression and recursive expansion.

### 2. [Singularity_Dave_Brain_QTL.md](Singularity_Dave_Brain_QTL.md)
**File Documented**: `Singularity_Dave_Brain.QTL`
**Type**: QTL Blueprint
**Lines**: 3,434
**Understanding**: The **Brain** of the entire system - global orchestrator and single source of truth. Defines all flags, folder structures, component relationships, and system behavior. Everything starts here.

### 3. [Singularity_Dave_Brainstem_UNIVERSE_POWERED_py.md](Singularity_Dave_Brainstem_UNIVERSE_POWERED_py.md)
**File Documented**: `Singularity_Dave_Brainstem_UNIVERSE_POWERED.py`
**Type**: Python Module - Core Executor
**Lines**: 12,200
**Understanding**: The **Brainstem** - interprets Brain.QTL and executes commands. Manages all file operations, hierarchical paths, and component coordination. Exports critical functions used by all other components.

### 4. [Singularity_Dave_Looping_py.md](Singularity_Dave_Looping_py.md)
**File Documented**: `Singularity_Dave_Looping.py`
**Type**: Python Module - Mining Loop Manager
**Lines**: 16,302 (largest file)
**Understanding**: The **Looping Orchestrator** - manages when, how many, and how long to mine. Controls block/day timing, coordinates between miner and system, handles state management.

### 5. [config_json.md](config_json.md)
**File Documented**: `config.json`
**Type**: JSON Configuration
**Lines**: 40
**Understanding**: Bitcoin RPC connection settings, hardware configuration, ZMQ setup, and payout address. Contains credentials for Bitcoin Core connection. **MAINNET CONFIGURATION** (real Bitcoin).

### 6. [dynamic_template_manager_py.md](dynamic_template_manager_py.md)
**File Documented**: `dynamic_template_manager.py`
**Type**: Python Module - Template Coordinator
**Lines**: 6,886
**Understanding**: The **DTM** - handles template coordination and GPS-enhanced mining. Implements 4-layer defensive write system. Never fails, always logs. Manages consistent data structures across all components.

### 7. [production_bitcoin_miner_py.md](production_bitcoin_miner_py.md)
**File Documented**: `production_bitcoin_miner.py`
**Type**: Python Module - Bitcoin Mining Worker
**Lines**: 7,025
**Understanding**: The **Miner** - performs actual Bitcoin mining. Implements SHA-256 hashing, block template handling, nonce iteration, and mathematical enhancements using Knuth-Sorrellian-Class system. **Breaking Point Enhanced** for maximum performance.

## System Architecture Overview

```
Brain.QTL (3,434 lines)
   ↓ [Defines Everything]
   ↓
Brainstem (12,200 lines)  ←→  DTM (6,886 lines)
   ↓ [Executes]               [Coordinates Templates]
   ↓
Looping (16,302 lines)
   ↓ [Manages Loops]
   ↓
Miner (7,025 lines)
   ↓ [Performs Mining]
   ↓
Bitcoin Network
```

**Total System**: ~46,000 lines of code + configuration files

## File Relationships

### Configuration Files:
- **config.json** → Used by all components for Bitcoin RPC connection
- **Iteration 3.yaml** → Used by all components for mathematical parameters
- **Brain.QTL** → Defines behavior for all components

### Python Modules:
- **Brainstem** → Imported by DTM, Miner, Looping
- **DTM** → Used by Miner and Looping for templates
- **Miner** → Called by Looping
- **Looping** → Orchestrates everything

### Data Flow:
1. **Brain.QTL** defines what to do
2. **Brainstem** provides execution framework
3. **Looping** decides when to mine
4. **Miner** performs the mining
5. **DTM** coordinates templates throughout
6. **Config.json** provides connection details
7. **Iteration 3.yaml** provides math parameters

## Key Concepts

### 1. **Knuth-Sorrellian-Class Mathematical System**
Custom mathematical framework for computational compression and recursive expansion:
- **Class 1**: Foundation iteration (A^B)^C
- **Class 2**: 3-rotational recursion
- **Class 3**: Meta-rotational expansion
- **Class 4**: Mirrored duality (recursive-entropic folding)
- **Class 5**: Complete synthesis of all classes

**111-digit Universe BitLoad Constant**:
```
208500855993373022767225770164375163068756085544106017996338881654
571185256056754443039992227128051932599645909
```

### 2. **Hierarchical File Organization**
All files organized by time:
```
Mining/
├── Ledgers/YYYY/MM/DD/HH/
├── Submissions/YYYY/MM/DD/HH/
├── Math_Proofs/YYYY/MM/DD/HH/
└── System/
    ├── System_Reports/[Component]/Hourly/YYYY/MM/DD/HH/
    ├── System_Logs/[Component]/Hourly/YYYY/MM/DD/HH/
    └── Error_Reports/[Component]/Hourly/YYYY/MM/DD/HH/
```

### 3. **Defensive Architecture**
**Never fail, always log** philosophy:
- Multi-layer fallback systems
- Template-based error recovery
- Graceful degradation
- Continue on error

### 4. **Mode System**
- **Production** (default): Real Bitcoin mining
- **Demo**: Simulated mining
- **Test**: Limited validation runs
- **Staging**: Final testing
- **Smoke Test**: Component validation
- **Smoke Network**: Full system validation

### 5. **Flag System**
All flags defined in Brain.QTL:
- Mode flags: `--demo`, `--test`, `--staging`, `--smoke-test`, `--smoke-network`
- Mining control: `--block N`, `--block-random`, `--block-all`, `--day N`, `--day-all`
- Hardware: Auto-detection and resource limits

## For Agents: Quick Start Guide

### Understanding the System?
**Start with**: Brain.QTL documentation (defines everything)

### Working with Files?
**Start with**: Brainstem documentation (handles all file operations)

### Modifying Mining Logic?
**Start with**: Miner documentation (actual mining) and Looping documentation (orchestration)

### Debugging Issues?
**Check**: Error reports in `Mining/System/Error_Reports/[Component]/Hourly/YYYY/MM/DD/HH/`

### Adding Features?
1. Check **Brain.QTL** for system architecture
2. Use **Brainstem** functions for file operations
3. Follow **DTM** defensive patterns for safety
4. Test with `--smoke-test` before production

### Configuration Changes?
**Edit**: `config.json` for Bitcoin settings, `Iteration 3.yaml` for math parameters

## File Size Reference

| File | Lines | Purpose |
|------|-------|---------|
| Singularity_Dave_Looping.py | 16,302 | Loop management (largest) |
| Singularity_Dave_Brainstem_UNIVERSE_POWERED.py | 12,200 | Core executor |
| production_bitcoin_miner.py | 7,025 | Mining worker |
| dynamic_template_manager.py | 6,886 | Template coordinator |
| Singularity_Dave_Brain.QTL | 3,434 | System orchestrator |
| Iteration 3.yaml | 88 | Math parameters |
| config.json | 40 | Bitcoin connection |
| **TOTAL** | **~46,000** | **Full system** |

## Important Warnings

### Security:
- **config.json** contains RPC credentials - protect this file
- Use `chmod 600 config.json` to restrict access
- Don't share credentials publicly

### Network:
- **Port 8332** = Bitcoin MAINNET (real money)
- **Port 18332** = Testnet (test coins)
- Current config is MAINNET - mines real Bitcoin

### Mining Reality:
- Solo mining probability is extremely low without ASIC hardware
- System is mathematically correct but not competitive with ASICs
- Consider testnet mining or pool mining for realistic results

### File Operations:
- All writes use defensive patterns (never fail)
- Hierarchical paths automatically created
- Emergency logs always succeed
- Never stop mining due to logging failures

## Mathematical Foundation

The system integrates advanced mathematics:
- **Knuth-Sorrellian-Class**: Classes 1-5 operations
- **Universe BitLoad**: 111-digit base constant
- **Recursive-Entropic**: Dual computational paths
- **Folding Operations**: Compression-expansion dynamics
- **Math Proofs**: Generated for each found block

See `/math` folder for detailed mathematical formalization.

## Template System

All data follows templates from `System_File_Examples/`:
- `global_mining_ledger.json`
- `global_mining_submission.json`
- `global_mining_error.json`
- `global_system_report.json`
- `math_proof_template.json`

**Always use templates** for consistent data structures.

## Common Operations

### Check Mining Status:
```bash
ls -lh Mining/Ledgers/$(date +%Y/%m/%d/%H)/
```

### View Recent Errors:
```bash
cat Mining/System/Error_Reports/Miners/Global/global_miners_error.json
```

### Check System Reports:
```bash
ls -lh Mining/System/System_Reports/*/Hourly/$(date +%Y/%m/%d/%H)/
```

### Verify Math Proofs:
```bash
ls -lh Mining/Math_Proofs/$(date +%Y/%m/%d/%H)/
```

## Getting Help

1. **Read the documentation** for the specific file you're working with
2. **Check Brain.QTL** for system-wide behavior
3. **Review error reports** in hierarchical structure
4. **Use smoke tests** to validate changes
5. **Follow defensive patterns** from DTM

## Contributing

When modifying files:
1. **Maintain defensive architecture** - never fail, always log
2. **Follow hierarchical structure** - use Brain's folder system
3. **Use templates** - load from System_File_Examples
4. **Report to Brain** - use Brainstem functions
5. **Test with smoke tests** - validate before production
6. **Update documentation** - keep these docs current

## Version Information

- **Brain.QTL Version**: 3.2
- **Created**: 2025-09-05
- **Last Updated**: 2025-10-14
- **Status**: Canonical (authoritative source)
- **Math System**: Knuth-Sorrellin Classes 1-5
- **Breaking Point**: Applied 2025-09-24

## Support

For issues or questions:
1. Check error reports in Mining/System/Error_Reports/
2. Review system reports in Mining/System/System_Reports/
3. Validate configuration with smoke tests
4. Consult individual file documentation

---

**Last Updated**: 2025-12-21  
**Documentation Version**: 1.0  
**For**: Other agents working with the Bitcoin Mining System
