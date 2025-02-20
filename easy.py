from collections import deque
import sys
sys.stdin = open('input.in', 'r')

T = int(input())

def find(start, under): 
    while inj[start]:
        node = inj[start].popleft()
        under.append(node)
        visited[node] = True
        find(node, under)
    return under

for nums in range(1, T+1):
    people = int(input())
    visited = [False] * (people)
    start = 0
    under = []
    boss = 0
    inj = [deque() for _ in range(people)]

    arr = [list(map(int, input().split())) for _ in range(people)] 
    
    for i in range(people): # 누가 누구랑 연결되어있는지 arr을 순회하며 찾음
        for j in range(people):
            if arr[i][j] == 1:
                inj[i].append(j)
                
    for k in range(len(inj)):
            if 0 in inj[k]:
                boss = k
                
    

    print(f'#{nums} boss:{boss} / under:', end = '')
    print(*find(start, under))