import heapq
import sys
sys.stdin = open("input.txt", 'r')

class Recover:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def route(self, arr):
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[1e9] * self.n for _ in range(self.n)]
        visited[0][0] = arr[0][0]
        q = [(arr[0][0], 0, 0)]

        while q:
            wv, x, y = heapq.heappop(q)

            if wv > visited[x][y]: # 더 짧은 경로로 방문 시 넘어감
                continue

            if x == self.n-1 and y == self.n-1:
                return wv

            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    nwv = wv + arr[nx][ny]
                    if nwv < visited[nx][ny]:
                        visited[nx][ny] = nwv
                        heapq.heappush(q, (nwv, nx, ny))

    def result(self):
        return self.route(self.arr)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    solve = Recover(n, arr)
    print(f'#{tc} {solve.result()}')



 와 힙큐에 클래스에 이게  천재인가
