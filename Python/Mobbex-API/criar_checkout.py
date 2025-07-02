import requests
import json

url = "https://api.mobbex.com/p/checkout"

payload = json.dumps({
  "total": "100.53",
  "description": "Checkout de Prueba",
  "reference": "260520210954",
  "currency": "ARS",
  "test": True,
  "return_url": "https://mobbex.com/return_url",
  "webhook": "https://mobbex.com/webhook",
  "customer": {
    "email": "demo@mobbex.com",
    "name": "Cliente Demo",
    "identification": "12123123"
  }
})
headers = {
  'x-api-key': 'zJ8LFTBX6Ba8D611e9io13fDZAwj0QmKO1Hn1yIj',
  'x-access-token': 'd31f0721-2f85-44e7-bcc6-15e19d1a53cc',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)