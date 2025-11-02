import httpx
from tools.fakers import *

payload_create_user_response = {
"email": get_random_mail(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"

}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=payload_create_user_response)
create_user_response_data = create_user_response.json()
print('Create user response:', create_user_response_data)

payload_authentication = {
    "email" : payload_create_user_response["email"],
    "password": payload_create_user_response["password"],
}
authentication_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = payload_authentication)
authentication_response_data = authentication_response.json()
print('Authentication response:', authentication_response_data)

headers_authentication = {
    "Authorization": f"Bearer {authentication_response_data['token']['accessToken']}"
}

response_delete = httpx.delete(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers = headers_authentication)
response_delete_data = response_delete.json()
print('Delete user response:', response_delete_data)
print(response_delete.status_code)