import math
import time

def inorder(n, last):
    global cnt
    if n <= last:
        inorder(n * 2, last)
        tree[n] = cnt
        cnt += 1
        inorder(n * 2 + 1, last)


for tc in range(int(input())):
    start = time.time()

    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    inorder(1, N)
    print(f'#{tc + 1} {tree[1]} {tree[int(N / 2)]}')
    end = time.time()
    print(f'{end-start:.5f} sec')
