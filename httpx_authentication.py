import httpx



login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(login_response.status_code)
print(login_response.json())

login_response_data = login_response.json()
refresh_token = {
'refreshToken': login_response_data['token']['refreshToken'],
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_token)
print(refresh_response.status_code)
print(refresh_response.json())

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
