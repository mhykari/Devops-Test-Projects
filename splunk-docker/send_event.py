import requests
import json
import time

# Splunk HEC details
splunk_hec_url = "http://localhost:8088/services/collector"  # Update host if necessary
splunk_token = "your_hec_token"  # Replace with the actual HEC token

# Headers for the request
headers = {
    "Authorization": f"Splunk {splunk_token}",
    "Content-Type": "application/json"
}

# Event data to send
data = {
    "event": "This is a test event from a service",
    "sourcetype": "_json",
    "host": "test-host",
    "index": "main"
}

# Send the event to Splunk
try:
    response = requests.post(splunk_hec_url, headers=headers, data=json.dumps(data), verify=False)
    if response.status_code == 200:
        print("Data successfully sent to Splunk!")
    else:
        print(f"Failed to send data: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error sending data to Splunk: {e}")
