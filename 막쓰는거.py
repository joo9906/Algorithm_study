a = list(map(int, input('두 수를 입력하세요. ').split()))
def num():
    print(f'첫 번째 함수 실행중 a = {a[0]}, b = {a[1]}')
    a.reverse()
    print(f'첫 번째 함수 실행중 a = {a[0]}, b = {a[1]}')

num()