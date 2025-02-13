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
    for _ in range(m):
        i, j = map(int, input().split())
        if result1 == [] :
            a = arr[0:i-1]
            a = a[::-1]
            b = arr[i:n]
        elif result1 != [] :
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

        result2.extend(list(reversed(a)))
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
    # result.extend(arrs[i-1]) 처음에 시도한 방법
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