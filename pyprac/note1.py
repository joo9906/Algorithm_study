import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

class Unionfind:
    def __init__(self, n, arr):
        self.n = n
        self.arr = [[] for _ in range(n+1)]
        self.island = [i for i in range(n+1)]
        self.parents = [i for i in range(n+1)]
        for a, b in arr:
            self.arr[a].append(b)
            self.arr[b].append(a)
            self.union(a, b)
        self.result()


    def find(self, x):
        if x == self.parents[x]:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx < rooty:
            self.parents[rooty] = rootx
        else:
            self.parents[rootx] = rooty # else 부분 까먹지 말기

    def result(self):
        for i in range(2, self.n+1):
            if self.find(1) != self.find(i): #여기에서 i의 대표자를 계속 찾았어야 함
                print(1, i)
                return


n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n-2)]
if n == 2:
    print(1, 2)
else:
    solve = Unionfind(n, arr)
