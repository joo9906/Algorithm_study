from collections import deque

n = int(input())
stack = deque()
garbage = []
for i in range(1, n+1):
    stack.append(i)
while len(stack) > 1:
    a = stack.popleft()
    garbage.append(a)
    b = stack.popleft()
    stack.append(b)

print(*stack)

# --------------------------------------------------------
# 1158 요세푸스
n,k = map(int,input().split())


# ----------------------------------------------------------
# 9935 문자폭탄
def strings():
    arr = input().rstrip()
    bomb = input().rstrip()
    result = []
    bl = len(bomb)
    
    for i in arr:
        result.append(i)
        if len(result) >= bl and result[-bl:] == list(bomb):
            del result[-bl:]
    
    if not result:
        return 'FRULA'
    else:
        return ''.join(result)
        
print(strings())

# -----------------------------------------------------------------
# 17413 단어 뒤집기 2
def word():
    words = input().strip()
    result = []
    save = deque()
    check = 0
    

    for i in words:
        if i == ' ':
            result.extend(save)
            result.append(' ')
            save = deque()
            continue
            
        if i == '<':
            check = 1
            if save:
                result.extend(save)
                save = deque()
        
        if i == '>':
            result.append(i)
            check = 0
            continue
        
        if check == 1:
            result.append(i)
        elif check == 0:
            save.appendleft(i)
            
    if save:
        result.extend(save)
    
    return print(''.join(result))

word()
# ----------------------------------------------------------------------
# 1021 회전하는 큐
def func():
    n, m = map(int, input().split())
    target = deque(map(int, input().split()))
    arr = deque([i for i in range(1, n+1)])
    cnt = 0

    while target:
        a = arr.popleft()
        b = target.popleft()
        middle = int(len(arr)/2)

        if b in list(arr)[:middle]:
            while a != b:
                arr.append(a)
                a = arr.popleft()
                cnt += 1
        else:
            while a != b:
                arr.appendleft(a)
                a = arr.pop()
                cnt += 1

    return print(cnt)

func()

# 외계인의 손가락

import sys
input = sys.stdin.readline

def solve(arr):
    plat = [[] for _ in range(7)]
    cnt = 0

    for line_num, plat_num in arr:
        while plat[line_num] and plat[line_num][-1] > plat_num:
            plat[line_num].pop()
            cnt += 1

        if plat[line_num] and plat[line_num][-1] == plat_num:
            continue

        plat[line_num].append(plat_num)
        cnt += 1

    return cnt

n, p = map(int, input().split())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
print(solve(arr))