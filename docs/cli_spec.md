# Vaudit CLI Specification

## 1. Overview

The Vaudit CLI provides a lightweight interface for inspecting Fireblocks wallet configurations and identifying potential governance or security risks. It is designed for security leads, auditors, and operators who need a quick and programmatic way to assess wallet setups without relying on a web dashboard.

> Note: This CLI is part of the POC version of Vaudit. Some features are experimental or limited in scope.

---

## 2. Setup

### Requirements
- Python 3.8+
- Access to Fireblocks REST API with appropriate read-only permissions

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/stirnetwork/vaudit.git
cd vaudit
pip install -r requirements.txt
```

### Fireblocks API Credentials

If an API user has not yet been created, you must generate a CSR (Certificate Signing Request) to request one:

```bash
vaudit generate-csr
```

This command will generate and store the following files:

- `~/.fireblocks/keys/fireblocks_${hash}.key` (private key)  
- `~/.fireblocks/keys/fireblocks_${hash}.csr` (certificate signing request)

> Note: Fireblocks does not currently offer an official CLI. As a temporary measure, Vaudit uses the following directory to store access configuration:

```
~/.fireblocks/config
```

Example:

> Profile switching is nice-to-have and not a mandatory feature in the current version.


```ini
[default]
timezone = "Asia/Tokyo"

[profile default]
fireblocks_access_key_id = your_access_key_id
fireblocks_secret_access_key_path = /path/to/secret.key
# or
fireblocks_secret_access_key = your_base64_encoded_secret
```

---

## 3. Usage

```bash
vaudit <command> [options]
```

Available commands:

- `generate-csr` — Generate a CSR and private key for Fireblocks API access  
- `dump` — Fetch and save Fireblocks workspace configuration data  
- `scan` — Evaluate configuration data against governance rules

You can also view this list using:

```bash
vaudit --help
```

---

## 4. Commands

---

### `generate-csr`

Generates a new private key and a certificate signing request (CSR) to be used when registering an API user with Fireblocks.

**Options:**
- `--output-dir` Directory to save the generated key and CSR (default: `~/.fireblocks/keys/`)  
- `--organization` Organization name to include in the CSR (required)  
- `--key-type` Key algorithm to use: `rsa4096`, `ed25519` (default: `rsa4096`)  
  > 🔍 `ed25519` support may vary depending on Fireblocks backend; please confirm compatibility.

**Example:**
```bash
vaudit generate-csr --organization "Stir Pte. Ltd." --key-type rsa4096
```

**Output:**
- CSR and private key files saved to the specified directory


---

### `dump`

Retrieves raw configuration data from Fireblocks and stores it locally for further analysis.

> ⚠️ Note: Fireblocks API responses may not contain all configuration details. Some governance data may be unavailable.

**Options:**
- `--output` Path to save the output file (default: `output/fireblocks_snapshot.json`)  
- `--output-format` Output format: `yaml` (default) or `json`

**Behavior:**
- Adds a timestamp to the snapshot metadata (e.g., `retrieved_at: 2025-04-05T12:34:56Z`) for traceability.

**Example:

> Profile switching is nice-to-have and not a mandatory feature in the current version.
**
```bash
vaudit dump --output ./output/fireblocks_snapshot.yaml --output-format yaml
```

**Output:**
- Output format and structure are TBD. Typically includes raw configuration data (vaults, users, policies, etc.)
- Includes `retrieved_at` field for timestamp

---

### `scan`

Evaluates Fireblocks configurations against predefined governance rules.

> ⚠️ Note: Fireblocks API responses may not contain all configuration details. Some governance data may be unavailable.

**Modes:**
- From saved file (offline analysis)  
- From live Fireblocks API (online analysis)

**Options:**
- `--input` Path to the file containing configuration data to be scanned (default: `output/fireblocks_snapshot.yaml`)  
- `--rules` Path to YAML file containing custom risk rules (default: `rules/default_risk_policy.yaml`)  
- `--output-format` Output format: `csv`, `pdf`, `yaml` (default: `csv`)  
- `--output` Path to save scan results (default: `output/fireblocks_scan.csv`)  
- `--live` Perform real-time scan using API (overrides `--input`)

**Example (offline scan):**
```bash
vaudit scan --input ./output/fireblocks_snapshot.yaml --rules ./rules/default_risk_policy.yaml --output-format pdf --output ./output/scan_result.pdf
```

**Example (live scan):**
```bash
vaudit scan --live --rules ./rules/default_risk_policy.yaml --output-format csv
```

**Output:**
- A formatted CSV or PDF file written to `output/fireblocks_scan.yml` (or custom path)

---

## 5. Rule Definition Format

> ⚠️ The rule format is not yet finalized and will be refined as development progresses.

Rules are defined in a YAML file and follow this basic structure:

```yaml
rules:
  - id: rule_001
    name: Require 2FA for all users
    type: user
    severity: high
    condition: "user.2fa_enabled == false"
    message: "User does not have 2FA enabled"
```

---

## 6. Limitations

- No real-time updates or event monitoring  
- CLI only (no web interface)  
- Rule engine supports simple logical conditions only  
- Configuration changes to Fireblocks are not performed (read-only)  
- API may not expose complete governance configurations

---

## 7. Future CLI Enhancements (Planned)

- Audit history with timestamped reports  
- Integration with alert systems (e.g., Slack, email)  
- Customizable rule packs  
- Role-based access control for CLI users
