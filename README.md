# vaudit

`vaudit` is a CLI tool designed to manage configuration, governance, and audit for Fireblocks and cryptocurrency wallets using Infrastructure-as-Code principles.

## ✅ Key Features

- Manage Fireblocks settings declaratively with YAML
- Detect configuration differences with `plan`
- Apply changes with `apply`
- Perform audits with `audit`
- Validate and manage policies using `policy` subcommands

## 🛠 Usage

```bash
# Initialize a default config file
vaudit init

# Preview configuration changes
vaudit plan

# Apply configuration to Fireblocks
vaudit apply

# Audit current configuration and state
vaudit audit

# Apply governance policies
vaudit policy apply
```

## 🧩 Configuration (`vaudit.yml`)

All settings are written in YAML. Example:

```yaml
fireblocks:
  api_key: ${FIREBLOCKS_API_KEY}
  vault_id: "vault-prod-01"

targets:
  - name: operations_wallet
    vault_account_id: "123456789"
    governance_policy: "default-policy"
    required_signers: 2
```


## 🖋 Contributing

We use the [Developer Certificate of Origin (DCO)](./DCO).  
By contributing to this project, you agree to the terms of the DCO.

All commits must be signed off using `git commit -s`.

Example:

```
git commit -s -m "Add feature X"
```
