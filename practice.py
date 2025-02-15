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