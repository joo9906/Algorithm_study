# 회문 2 - 나중에 다른 방법 시도해보기
for t in range(10):
    N = int(input())
    arr = [input() for _ in range(100)]
 
    max_val = 0
 
    # 가로에서 가장 긴 회문 찾기
    for c in range(100):
        for i in range(100):
            for j in range(100 - i):
                test = arr[c][j:j + i + 1]
                if test == test[::-1]:
                    if len(test) > max_val:
                        max_val = len(test)
 
    # 세로에서 가장 긴 회문 찾기
    # 세로 회문을 찾기 위해 새로운 배열을 만들어 값들을 뒤집음
    transposed_arr = [''.join([arr[x][i] for x in range(100)]) for i in range(100)]
 
    for c in range(100):
        for i in range(100):
            for j in range(100 - i):
                test = transposed_arr[c][j:j + i + 1]
                if test == test[::-1]:
                    if len(test) > max_val:
                        max_val = len(test)
 
    print(f'#{t + 1} {max_val}')

# -------------------------------------------------------------------------------------------------------
#초심자의 회문 검사
T = int(input())
 
def check():
    arr = list(map(str, input()))
    if arr == arr[::-1]:
        return 1
    else:
        return 0
 
for i in range(1, T+1):
    print(f'#{i} {check()}')

# --------------------------------------------------------------------------------------------------------
# 가장 빠른 문자열
T = int(input())

def check():
    full, part = map(str, input().split())
    check = full.replace(part, '*', len(full))
    return len(check)

for i in range(1, T+1):
    print(f'#{i} {check()}')