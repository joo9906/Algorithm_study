import sys
sys.stdin = open("input.txt", 'r')

data = []
for _ in range(3):
    data.append(list(map(int, input().split())))

for i in data:
    if sum(i) == 0:
        print("D")
    elif sum(i) == 4:
        print("E")
    elif sum(i) == 1:
        print("C")
    elif sum(i) == 2:
        print("B")
    else:
        print("A")