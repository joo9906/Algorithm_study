# 1991 트리 순회
class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def preorder(node):
    print(node.root, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.root, end = '')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.root, end='')

n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]
tree = {}
for a, b, c in arr:
    tree[a] = Node(a, b, c)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

# 9934 완전 이진 트리

k = int(input())
arr = list(map(int, input().split()))
result = [[] for _ in range(k)]

def inorder(start, end, level = 0):
    if level >= k:
        return

    mid = (start + end) // 2

    result[level].append(arr[mid])
    inorder(start, mid, level+1)
    inorder(mid+1, end, level+1)

inorder(0, len(arr))

for i in result:
    print(*i)

# 1068 트리

import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)

