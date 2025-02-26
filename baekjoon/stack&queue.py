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