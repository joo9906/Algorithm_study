'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
import sys

sys.stdin = open("input.in", "r")

def preorder(T):
    if T:
        print(T)
        preorder(left[T])
        preorder(right[T])

def inorder(T):
    if T:
        inorder(left[T])
        print(T)
        inorder(right[T])

def postorder(T):
    if T:
        postorder(left[T])
        postorder(right[T])
        print(T)

n = int(input())
e = n-1
arr = list(map(int, input().split()))

# 왼쪽 자식
left = [0] * (n+1) # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (n+1) # 부모를 인덱스로 오른쪽 자식 저장
prt = [0] * (n+1)

for i in range(e):
    p, c = arr[i*2], arr[i*2+1]
    prt[c] = p

for i in range(e):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0: #p의 자리가 비어있다면. 있으면 오른쪽 자식으로 저장
        left[p] = c
    else:
        right[p] = c

print('왼쪽', left)
print('오른쪽', right)
preorder(6)
inorder(1)