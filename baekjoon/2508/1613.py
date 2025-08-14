import sys
input = sys.stdin.readline
sys.stdin = open("./input2508.txt", "r")

n, k = map(int, input().strip().split())
situation = {i: [] for i in range(1, n+1)}

def check(start, target):
    global situation
    
    check_list = situation[start]
    
    for i in check_list:
        pass
        
for _ in range(k):
    f, b = map(int, input().strip().split())
    situation[f].append(b)

check = []
s = int(input().strip())
for _ in range(s):
    f, b = map(int, input().strip().split())
    check.append((f, b))

print(situation, check)