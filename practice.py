import requests

rul = 'https://fakestoreapi.com/carts'
data = requests.get(rul).json()
print(data)