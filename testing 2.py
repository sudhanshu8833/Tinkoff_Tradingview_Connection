

# Replace these with your OANDA API credentials
account_id = '101-003-21121032-001'
api_token = 'b4ba4a8e460a1265faaefc69ea4d4f94-8c0f1a647590f483f36ff495b9f6f5d6'

import requests

# Your OANDA API endpoint and account ID
api_endpoint = 'https://api-fxpractice.oanda.com/v3/accounts/{accountID}/instruments'  # Replace with your specific API endpoint
# Replace with your API token

# Set up headers with your API token
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Make a GET request to retrieve the list of instruments
response = requests.get(api_endpoint.format(accountID=account_id), headers=headers)
print(response.json())
# Check for a successful response
if response.status_code == 200:
    instruments = response.json()['instruments']
    for instrument in instruments:
        print(f"Symbol: {instrument['name']}, Type: {instrument['type']}")
else:
    print(f"Failed to retrieve instruments. Status code: {response.status_code}")
