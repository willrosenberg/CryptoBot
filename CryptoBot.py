import requests
import json

response = requests.get("https://api.coinbase.com/v2/exchange-rates")
#response.status_code
print(json.dumps(response.json(), sort_keys=True, indent=4))