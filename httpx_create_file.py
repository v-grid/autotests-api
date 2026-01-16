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

create_file_header = {
    "Authorization": f"Bearer {authentication_response_data['token']['accessToken']}"
}
create_file_data = {
"filename": "1string",
"directory": "1string",
"upload_file":"./testdata/files/1.png"
}
create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={
          "filename": create_file_data["filename"],
          "directory": create_file_data["directory"]

    },
    files={"upload_file": open(create_file_data["upload_file"], "rb")},
    headers=create_file_header
)
create_file_response_data = create_file_response.json()
print('Create file response:', create_file_response_data)
print(create_file_response.status_code)
