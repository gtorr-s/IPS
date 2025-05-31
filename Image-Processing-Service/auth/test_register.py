import requests

# Registrar
response = requests.post(
    "http://127.0.0.1:8000/auth/register",
    data={"username": "torres", "password": "1234"}
)
print(response.json())

# Login
response = requests.post(
    "http://127.0.0.1:8000/auth/token",
    data={"username": "torres", "password": "1234"}
)
print(response.json())
