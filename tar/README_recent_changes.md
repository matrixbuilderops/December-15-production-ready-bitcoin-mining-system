# Recent Changes Snapshot

Date: 2025-12-20

Key updates included in this archive:
- Demo mining now attempts real SHA256 via `ProductionBitcoinMiner` (10s cap), falling back to simulated only if no hash found, while still saving all demo artifacts.
- Submission/math proof flow enhanced: ledger, proof, aggregated, and block_submission files are persisted; submission snapshots added.
- Canonical template sourcing: demo/test/staging/live default to Brain/Temporary Template when none passed, and templates are distributed to process folders.
- Centralized template load guarded to set `centralized_template_file` when missing.
- Added math sanity checks for hashing and leading-zero counters (`Test/math_sanity_check.py`).
