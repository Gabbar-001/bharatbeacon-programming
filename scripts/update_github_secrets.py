import json
import base64
import requests
from nacl import encoding, public

GITHUB_TOKEN = "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"
REPO = "Gabbar-001/bharatbeacon-news"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 1. Get Repo Public Key for Secrets
key_res = requests.get(f"https://api.github.com/repos/{REPO}/actions/secrets/public-key", headers=headers)
if key_res.status_code != 200:
    print(f"[X] Failed to get public key: {key_res.text}")
    exit(1)

key_data = key_res.json()
public_key_b64 = key_data["key"]
key_id = key_data["key_id"]

public_key = public.PublicKey(public_key_b64.encode("utf-8"), encoding.Base64Encoder)
sealed_box = public.SealedBox(public_key)

# 2. Encrypt and upload YOUTUBE_TOKEN_JSON
with open("token.json", "r", encoding="utf-8") as f:
    token_json_str = f.read()

encrypted_token = sealed_box.encrypt(token_json_str.encode("utf-8"))
b64_encrypted_token = base64.b64encode(encrypted_token).decode("utf-8")

secret_payload = {
    "encrypted_value": b64_encrypted_token,
    "key_id": key_id
}

put_res = requests.put(
    f"https://api.github.com/repos/{REPO}/actions/secrets/YOUTUBE_TOKEN_JSON",
    headers=headers,
    json=secret_payload
)

if put_res.status_code in (201, 204):
    print("[✓] Successfully updated YOUTUBE_TOKEN_JSON in GitHub Secrets!")
else:
    print(f"[X] Failed to update secret: {put_res.status_code} {put_res.text}")
