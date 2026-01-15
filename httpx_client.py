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

payload_authentication = {
    "email" : payload_create_user_response["email"],
    "password": payload_create_user_response["password"],
}
authentication_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = payload_authentication)
authentication_response_data = authentication_response.json()

client =httpx.Client(
    base_url="http://localhost:8000",
    timeout= 100,
    headers= {"Authorization": f"Bearer {authentication_response_data['token']['accessToken']}"}

)
response = client.get("/api/v1/users/me")
print("Get user me data", response.json())

