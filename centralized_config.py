import json
import os
from pathlib import Path

def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        # Fallback to looking in parent directory if not found (e.g. running from subdir)
        config_path = Path(__file__).parent.parent / "config.json"

    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)
    return {}

def get_bitload():
    """Get bitload constant from config"""
    config = load_config()
    bitload = config.get("mathematical_framework", {}).get("bitload_constant")
    if bitload:
        return int(bitload)
    # Fallback default if not in config
    return 208500855993373022767225770164375163068756085544106017996338881654571185256056754443039992227128051932599645909

def get_rpc_credentials():
    """Get RPC credentials from config"""
    config = load_config()

    # Try structured bitcoin_rpc first
    if "bitcoin_rpc" in config:
        rpc = config["bitcoin_rpc"]
        return {
            "host": rpc.get("host", "127.0.0.1"),
            "port": rpc.get("port", 8332),
            "username": rpc.get("username", ""),
            "password": rpc.get("password", ""),
            "wallet_name": rpc.get("wallet_name", "")
        }

    # Fallback to flat structure
    return {
        "host": config.get("rpc_host", "127.0.0.1"),
        "port": config.get("rpc_port", 8332),
        "username": config.get("rpcuser", ""),
        "password": config.get("rpcpassword", ""),
        "wallet_name": config.get("wallet_name", "")
    }
