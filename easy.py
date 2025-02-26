from collections import deque

n = int(input())
student = [list(map(int, input().split())) for _ in range(n)]

def compare():
    cnt = 1
    result = []
    for i in range(n):
        weight, height = student[i]
        for j in range(n):
            x, y = student[j]
            if x > weight and y > height:
                cnt +=1
        result.append(cnt)
        cnt = 1
    return print(*result)

compare()