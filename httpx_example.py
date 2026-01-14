import httpx


response = httpx.get('http://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

data = {
    'title': 'новая задача',
    'completed': False,
    'userId': 1
}

response = httpx.post('http://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code)
#print(response.headers)
print(response.json())


data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
#print(response.headers)
print(response.json())

headers = {"Authorization": "Bearer test_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://httpbin.org/get", params=params)
response = httpx.get('http://jsonplaceholder.typicode.com/todos?userId=1')

print(response.status_code)
print(response.url)
#print(response.headers)
print(response.json())

files = {"file":("exemple.txt", open("exemple.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())

with httpx.Client() as client:
    response1 = client.get("http://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("http://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

client = httpx.Client(headers = {"Authorization": "Bearer test_token", "Content-Type": "application/json"})

response = client.get("http://httpbin.org/get")
print(response.status_code)
print(response.json())

try:
    response = httpx.get("http://jsonplaceholder.typicode.com/todos/eere")
    response.raise_for_status()
    print(f"Успешно! Статус: {response.status_code}")
    print(f"Данные: {response.json()}")
except httpx.HTTPStatusError as e:
    print(f"Ошибка HTTP: {e}")
