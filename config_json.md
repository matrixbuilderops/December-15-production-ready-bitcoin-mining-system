# config.json - Understanding Document

## File Type
JSON Configuration File

## Purpose
Contains connection and configuration parameters for the Bitcoin node, RPC interface, and mining system settings.

## File Size
40 lines

## Structure Overview

The configuration is organized into 6 main sections:

### 1. **Legacy RPC Credentials** (Lines 2-7)
```json
"rpcuser": "SignalCoreBitcoin",
"rpcpassword": "B1tc0n4L1dz",
"rpc_host": "127.0.0.1",
"rpc_port": 8332,
"wallet_name": "SignalCoreBitcoinWallet",
"payout_address": "bc1qrqk4qwwy37xtpcvxs7ayeufld07tja652ka2wv"
```

**Legacy Format**: Top-level RPC settings for backward compatibility.

**Key Fields**:
- `rpcuser`: Username for Bitcoin RPC authentication
- `rpcpassword`: Password for Bitcoin RPC authentication
- `rpc_host`: Bitcoin node address (localhost)
- `rpc_port`: Bitcoin RPC port (8332 is Bitcoin mainnet default)
- `wallet_name`: Bitcoin Core wallet to use
- `payout_address`: Bitcoin address where mining rewards are sent

**Payout Address**: `bc1qrqk4qwwy37xtpcvxs7ayeufld07tja652ka2wv`
- This is a **Bech32 address** (starts with `bc1`)
- Native SegWit format (lowest transaction fees)
- Mainnet address (production Bitcoin network)

### 2. **Bitcoin RPC Configuration** (Lines 8-15)
```json
"bitcoin_rpc": {
  "host": "127.0.0.1",
  "port": 8332,
  "username": "SignalCoreBitcoin",
  "password": "B1tc0n4L1dz",
  "wallet_name": "SignalCoreBitcoinWallet",
  "timeout": 30
}
```

**Modern Format**: Structured RPC settings under dedicated object.

**Key Fields**:
- `host`: Bitcoin node IP address (localhost = same machine)
- `port`: 8332 is standard Bitcoin Core RPC port
- `username`/`password`: Same as legacy format
- `wallet_name`: Same as legacy format
- `timeout`: 30 seconds for RPC requests

**Network**: Port 8332 indicates **Bitcoin mainnet** (testnet uses 18332)

### 3. **Bitcoin Node Configuration** (Lines 16-19)
```json
"bitcoin_node": {
  "auto_configure": false,
  "conf_file_path": "bitcoin.conf"
}
```

**Purpose**: Control whether the system should automatically configure the Bitcoin node.

**Key Fields**:
- `auto_configure`: `false` = Do NOT auto-configure Bitcoin node (manual setup required)
- `conf_file_path`: Location of bitcoin.conf file (relative path)

**Important**: With `auto_configure: false`, the user must manually set up their Bitcoin node before mining.

### 4. **Pool Configuration** (Lines 20-26)
```json
"pool_config": {
  "enabled": false,
  "pool_url": "",
  "pool_username": "",
  "pool_password": "",
  "solo_mining": true
}
```

**Purpose**: Configure pool vs solo mining.

**Current Setting**: **Solo Mining Mode**
- `enabled`: `false` = Pool mining is disabled
- `solo_mining`: `true` = Mining solo (not in a pool)
- Pool credentials empty (not used)

**Solo Mining**: This system mines independently, keeping 100% of block rewards (if successful).

### 5. **ZMQ Configuration** (Lines 27-34)
```json
"zmq": {
  "enabled": true,
  "host": "127.0.0.1",
  "rawblock_port": 28333,
  "hashblock_port": 28335,
  "rawblock_endpoint": "tcp://127.0.0.1:28333",
  "hashblock_endpoint": "tcp://127.0.0.1:28335"
}
```

**Purpose**: ZeroMQ (ZMQ) integration for real-time Bitcoin network notifications.

**Key Fields**:
- `enabled`: `true` = ZMQ notifications are active
- `host`: localhost (same machine as Bitcoin node)
- `rawblock_port`: 28333 (receives complete block data)
- `hashblock_port`: 28335 (receives block hash notifications)
- `*_endpoint`: Full TCP endpoint URLs

**ZMQ Benefits**:
- Real-time notification when new blocks arrive
- Faster response to network changes
- Reduced polling overhead

**Configuration Note**: Bitcoin Core must be started with ZMQ enabled:
```
bitcoind -zmqpubrawblock=tcp://127.0.0.1:28333 -zmqpubhashblock=tcp://127.0.0.1:28335
```

### 6. **Hardware Configuration** (Lines 35-40)
```json
"hardware": {
  "auto_detect": true,
  "miner_processes": "auto",
  "cpu_cores_reserved": 2,
  "max_memory_gb": 60
}
```

**Purpose**: Control hardware resource usage for mining.

**Key Fields**:
- `auto_detect`: `true` = Automatically detect available hardware
- `miner_processes`: `"auto"` = Automatically determine optimal number of mining processes
- `cpu_cores_reserved`: 2 cores reserved for system operations (not used for mining)
- `max_memory_gb`: 60 GB maximum memory for mining operations

**Resource Management**:
- System reserves 2 CPU cores for OS and Bitcoin node
- Remaining cores used for mining
- Memory limit prevents system slowdown
- Auto-detection optimizes for current hardware

## Network Type

**This configuration is for Bitcoin MAINNET** (production network):
- RPC port 8332 (mainnet standard)
- Payout address starts with `bc1` (mainnet Bech32)
- Real bitcoin rewards (not testnet coins)

**To use testnet**, you would need:
- `rpc_port`: 18332
- Payout address starting with `tb1`
- Bitcoin Core started with `-testnet` flag

## Security Considerations

**Credentials Exposed**:
```json
"rpcuser": "SignalCoreBitcoin"
"rpcpassword": "B1tc0n4L1dz"
```

**⚠️ SECURITY NOTE**: These credentials are visible in the config file.
- Anyone with access to this file can control the Bitcoin node
- RPC access allows wallet operations and transaction signing
- In production, this file should have restricted permissions (chmod 600)
- Consider using more secure authentication methods

**Best Practices**:
1. Use strong, unique RPC passwords
2. Restrict file permissions: `chmod 600 config.json`
3. Don't share this file in public repositories
4. Use Bitcoin Core's cookie authentication if possible
5. Run Bitcoin node on isolated network segment

## Integration with Other Components

### Used by:
1. **production_bitcoin_miner.py** - Reads Bitcoin RPC settings
2. **Singularity_Dave_Looping.py** - Uses for loop coordination
3. **dynamic_template_manager.py** - May use for template coordination
4. **Singularity_Dave_Brainstem_UNIVERSE_POWERED.py** - Loads config via ConfigNormalizer

### Config Loading Pattern:
```python
# Common pattern in components
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    rpc_user = config['bitcoin_rpc']['username']
    # ... use config
except Exception as e:
    # Fallback or error handling
```

### With ConfigNormalizer:
```python
from config_normalizer import ConfigNormalizer
normalizer = ConfigNormalizer('config.json')
config = normalizer.get_normalized_config()
```

## Configuration Requirements

For the system to work, you must have:

1. **Bitcoin Core installed** and running
2. **Bitcoin Core configured** with:
   - RPC enabled (`rpcuser`, `rpcpassword` in bitcoin.conf)
   - ZMQ enabled (if using ZMQ features)
   - Wallet loaded (`SignalCoreBitcoinWallet`)
3. **Wallet created** with name matching `wallet_name`
4. **Payout address** must be in the wallet
5. **Sufficient disk space** for Bitcoin blockchain (~500+ GB)
6. **Network connectivity** to Bitcoin P2P network

## Example Bitcoin Core Configuration

Corresponding `bitcoin.conf` file should include:
```
# RPC Settings
server=1
rpcuser=SignalCoreBitcoin
rpcpassword=B1tc0n4L1dz
rpcallowip=127.0.0.1
rpcport=8332

# ZMQ Settings
zmqpubrawblock=tcp://127.0.0.1:28333
zmqpubhashblock=tcp://127.0.0.1:28335

# Mining Settings
gen=0
# (mining is done by external software, not Bitcoin Core)

# Network
listen=1
port=8333

# Wallet
wallet=SignalCoreBitcoinWallet
```

## Mode-Specific Behavior

The config is used differently in different modes:

- **Production Mode**: Uses config as-is for real Bitcoin mining
- **Demo Mode**: May override with simulated values
- **Test Mode**: May use testnet or regtest settings
- **Staging Mode**: Uses real config but limited operations

Mode is controlled by flags from Brain.QTL, not this config file.

## Timeout Settings

**RPC Timeout**: 30 seconds
- Mining operations can be slow
- Network requests may take time
- 30 seconds allows for network latency
- If mining takes longer, consider increasing

**No Block Template Timeout**: Not specified
- System must handle case where template expires
- Bitcoin Core invalidates old templates when new block arrives
- Miner must request fresh template after each network block

## Hardware Auto-Detection

With `auto_detect: true`, the system:
1. Detects available CPU cores
2. Reserves `cpu_cores_reserved` cores (2)
3. Allocates remaining cores to mining
4. Sets process count automatically
5. Monitors memory usage
6. Stays under `max_memory_gb` limit (60 GB)

**Example**:
- System with 8 cores
- Reserves 2 cores
- Uses 6 cores for mining
- May create 6 miner processes (one per core)

## For Other Agents: Quick Reference

**Need Bitcoin connection?** → Use `bitcoin_rpc` section

**Need payout address?** → Use `payout_address` field

**Need to check solo vs pool?** → Check `pool_config.solo_mining`

**Need hardware limits?** → Check `hardware` section

**Need ZMQ endpoints?** → Use `zmq.*_endpoint` fields

**Need to modify config?** → Edit this file, restart mining system

**Connection failing?** → Verify:
1. Bitcoin Core is running
2. RPC credentials match bitcoin.conf
3. Ports are not blocked by firewall
4. Wallet is loaded in Bitcoin Core
5. ZMQ is enabled if `zmq.enabled: true`

**Security issue?** → Change RPC password, restart Bitcoin Core

**Wrong network?** → Check port (8332=mainnet, 18332=testnet)

## Important Notes

1. **Mainnet**: This configuration is for REAL Bitcoin (mainnet)
2. **Solo Mining**: System mines independently, not in a pool
3. **Local Node**: Bitcoin Core must run on same machine (127.0.0.1)
4. **ZMQ Enabled**: Real-time block notifications active
5. **Auto Hardware**: System automatically optimizes for current hardware
6. **Manual Node Setup**: Bitcoin node must be configured manually (`auto_configure: false`)
7. **Security Sensitive**: Contains RPC credentials - protect this file

## Testing Configuration

Before mining:
1. Test RPC connection: `bitcoin-cli -rpcuser=SignalCoreBitcoin -rpcpassword=B1tc0n4L1dz getblockchaininfo`
2. Verify wallet: `bitcoin-cli -rpcwallet=SignalCoreBitcoinWallet getwalletinfo`
3. Check payout address: `bitcoin-cli getaddressinfo bc1qrqk4qwwy37xtpcvxs7ayeufld07tja652ka2wv`
4. Test ZMQ: Use ZMQ test subscriber to verify block notifications
5. Verify resources: Check available CPU cores and memory
