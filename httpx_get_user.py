import httpx
from tools.fakers import *

user_create_payload = {
"email": get_random_mail(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

user_create_response = httpx.post("http://localhost:8000/api/v1/users", json=user_create_payload)
user_create_response_data = user_create_response.json()

print('Create user data:', user_create_response_data)
#print(user_create_response.status_code)

authentication_payload = {
    "email": user_create_payload['email'],
  "password": user_create_payload['password']
}

authentication_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=authentication_payload)
authentication_response_data = authentication_response.json()
print('Login data:', authentication_response_data)
#print(authentication_response.status_code)

get_user_headers = {
    "Authorization": f"Bearer {authentication_response_data['token']['accessToken']}"
}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{user_create_response_data['user']['id']}", headers=get_user_headers)
get_user_response_data = get_user_response.json()
print("Get user data:", get_user_response_data)


# payload_create = {
#   "email": get_random_mail(),
#   "password": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }
#
# response_create =  httpx.post("http://localhost:8000/api/v1/users", json=payload_create)
# user_id = response_create.json()["user"]["id"]
# user_email = response_create.json()["user"]["email"]
# user_password = payload_create["password"]
#
# payload_authentication = {
#     "email": user_email,
#     "password": user_password
# }
#
# response_authentication = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_authentication)
# accessToken_data = response_authentication.json()["token"]["accessToken"]
# accessToken_type = response_authentication.json()["token"]["tokenType"]
#
# headers = {
#     "Authorization": f"{accessToken_type} {accessToken_data}",
# }
#
# response_get_user_id = httpx.get(f"http://localhost:8000/api/v1/users/{user_id}", headers=headers)
# print(response_get_user_id.json())
