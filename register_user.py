import requests

url = "http://127.0.0.1:5000/auth/register"

data = {
    "username": "venky",
    "password": "12345"
}

res = requests.post(url, json=data)

print("STATUS:", res.status_code)
print("RESPONSE:", res.text)