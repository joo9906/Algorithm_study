# 1244 스위치 켜고 끄기
def turn(arr, n): # 해당 스위치의 상태를 바꾸는 함수
    if arr[n] == 0:
        arr[n] = 1
    elif arr[n] == 1:
        arr[n] = 0

def boy(arr, num, n): # 남자일 때 적용
    for i in range(num-1, len(arr), num): # 받은 위치의 배수번째 위치의 스위치를 turn 함
        turn(arr, i)

def girl(arr, num, find): # 여자일 때 적용
    if num - find < 0 or num + find >= len(arr) or arr[num - find] != arr[num + find]:
        return turn(arr, num)
    elif arr[num-find] == arr[num+find]:
        turn(arr, num-find)
        turn(arr, num+find)
        girl(arr, num, find+1)

def off(): # input 값들을 받고 실행한 뒤 출력까지 하는 함수
    n = int(input())
    arr = list(map(int, input().split()))
    head = int(input())
    people = [list(map(int, input().split())) for _ in range(head)]

    for x, y in people: #남/여 받은대로 실행
        if x == 1:
            boy(arr, y, n)
        elif x == 2:
            girl(arr, y-1, 1)

    cnt = 0
    for i in arr:
        print(i, end=' ')
        cnt += 1
        if cnt == 20:
            print()
            cnt = 0

off()

# ----------------------------------------------------------------------------

# 7562 나이트의 이동 - BFS를 사용한 최적경로 탐색
from collections import deque

T = int(input())

def chess():
    I = int(input())
    arr = [[0] * I for _ in range(I)] # 체스판 생성
    start_x, start_y = map(int, input().split())  # 나이트가 시작하는 좌표
    target_x, target_y = map(int, input().split()) # 도달해야 할 좌표
    
    # 시작점과 목표점이 같으면 바로 중단
    if start_x == target_x and start_y == target_y: 
        return 0
    
    # 나이트가 이동할 수 있는 칸의 델타 - 순서대로 1시 2시 4시 5시 7시 8시 10시 11시 방향
    delta = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    
    q = deque([(start_x, start_y, 0)]) #현재 x좌표와 y좌표, 움직인 횟수 / 이후에는 움직인 좌표들이 들어갈거임
    
    # 타겟과 시작점이 같은 경우 꼬이면 안되니까 타겟을 시작점보다 나중에 지정해줘야 함
    arr[start_x][start_y] = 1 # 시작점의 좌표를 1로 바꾸고 시작(방문 했다는 표시)
    arr[target_x][target_y] = 2  # 나이트가 도착하려는 좌표를 2로 설정
    
    
    
    while q: # q에 저장하는 값이 있는동안 계속 반복(없으면 못 가는 것이므로 중단)

        now_x, now_y, cnt = q.popleft() # x, y 좌표들을 받고 cnt는 움직인 횟수 / 가장 왼쪽을 뽑아야 함

        for x, y in delta: # 델타를 순회하며 나이트가 움직일 수 있는 좌표를 탐색
            nx = now_x + x # 다음 x좌표
            ny = now_y + y # 다음 y좌표
            
            
            
            # 체스판을 벗어나지 않고 다음 좌표가 방문한 곳도 아니라면 실행
            if 0 <= nx < I and 0 <= ny < I and arr[nx][ny] != 1:
                if arr[nx][ny] == 2: # 다음 좌표가 목적지라면 cnt에 1 더하고 끝
                    return cnt + 1
            
                q.append([nx, ny, cnt + 1]) # 좌표 저장소에 다음 좌표를 저장
                arr[nx][ny] = 1 # 다음 좌표를 방문했다고 표시 함
    
    return 'Fail'
         
for k in range(T):
    print(chess())
    
# ------------------------------------------------------------------------
# 2178 미로 탐색 - 덱보다 그냥 리스트가 더 빠름. 왜지?????

def maze():
    ty, tx = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(ty)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)] #시계방향 델타
    arr[0][0] = 0 # 첫 좌표 방문처리
    
    q = [(0, 0, 1)] # 첫 좌표도 1회로 쳐서 시작
    
    while q: # q에 값이 있는동안 계속 반복
        nowy, nowx, cnt = q.pop(0) # q의 왼쪽 끝을 꺼내서 현재의 y, x좌표, 움직인 횟수를 뽑아옴

        if nowy == ty-1 and nowx == tx-1: # 현재의 y좌표, x좌표가 목표점과 같으면 cnt 뱉음
            return cnt
        
        for dy, dx in delta: # 델타를 돌면서 dy와 dx 값을 받음
            nx = nowx + dx # 다음 x좌표는 nowx + dx
            ny = nowy + dy # 다음 y 좌표는 nowy + dy

            # 미로 내에 있고 다음 좌표가 1일 때
            if 0 <= ny < ty and 0 <= nx < tx and arr[ny][nx] == 1:
                q.append((ny, nx, cnt + 1)) # 다음 y좌표, 다음 x좌표, 이동 횟수에는 1 추가
                
                # 여기서 먼저 0 처리를 해줘야 for문을 돌면서 불필요한 좌표를 변경하지 않음
                arr[ny][nx] = 0 
print(maze())

# ---------------------------------------------------------------------
# 14425 문자열 집합
import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.head = {}
    
    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['end'] = True
    
    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if 'end' in cur:
            return True
        else:
            return False

tree = Trie()
n, m = map(int, input().split())
cnt = 0

for _ in range(n):
    tree.add(input().strip())

for _ in range(m):
    if tree.search(input().strip()):
        cnt += 1

print(cnt)

# 17478 재귀 단순반복 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def func(n):
    global N

    if n == N:
        print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

    if n == 0:
        print('____' * (N-n) + '"재귀함수가 뭔가요?"')
        print('____' * (N-n) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * (N - n) + '라고 답변하였지.')
        return

    print('____' * (N-n) + '"재귀함수가 뭔가요?"')
    print('____' * (N-n) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('____' * (N-n) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('____' * (N-n) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.')
    func(n-1)
    print('____' * (N-n) + '라고 답변하였지.')

N = int(input())
func(N)

# 17478 재귀함수가 뭔가요ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def recursion(S, l, r, cnt):
    if l > r:
        if len(S) % 2 == 1:
            return print(1, cnt - 1)
        else:
            return print(1, cnt)
    elif S[l] != S[r]:
        return print(0, cnt)
    else:
        return recursion(S, l + 1, r - 1, cnt + 1)

def ispalindrome(S):
    return recursion(S, 0, len(S)-1, 1)

T = int(input())
for i in range(T):
    S = list(map(str, input().strip()))
    ispalindrome(S)

# 2491 수얼 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def bigfind(n, arr):
    result1 = 0
    result2 = 0

    for k in range(n):
        if n - k < result1:
            break
        i = k
        cnt = 1
        while i + 1 < n and arr[i] <= arr[i + 1]:  # 증가
            cnt += 1
            i += 1

        result1 = max(result1, cnt)

    for j in range(n):
        if n - j < result2:
            break
        num = j
        cnt = 1
        while num + 1 < n and arr[num] >= arr[num + 1]:  # 감소
            cnt += 1
            num += 1

        result2 = max(result2, cnt)

    return max(result1, result2)


n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(bigfind(n, arr))

# 1976 여행가자 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class Unionfind:
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.arr = [list(map(int, input().split())) for _ in range(self.n)] # 인접행렬임
        self.city = list(map(lambda x: int(x) - 1, input().split())) # 도시 어디로 갈지
        self.parents = [i for i in range(self.n)]
        self.union_cities()
        self.result = self.isconnect()

    def find(self, x):
        if self.parents[x] == x: # 본인과 대표자가 같으면 그대로 반환
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x] # 대표자 반환

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # 집합 대 집합에서 대표자의 숫자가 더 작은 쪽으로 대표자를 변경
        if rootX < rootY:
            self.parents[rootY] = rootX
        else:
            self.parents[rootX] = rootY

    def union_cities(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.arr[i][j] == 1:
                    self.union(i, j)

    def isconnect(self):
        front = self.find(self.city[0])

        for k in self.city[1:]:
            next = self.find(k)
            if front != next:
                return 'NO'
            front = next
        return 'YES'

solve = Unionfind()
print(solve.result)

# 1717 집합의 표현 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 이거 sys input 이랑 재귀 깊이 안풀어주면 재귀 오류 / 시간 초과 뜸, pypy는 메모리 터짐

import sys
#from collections import deque
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Unionfind:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.arr = [list(map(int, input().strip().split())) for _ in range(m)]
        self.parents = [i for i in range(n+1)]

    def find(self, x):
        if self.parents[x] == x: # 본인과 대표자가 같으면 그대로 반환
            return x

        self.parents[x] = self.find(self.parents[x]) # 본인의 대표자를 현재 그룹의 대표자로 변경

        return self.parents[x] # 대표자 반환

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # 집합 대 집합에서 대표자의 숫자가 더 작은 쪽으로 대표자를 변경
        if rootX < rootY:
            self.parents[rootY] = rootX
        else:
            self.parents[rootX] = rootY

    def result(self):
        res = []
        for state, a, b in self.arr:
            if state == 0:
                self.union(a, b)

            elif state == 1:
                i = self.find(a)
                j = self.find(b)
                if i == j:
                    res.append('YES')
                else:
                    res.append('NO')
        return res

n, m = map(int, input().strip().split())
ans = Unionfind(n, m)
k = ans.result()
for l in k:
    print(l)