import sys
# sys.stdin = open("input2508.txt", "r")
input = sys.stdin.readline

def binary_search(target, left, right):
    pass

N = int(input())
A_list = set(map(int, input().strip().split()))
M = int(input())
check_list = list(map(int, input().strip().split()))

for i in check_list:
    if i in A_list:
        print(1)
    else:
        print(0)