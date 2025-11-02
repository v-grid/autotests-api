import httpx

date_authentication = {
    "email": "user@example10cd.com",
    "password": "string"
}
response_authentication = httpx.post("http://localhost:8000/api/v1/authentication/login", json=date_authentication)
# print(response_authentication.json())
access_token = response_authentication.json()['token']['accessToken']
data_headers = {
    "Authorization": "Bearer " + access_token,
    "accept": "application/json"
}
response_users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=data_headers)
print(response_users_me.json())
print(response_users_me.status_code)