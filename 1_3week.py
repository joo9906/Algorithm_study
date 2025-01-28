import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

censored_user_list = {}

def create_user(information):
    company_name = information['company']
    name = information['name']

    if censorship(company_name, name, black_list):
        if company_name not in censored_user_list:
            censored_user_list[company_name] = []
    
        censored_user_list[company_name].append(name)


def censorship(company_name, name, black_list):
    if company_name in black_list:
        print(f"{company_name} 소속의 {name}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다')
        return True

for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    name=parsed_data['name']
    lat=float(parsed_data['address']['geo']['lat'])
    lng=float(parsed_data['address']['geo']['lng'])
    company_name=parsed_data['company']['name']
    information={
        'company' : company_name,
        'lat' : lat,
        'lng' : lng,
        'name' : name
    }
    create_user(information)
    
print(censored_user_list)

