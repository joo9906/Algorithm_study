a = []
b = 0

for i in range(5):
    word = input().strip()
    a.append(word)

wor = input().strip()
senten = input().strip()



for i in a:
    if wor in i or senten in i:
        print(i)
        b+=1

if b==0:
    print('none')