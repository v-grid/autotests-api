import httpx
from tools.fakers import get_random_mail


payload = {
"email": get_random_mail(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

request_create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload)
print(f"mail: {get_random_mail()}")
print(request_create_user.status_code)
print(request_create_user.json())