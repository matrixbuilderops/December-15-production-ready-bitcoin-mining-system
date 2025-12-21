import hashlib
import sys
from pathlib import Path

# Ensure repo root is importable
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from production_bitcoin_miner import ProductionBitcoinMiner


def test_double_sha256_matches_hashlib():
    expected = hashlib.sha256(hashlib.sha256(b"abc").digest()).hexdigest()
    got = ProductionBitcoinMiner._double_sha256(b"abc").hex()
    assert got == expected, f"double_sha256 mismatch: {got} != {expected}"


def test_leading_zero_counters(miner: ProductionBitcoinMiner):
    hash_hex = "0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    binary_zeros, hex_zeros = miner.get_dual_leading_zeros(hash_hex)
    # The miner's count_leading_zeros reports bit-level zeros for hex strings
    assert hex_zeros == 16, f"hex leading zeros expected 16, got {hex_zeros}"
    assert binary_zeros == 16, f"binary leading zeros expected 16, got {binary_zeros}"

    triple = miner.get_triple_leading_zeros(hash_hex)
    assert triple["standard_hex"] == 16, f"standard_hex expected 16, got {triple['standard_hex']}"
    assert triple["standard_binary"] == 16, f"standard_binary expected 16, got {triple['standard_binary']}"


def test_hash_function_matches_double_sha(miner: ProductionBitcoinMiner):
    header = b"sample header"
    expected = hashlib.sha256(hashlib.sha256(header).digest()).digest()
    got = miner.calculate_hash(header)
    assert got == expected, "calculate_hash should match double SHA256"


def run_all():
    # Keep demo/daemon small to avoid long-running loops; we test math helpers only.
    miner = ProductionBitcoinMiner(daemon_mode=True, demo_mode=True, max_attempts=1)

    test_double_sha256_matches_hashlib()
    test_leading_zero_counters(miner)
    test_hash_function_matches_double_sha(miner)

    # Ultra Hex sanity: Ultra 1 below 64 zeros, Ultra 2 at >=64
    uh1 = miner.get_ultra_hex_leading_zeros("00ff" + "f" * 62)
    assert uh1["ultra_hex_digit"] == 1, f"Ultra digit expected 1, got {uh1['ultra_hex_digit']}"
    uh2 = miner.get_ultra_hex_leading_zeros("0" * 64)
    assert uh2["ultra_hex_digit"] >= 2, f"Ultra digit expected >=2 at 64 zeros, got {uh2['ultra_hex_digit']}"

    print("✅ math_sanity_check: all tests passed")


if __name__ == "__main__":
    try:
        run_all()
    except AssertionError as exc:
        print(f"❌ math_sanity_check FAILED: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"❌ math_sanity_check ERROR: {exc}")
        sys.exit(2)
