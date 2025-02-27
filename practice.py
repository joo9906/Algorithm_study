T = int(input())

m, n, k = map(int, input().split())
route = {i:[] for i in range(n)}
for i in range(n):
    base, to, cost = map(int, input().split())
    route[base].append((to,cost))

result = []
cnt = 0 # 비용의 총 합이 될 변수
base = 0 #시작하는 노드

def dungeon(cnt):
    global k

    if cnt > k:
        return result.append(to)

    to, cost = route[base].pop(0)
    cnt += cost
    if cnt <= k:
        result.append(to)
        dungeon
    else:

    
    
dungeon()