import requests

response = requests.post(
    "http://localhost:5000/metrics/average-ticket",
    json={
        "services": [
            {"price": 120.0},
            {"price": 80.0},
            {"price": 100.0}
        ]
    }
)

print(response.json())