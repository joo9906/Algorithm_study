import sys
#input = sys.stdin.readline
sys.stdin = open("../input.txt", "r")

n = int(input())
cost = {i:{'R': 0, 'G': 0, 'B': 0} for i in range(3)}
for i in range(n):
    cost[i]['R'], cost[i]['G'], cost[i]['B'] = list(map(int, input().strip().split()))

q = [float('inf')] * (n + 101)


