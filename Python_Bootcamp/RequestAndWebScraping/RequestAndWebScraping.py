import requests

url = 'https://www.python.org'
response = requests.get(url)

print(type(response))
print(response.status_code)
print(response.ok)

content = response.content
print(content.decode())

print(response.encoding)
print(response.headers)

