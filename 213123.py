import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
dummy_data=[]

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


def censorship(company, name, black_list):
    if company in black_list:
        print(f"{company} 소속의 {name}은/는 등록할 수 없습니다")
        return False

    print("이상 없습니다.")
    return True


def create_user(a):
    company_name = i['company']
    namme = i['name']    

    if censorship(company_name, namme, black_list):
        if company_name not in censored_user_list:
            censored_user_list[company_name] = []
        censored_user_list[company_name].append(name)

create_user(information)