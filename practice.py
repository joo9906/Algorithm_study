di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n = 2
m = 3

for i in range(n):
    for j in range(m):
        for dir in range(4):
            ni = i +di[dir]
            nj = j +dj[dir]
            if 0<= ni < n and 0<=nj<=m:
                print(ni, nj)
