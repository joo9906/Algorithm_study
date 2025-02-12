T = int(input())

def stone():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for _ in range(m):
        i, j = map(int, input().split())
        a = arr[0:i-1]
        a = a.reverse()
        b = arr[i:n]
        for k in range(j-1):
            if a[k] == b[k] == 1:
                a[k] = b[k] = 0

            elif a[k] == b[k] == 0:
                a[k] = b[k] = 1

            else :
                a[k], b[k] = b[k], a[k]
    result.extend(a)
    result.extend(b)

    return result



for i in range(1, T+1):
    print(f'#{i} {stone()}')