n, m = map(int, input().split())
arr = [0] * 1000001

for _ in range(n):
    x, y = map(int, input().split())
    arr[y-1] = x

def polar(arr, m):
    window = sum(arr[:m*2+1])
    max_ice = window

    for i in range(m*2+1, 1000001) : # 이 부분만 보고 배낌낌
        window = window - arr[i-(m*2+1)] + arr[i]
        if max_ice < window:
            max_ice = window

    return max_ice

print(polar(arr, m))

n, m = map(int, input().split())
arr = [0] * 1000001

for _ in range(n):
    x, y = map(int, input().split())
    arr[y-1] = x

def polar(arr, m):
    window = sum(arr[:m*2+1])
    max_ice = window

    for i in range(1, 1000001) :  # 이게 내가 처음에 한거거
        window = window - arr[i-1] + arr[i+m*2] 
        if max_ice < window:
            max_ice = window

    return max_ice

print(polar(arr, m))