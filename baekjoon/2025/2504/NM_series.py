import sys, heapq
input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

n, m = int(input().strip().split())
arr = list(map(int, input().strip().split()))
visit = [False] * n
ans = []

def recur(arr, li):
    global n, m

    if len(li) == m:
        heapq.heappush(ans, li)
        return

    for i in range(n):
        if not visit[i]:
            li.append(arr[i])
            visit[i] = True
        visit[i] = False

recur(arr, [])

for k in ans:
    print(k)


# 15657-8번
def recur(num):
    global n, m, arr
    
    if len(total) == m:
        print(*total)
        return
    
    for i in range(num, n):
        total.append(arr[i])
        recur(i)
        total.pop()

recur(0)
