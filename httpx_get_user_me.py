import httpx

test_payload = {
    "email": "user@example.com",
    "password": "string"
}
response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=test_payload)
print(response_login.status_code)
print(response_login.json())
authentication_data = response_login.json()
accessToken_data = response_login.json()['token']['accessToken']

headers_Authorization = {
    "Authorization": f"Bearer {accessToken_data}"
}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_Authorization)
print(response.status_code)
print(response.json())