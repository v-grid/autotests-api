import httpx

"""
#response_bearer = httpx.get("https://httpbin.org/bearer")
#response_get = httpx.get("https://httpbin.org/get")
data_1 = {
    "username" : "admin1",
    "password" : "admin1",
    "rol_admin" : True
}
response_post_data = httpx.post("https://httpbin.org/post", data=data_1)
#print(response_post_data.json())
#print(response_post_data.status_code)


data={
    "email": "user@example10cd.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

headers = {
    "Authorization": "Bearer my_secret",
   

}
response_locall_post = httpx.post("http://localhost:8000/api/v1/users", json=data, headers=headers)

#print(response_get.status_code)
#print(response_get.json())
#print(response_get.text)
#print(response_bearer.status_code)
#print(response_bearer.json())



print(response_locall_post.json())
print(response_locall_post.status_code)
print(response_locall_post.headers)
data_authentication = {
  "email": "user@example10cd.com",
  "password": "string"
}
response_authentication = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data_authentication)
#print(response_authentication.status_code)
#print(response_authentication.json())
data_refresh = {
  "refreshToken": response_authentication.json()['token']['refreshToken']
}
#print(data_refresh)
response_refresh = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=data_refresh)
print(response_refresh.json())
print(response_refresh.status_code)

"""

date_authentication = {
"email": "user@example10cd.com",
"password": "string"
}
response_authentication = httpx.post("http://localhost:8000/api/v1/authentication/login", json=date_authentication)
#print(response_authentication.json())
access_token = response_authentication.json()['token']['accessToken']
data_headers = {
    "Authorization": "Bearer " + access_token,
    "accept": "application/json"
}
response_users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=data_headers)
print(response_users_me.json())
print(response_users_me.status_code)