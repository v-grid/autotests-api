import httpx
from tools.fakers import *

payload_create_user = {
    "email": get_random_mail(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response_create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload_create_user)
response_create_user_data = response_create_user.json()
print(response_create_user.status_code)
print(response_create_user_data)

payload_authentication_user = {
  "email": payload_create_user["email"],
  "password": payload_create_user["password"]
}

response_authentication_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_authentication_user)
response_authentication_user_data = response_authentication_user.json()
print(response_authentication_user.status_code)
print(response_authentication_user_data)

headers_update_user = {
    "Authorization": f"Bearer {response_authentication_user_data['token']['accessToken']}"
}
payload_update_user = {

  "email": get_random_mail(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"

}
response_update_user = httpx.patch(f"http://localhost:8000/api/v1/users/{response_create_user_data['user']['id']}", json=payload_update_user, headers = headers_update_user)
response_update_user_data = response_update_user.json()
print(response_update_user.status_code)
print(response_update_user_data)

