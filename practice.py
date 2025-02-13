T = int(input())

def stone():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for _ in range(m):
        i, j = map(int, input().split())
        if result == [] :
            a = arr[0:i-1]
            a = a[::-1]
            b = arr[i:n]
        elif result == True :
            a = result[0:i-1]
            a = a[::-1]
            b = result[i:n]

        try :
            for k in range(j-1):
                if a[k] == b[k] == 1:
                    a[k] = b[k] = 0

                elif a[k] == b[k] == 0:
                    a[k] = b[k] = 1

                else :
                    a[k], b[k] = b[k], a[k]
        except IndexError:
            break

        result.extend(list(reversed(a)))
        result.append(arr[i-1])
        result.extend(b)

    return result



for i in range(1, T+1):
    print(f'#{i} {stone()}')