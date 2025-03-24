# 미로
T = int(input())
 
def square(x, y, arr):
    if arr[x][y] == 3: # 종료조건
        return 1
 
    arr[x][y] = 1 # 재귀가 될 때마다 시작점의 좌표를 True로 설정해서 방문했다고 표시하는 부분
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 
    for i, j in delta:
        nx = x + i
        ny = y + j
        if 0 <= nx < n and 0 <= ny < n: #다음에 방문할 곳의 visited를 보고 방문 안한 지점만 가겠다
            if arr[nx][ny] != 1: # 만약 다음에 방문할 곳이 벽이 아니라면(벽이면 다음 델타)
                if square(nx, ny, arr) == 1: #탈출이 가능하다는 결과가 나왔다면 모든 재귀를 1로 끝냄
                    return 1
     
    return 0 # 끝까지 못찾으면 0
 
for p in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    x = y = 0 
    
    for i in range(n): # 시작점의 좌표 탐색
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j
                break
 
    result = square(x, y, arr)
    print(f'#{p} {result}')

#----------------------------------------------------------------------------------------------

# Forth

T = int(input())

def forth():
    n = list(map(str, input()))
    stack = []
    nin = '+-*/'

    for i in n:
        try:
            if i.isdigit():
                stack.append(int(i))
            
            elif i in nin:
                b = stack.pop()
                a = stack.pop()

            if i == '.':
                break
            elif i == '-':
                stack.append(a-b)
            elif i == '+':
                stack.append(a+b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a/b)
        except IndexError:
            return 'error'  
    
    result = stack[0]

    return result

for j in range(1, T+1):
    print(f'#{j} {forth()}')


# -----------------------------------------------------------------------------------
# 계산기 3
check = '+-*/'
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
def change(arr, length):
    stack = []  # 최종 후위 표기식
    pl = []  # 연산자 스택

    for k in range(length):
        if arr[k].isdigit():  # 숫자면 바로 출력
            stack.append(arr[k])

        elif arr[k] in check:  # 연산자인 경우
            while pl and pl[-1] in check and priority[pl[-1]] >= priority[arr[k]]:
                stack.append(pl.pop())  # 우선순위 높은 연산자 먼저 pop
            pl.append(arr[k])  # 현재 연산자 push

        elif arr[k] == '(':  # 여는 괄호는 스택에 push
            pl.append(arr[k])

        elif arr[k] == ')':  # 닫는 괄호가 나오면 '(' 만날 때까지 pop
            while pl and pl[-1] != '(':
                stack.append(pl.pop())
            pl.pop()  # '(' 제거

    while pl:  # 남아 있는 연산자 처리
        stack.append(pl.pop())

    return stack

def forth():
    length = int(input())
    arr = list(map(str, input()))
    back = change(arr, length)
    stack = []

    for i in back:
        if i in check:
            b = stack.pop()
            a = stack.pop()
            if i == '-':
                stack.append(a - b)

            elif i == '+':
                stack.append(a + b)

            elif i == '*':
                stack.append(a * b)

            elif i == '/':
                stack.append(a // b)
        else:
            stack.append(int(i))


    result = stack[0]

    return result


for j in range(1, 11):
    print(f'#{j} {forth()}')





            

    