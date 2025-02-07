T = int(input())


def blacklist():
    h, w = map(int,input().split())
    normal_list = []
    black_list = []
    cnt = 0
    
    for _ in range(h):
        input_list = list(map(int,input().split()))
        normal_list.extend(input_list)
    
    b_h, b_w = map(int, input().split())
    for _ in range(b_h):
        input_list = list(map(int, input().split()))
        black_list.extend(input_list)
    
    for i in black_list:
        if i in normal_list:
            cnt += 1
    return cnt, (h*w)-cnt

for k in range(1, T+1):
    b1, b2 = blacklist()
    print(f'#{k} {b1} {b2}')