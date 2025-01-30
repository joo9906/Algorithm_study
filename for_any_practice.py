a = int(input())
paper = [[0]*100 for i in range(100)]

for i in range(a):
    x, y = map(int, input().split())
    for b in range(y,y+10):
        for c in range(x,x+10):
            paper[b][c] = 1
            
num = 0
for j in range(100):
    num += paper[j].count(1)

print(num)