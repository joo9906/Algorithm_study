import sys
input = sys.stdin.readline
# sys.stdin = open("../input.txt", "r")

n = int(input().strip())
q = []
check = set()

for _ in range(n):
    word = input().strip()
    if word not in check:
        q.append(word)
        check.add(word)

q.sort(key = lambda x: (len(x), x))

for j in q:
    print(j)