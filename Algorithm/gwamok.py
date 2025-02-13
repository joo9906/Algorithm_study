# 퍼펙트 셔플
T = int(input())

def shuffle():
    n = int(input())
    deck = list(map(str, input().split()))

    result = []

    if len(deck) % 2 == 0:
        for i in range(round(len(deck)//2)):
            result.append(deck[i])
            result.append(deck[i+n//2])

    if len(deck) % 2 == 1:
        for i in range(len(deck)//2):
            result.append(deck[i])
            result.append(deck[i + n // 2 + 1])
        result.append(deck[len(deck)//2])

    result = ' '.join(result)

    return result

for i in range(1,T+1):
    print(f'#{i} {shuffle()}')

# -------------------------------------------------------------
# 두 개의 숫자열
T = int(input())
 
def nums(n, m, A, B):
    max_val = 0
 
    if n<m:
        for i in range(m-n+1):
            sums = []
            for j in range(n):
                sums.append(A[j] * B[i+j])
            if max_val < sum(sums):
                max_val = sum(sums)
 
    if n>m:
        for i in range(n - m + 1):
            sums = []
            for j in range(m):
                sums.append(B[j] * A[i + j])
            if max_val < sum(sums):
                max_val = sum(sums)
 
    return max_val
 
 
for i in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{i} {nums(n, m, A, B)}')

# --------------------------------------------------------------------

# 돌 뒤집기 - 재귀 안쓴거
T = int(input())

def stone():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result1 = []

    for _ in range(m): # 기준 돌 왼쪽/오른쪽 리스트 생성
        i, j = map(int, input().split())
        if result1 == [] :
            a = arr[0:i-1]
            a = a[::-1]
            b = arr[i:n]

        elif result1 != [] : # 재귀를 안써서 들어온 코드드
            a = result1[0:i-1]
            a = a[::-1]
            b = result1[i:n]


        result2 = [] 
        comp = min(len(a), len(b))

        if comp >= j:
            for k in range(j):
                if a[k] == b[k] == 1:
                    a[k] = b[k] = 0

                elif a[k] == b[k] == 0:
                    a[k] = b[k] = 1

                else:
                    continue

        elif comp < j:
            for k in range(comp):
                if a[k] == b[k] == 1:
                    a[k] = b[k] = 0

                elif a[k] == b[k] == 0:
                    a[k] = b[k] = 1

                else:
                    continue

        result2.extend(list(reversed(a))) # 비교했던 리스트 합치기기
        if result1 != []:
            result2.append(result1[i - 1])
        else:
            result2.append(arr[i-1])
        result2.extend(b)


        result1 = result2



    return print(*result1)

for i in range(1, T+1):
    print(f'#{i}', end = ' ')
    stone()

# 재귀 쓴거
T = int(input())

def stone(n, m, arrs, cnt):
    if cnt == 0 :
        return print(*arrs)

    i, j = map(int, input().split())

    a = arrs[0:i-1]
    a = a[::-1]
    b = arrs[i:n]
    comp = min(len(a), len(b))

    if comp >= j:
        for k in range(j):
            if a[k] == b[k] == 1:
                a[k] = b[k] = 0

            elif a[k] == b[k] == 0:
                a[k] = b[k] = 1

            else:
                continue

    elif comp < j:
        for k in range(comp):
            if a[k] == b[k] == 1:
                a[k] = b[k] = 0

            elif a[k] == b[k] == 0:
                a[k] = b[k] = 1

            else:
                continue

    a = list(reversed(a))
    result = []
    result.extend(a)
    # result.extend(arrs[i-1]) 처음에 시도한 방법 - 인덱스 에러남남
    if 1 <= i <= n:
        result.extend(arrs[i - 1:i])
    result.extend(b)

    arrs = result

    cnt -= 1


    return stone(n, m, arrs, cnt)

for i in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{i}', end = ' ')
    stone(n, m, arr, m)

# -----------------------------------------------------------------------------------

# 풍선팡 - 델타 사용
T = int(input())
 
def balloon():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    delta = [[0,1], [1,0], [0,-1], [-1,0]] #델타 생성성
    compare = []
 
    for i in range(n):
        for j in range(n):
            score = 0
            score += arr[i][j]
            for x, y in delta: #델타 사용용
                nx = i + x
                ny = j + y
                while 0 <= nx < n and 0 <= ny < n: #이 조건은 그냥 외우시는게 좋아요
                    score += arr[nx][ny]
                    nx += x
                    ny += y
            compare.append(score)
                     
    result = max(compare) - min(compare)
 
    return result                
 
 
 
for i in range(1, T+1):
    print(f'#{i} {balloon()}')

# -------------------------------------------------------------------------------

# 스위치 조작

T = int(input())
 
def switch():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    cnt = 0
 
    for i in range(n):
        if arr[i] != brr[i]:
            cnt += 1
            for j in range(i, n):
                if arr[j] == 0:
                    arr[j] = 1
                elif arr[j] == 1:
                    arr[j] = 0
 
    return cnt
 
for k in range(1,T+1):
    print(f'#{k} {switch()}')

# -------------------------------------------------------------------------

# 어디에 단어가
T = int(input())
  
def puzzle(N, K, arr):
    correct = 0
      
    for row in arr: #가로 개수 구하기
        cnt = 0
        for a in row : # 가로 1줄 순회
            if a == 1: # 1이면 cnt에 1을 더하고 0이면 cnt가 K인지(1이 연속으로 K개 만큼 나오는지) 확인하고 맞으면 correct에 +1, 아니면 cnt 초기화
                cnt += 1
            else:
                if cnt == K:
                    correct += 1
                cnt = 0
        if cnt == K: #마지막에 나오는(row[-1]이 1인 경우에도 연속성을 판단하고 맞으면 correct에 1 추가)
            correct += 1
      
    for y in range(N): # 세로 개수 구하기
        column = []
        for x in range(N):
            column.append(arr[x][y]) #세로 한 줄을 column이란 함수에 넣어서 만듬
        cnt = 0
        for a in column : # 리스트로 한 줄을 만들었으니 다음부턴 위와 동일
            if a == 1:
                cnt += 1
            else:
                if cnt == K:
                    correct += 1
                cnt = 0
        if cnt == K:
            correct += 1
              
    return correct
  
for i in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
      
    print(f'#{i} {puzzle(N, K, arr)}')