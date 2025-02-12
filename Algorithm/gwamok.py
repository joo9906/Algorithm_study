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