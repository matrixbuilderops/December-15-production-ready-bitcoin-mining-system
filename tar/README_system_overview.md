# System Overview (Concise)

## Core Flow
- Template source: Brain/Temporary Template or node template (test/staging/live).
- Mining: `ProductionBitcoinMiner` builds real Bitcoin headers and performs double SHA256; leading-zero/target checks gate success.
- Orchestration: `Singularity_Dave_Looping.py` coordinates template distribution, process folders, logging, and demo/test/live modes.
- DTM: `dynamic_template_manager.py` manages templates, IDs, and persistence; acts as GPS/consensus guide for miners.
- Brainstem: `Singularity_Dave_Brainstem_UNIVERSE_POWERED.py` provides canonical paths, reports, errors, and Brain.QTL integration.

## Math Layer
- Uses Knuth/Sorrellian-class modifiers (entropy, decryption, near-solution, math-problems, math-paradoxes) to bias nonce generation and scoring.
- Ultra Hex: bucketed leading-zero milestones (64 zeros per bucket, up to 256 buckets) alongside standard leading-zero counts.
- All modes rely on real SHA256 PoW; math overlays guide search without bypassing target checks.

## Artifacts & Logs
- Ledgers, math proofs, submission logs, aggregated outputs, and block_submission files are written per run.
- Process folders receive working templates and mining results for traceability.
- Brain/Miners reports and error logs are maintained via Brainstem helpers.

## Key Files (included in tar)
- `Singularity_Dave_Brain.QTL` (Brain definitions)
- `Singularity_Dave_Brainstem_UNIVERSE_POWERED.py` (Brainstem)
- `config.json` (runtime config)
- `Iteration 3.yaml` (math parameters)
- `dynamic_template_manager.py` (DTM)
- `Singularity_Dave_Looping.py` (orchestrator)
- `production_bitcoin_miner.py` (miner)
