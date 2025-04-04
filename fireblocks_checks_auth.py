#!/usr/bin/python3

from fireblocks_sdk import FireblocksSDK
from setting import apiKey


#Update the following parameters with your API key and secret
apiSecret = open('fireblocks_secret.key', 'r').read()

fireblocks = FireblocksSDK(apiSecret, apiKey)

try:
    accounts = fireblocks.get_vault_account(vault_account_id=1)
    print(accounts)
    print("✅ Fireblocks SDK 認証成功！Vault取得できました")
except Exception as e:
    print("❌ Fireblocks SDK 認証失敗！")
    print("Status:", e)

