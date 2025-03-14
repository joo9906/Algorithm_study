import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def solve(n, word):
    if word.count('A') < n:
        return 0

    idx = []
    result = 0

    for i in range(len(word)): # A의 위치 찾기
        if word[i] == 'A':
            idx.append(i)

    for i in range(len(idx) - n + 1):
        a = idx[i+n-1] - idx[i]
        result = max(result,a)

    return result

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    word = input()
    print(f'#{tc} {solve(n, word)}')