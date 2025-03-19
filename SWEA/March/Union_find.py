# 춘추전국시대

class Unionfind:
    def __init__(self, N, people):
        self.N = N
        self.rank = people # 인구수 비교해서 더 큰 쪽이 이기는 거임
        self.parents = list(range(N))

    def find(self, x):
        # 경로압축
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        ref_x = self.find(x)
        ref_y = self.find(y)

        if ref_x != ref_y:
            if self.rank[ref_x] < self.rank[ref_y]:
                self.parents[ref_x] = ref_y
                self.rank[ref_y] += self.rank[ref_x]

            else:
                self.parents[ref_y] = ref_x
                self.rank[ref_x] += self.rank[ref_y]

    def war(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                for i in range(self.N):
                    if self.parents[i] == ry:
                        self.rank[i] = 0

            elif self.rank[rx] < self.rank[ry]:
                for i in range(self.N):
                    if self.parents[i] == rx:
                        self.rank[i] = 0

            else:
                for i in range(self.N):
                    if self.parents[i] == rx or self.parents[i] == ry:
                        self.rank[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))
    T = int(input())
    now = [list(map(str, input().split())) for _ in range(T)]

    solve = Unionfind(N, people)

    for event, countryA, countryB in now:
        cA = ord(countryA) - ord('A')
        cB = ord(countryB) - ord('A')

        if event == 'alliance':
            solve.union(cA, cB)
        elif event == 'war':
            solve.war(cA, cB)
    print(solve.rank)
    live = sum([1 for i in solve.rank if i > 0])
    print(f'#{tc} {live}')


# 순환회로 검사

class Unionfind:
    def __init__(self, N, arr):
        self.n = N
        self.arr = arr
        self.parents = list(range(N))
        self.rank = [0] * N

    # def make_tree(self, N, arr):
    #     parents = [[] for i in range(N+1)]
    #     for i in range(N):
    #         for j in range(N):
    #             if arr[i][j] == 1:
    #                 parents[i].append(j)
    #
    #     return parents

    def find(self, x):
        # 경로압축
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        ref_x = self.find(x)
        ref_y = self.find(y)

        if ref_x == ref_y:
            return True  # 순환이 있음

        if self.rank[ref_x] < self.rank[ref_y]:  # x쪽의 랭크가 더 높으면 y를 x로 병합
            self.parents[ref_x] = ref_y

        elif self.rank[ref_x] > self.rank[ref_y]:  # y쪽의 랭크가 더 높으면 x를 y로 병합
            self.parents[ref_y] = ref_x

        else:  # 둘 다 랭크가 같으면 아무데나 병합
            self.parents[ref_y] = ref_x
            self.rank[ref_x] += 1

        return False

    def result(self):
        res = False
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.arr[i][j] == 1:
                    if self.union(i, j):
                        res = True
        return res


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve = Unionfind(n, arr)
    if solve.result():
        print(f'#{tc} WARNING')
    else:
        print(f'#{tc} STABLE')

# 유니온 파인드 연습

class Unionfind:
    def __init__(self, N, Q):
        self.n = N
        self.q = Q
        self.parents, self.rank = self.make_tree(N)

    def make_tree(self, N):
        parents = [i for i in range(N + 1)]
        rank = [0] * (N + 1)

        return parents, rank

    def find(self, x):
        if self.parents[x] == x:
            return x

        ref = self.find(self.parents[x])
        self.parents[x] = ref
        return ref

    def union(self, x, y):
        ref_x = self.find(x)
        ref_y = self.find(y)

        if ref_x == ref_y:
            return

        self.parents[ref_y] = ref_x
        return


T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    solve = Unionfind(N, Q)
    print(f'#{tc}', end=' ')
    for _ in range(Q):
        q, a, b = map(int, input().split())

        if q == 1:
            solve.union(a, b)

        elif q == 0:
            if solve.find(a) == solve.find(b):
                print('YES', end=' ')
            else:
                print('NO', end=' ')
    print()