# 민우의 폭탄 돌리기 - while 버전
import sys
input = sys.stdin.read

T = int(input())

def bomb():
    n, m = map(int, input().split())
    k = int(input())
    arr = [list(input()) for _ in range(n)]
    delta = [[0,1], [1, 0], [0, -1], [-1, 0]]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                for x, y in delta:
                    nx = i + x
                    ny = j + y
                    long = 0
                    
                    while long < k:
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]== '_':                       
                            arr[nx][ny] = '%'
                            nx += x
                            ny += y
                            long += 1
                        else:
                            break
                arr[i][j] = '%'

    for k in range(n):
        print(''.join(arr[k]))

for p in range(1, T+1):
    print(f'#{p}')
    bomb()


# ----------------------- 4중 for문 버전-------------------------------------

T = int(input())

def bomb():
    n, m = map(int, input().split())
    k = int(input())
    arr = [list(input()) for _ in range(n)]
    delta = [[0,1], [1, 0], [0, -1], [-1, 0]]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                for x, y in delta:
                    nx = i + x
                    ny = j + y
                    for _ in range(k):
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]== '_':                       
                            arr[nx][ny] = '%'
                            nx += x
                            ny += y
                        else:
                            break
                arr[i][j] = '%'

    for k in range(n):
        print(''.join(arr[k]))

for p in range(1, T+1):
    print(f'#{p}')
    bomb()

# ----------------------------------------------------------------------------------
# 채점방식
T = int(input())

def test(student, test_num, correct, compare):
    best = 0
    worst = float('inf')
    for i in range(student):
        seq = 0
        score = 0
        for j in range(test_num):
            if correct[j] == compare[i][j]:
                seq += 1
                score += seq
            else:
                seq = 0

        if score > best:
            best = score
        if score < worst:
            worst = score

    return best-worst

for tc in range(1, T+1):
    student, test_num = map(int, input().split())
    correct = list(map(int, input().split()))
    compare = [list(map(int, input().split())) for _ in range(student)]
    print(f'#{tc} {test(student, test_num, correct, compare)}')

# -----------------------------------------------------------------------------------
# 바이러스 죽이기
T = int(input())

def charb():
    n, p = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    best = []

    for i in range(n):
        for j in range(n):
            score = 0
            score += arr[i][j]
            for x, y in delta:
                nx = x + i
                ny = y + j
                for k in range(p):
                    if 0 <= nx < n and 0 <= ny < n:
                        score += arr[nx][ny]
                        nx += x
                        ny += y
            best.append(score)
    return max(best)

for k in range(1,T+1):
    print(f'#{k} {charb()}')

# ----------------------------------------------------------------------------------------
# 스마트폰
from collections import deque
T = int(input())

def captcha():
    test_case = [[0] * 1001 for _ in range(1001)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(a[0], a[2]+1):
        for j in range(a[1], a[3]+1):
            test_case[i][j] += 1

    for i in range(b[0], b[2]+1):
        for j in range(b[1], b[3]+1):
            test_case[i][j] += 1

    result = 0
    gyup = []

    for i in range(1000):
        for j in range(1000):
            if test_case[i][j] == 2:
                result += 1
                gyup.append([i,j])

    if result == 0:
        return 4

    if result == 1:
        return 3

    xs = [x for x, y in gyup]
    ys = [y for x, y in gyup]

    if len(set(xs)) == 1 or len(set(ys)) == 1:
        return 2

    return 1

for i in range(1, T+1):
    print(f'#{i} {captcha()}')
    
# ----------------------------------------------------------
# 전등 스위치
T = int(input())

def on(arr, n):
    for i in range(n):
        arr[i+1]= 1
    
    return arr

def switch():
    n = int(input())
    arr = [0] * (n+2)
    target = [0]
    target.extend(list(map(int, input().split())))
    cnt = 0
    
    for j in range(1, n+1):
        if arr[j] != target[j] and target[j] == 1:
            for k in range(j,n+1,j):
                if arr[k] == 0:
                    arr[k] = 1
                    
                elif arr[k] == 1:
                    arr[k] = 0
            cnt += 1
            
        elif arr[j] != target[j] and target[j]==0:
            for k in range(j,n+1,j):
                if arr[k] == 0:
                    arr[k] = 1
                    
                elif arr[k] == 1:
                    arr[k] = 0
                    
            cnt += 1
    
    return cnt     

for q in range(1, T+1):
    print(f'#{q} {switch()}')