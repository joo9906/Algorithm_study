import sys
from collections import deque
sys.stdin = open("input.txt", 'r')

def solve(nodes, root):
    answer = 1
    q = deque()
    
    for i in nodes[root]:
        q.append(i)
        
    while q:
        next = q.popleft()
        answer += 1
        
        if nodes[next]:
            for j in nodes[next]:
                q.append(j)
        else:
            continue
    
    return answer

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 이거 1001로 했다가 1001번째 노드가 있어서 터짐.
    nodes = {i:[] for i in range(1002)}
    input_nodes = list(map(int, input().split()))
    for k in range(0, len(input_nodes), 2):
        nodes[input_nodes[k]].append(input_nodes[k+1])
    
    print(f'#{tc} {solve(nodes, N)}')
