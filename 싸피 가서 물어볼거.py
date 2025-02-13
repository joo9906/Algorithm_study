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
    # result.extend(arrs[i-1]) 처음에 시도한 방법법
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


