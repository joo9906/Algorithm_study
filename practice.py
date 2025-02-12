T = int(input())

def shuffle():
    n = int(input())
    stage = [list(map(int, input().split())) for _ in range(n)]
    
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    for x in range(n):
        for y in range(n):
            for i, j in delta:
                

    return result

for i in range(1,T+1):
    print(f'#{i} {shuffle()}')