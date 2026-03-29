import sys
#input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

n = int(input)
q = []
for _ in range(n):
    data = input().strip()
    