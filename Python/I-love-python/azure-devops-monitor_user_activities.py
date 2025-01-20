
import requests
import json
import time
import base64
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import datetime
from datetime import timedelta

# Configuration
ORGANIZATION = "haaman"  # Replace with your Azure DevOps organization name
VAULT_URL = "https://haa.vault.azure.net/"  # Replace with your Azure Key Vault URL
SECRET_NAME = "pat"  # Replace with the name of the secret storing your PAT
LOG_FILE = "azure_devops_audit_log.txt"

# Azure DevOps REST API endpoint for audit logs
AUDIT_LOG_API_URL = f"https://auditservice.dev.azure.com/{ORGANIZATION}/_apis/audit/auditlog?api-version=7.1-preview.1"

def get_pat_from_key_vault():
    # Authenticate to Azure Key Vault
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=VAULT_URL, credential=credential)

    # Retrieve the PAT from Key Vault
    secret = client.get_secret(SECRET_NAME)
    return secret.value

def fetch_audit_logs(pat):
    pat_encoded = base64.b64encode(f":{pat}".encode()).decode()
    headers = {
        'Authorization': f'Basic {pat_encoded}',
    }
    try:
        # Add startTime for the last 10 minutes
        start_time = (datetime.datetime.utcnow() - timedelta(minutes=10)).isoformat() + "Z"
        audit_log_url = f"{AUDIT_LOG_API_URL}&startTime={start_time}"

        response = requests.get(audit_log_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch audit logs. Status code: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error fetching audit logs: {e}")
        return None

def log_user_activities(log_data):
    entries = log_data.get("decoratedAuditLogEntries", [])
    if not entries:
        print("No audit log entries found.")
        return

    with open(LOG_FILE, "a") as log_file:
        for entry in entries:
            timestamp = entry.get("timestamp", "N/A")
            actor = entry.get("actorDisplayName", "N/A")
            actorUPN = entry.get("actorUPN", "N/A")
            details = entry.get("details", "N/A")

            log_entry = (
                f"Timestamp: {timestamp}\n"
                f"Actor: {actor}\n"
                f"ActorUPN: {actorUPN}\n"
                f"Details: {details}\n"
                f"{'-' * 40}\n"
            )

            log_file.write(log_entry)
            print(log_entry)

def main():
    print("Starting Azure DevOps Audit Log Monitoring...")
    pat = get_pat_from_key_vault()
    while True:
        logs = fetch_audit_logs(pat)
        if logs:
            log_user_activities(logs)
        time.sleep(60)  # Poll every 5 minutes

if __name__ == "__main__":
    main()
