n = int(input())
q = []
what = []

for _ in range(n):
    data = tuple(input().split())
    what.append(data)
print(what)
for i in what:
    if len(i) == 2:
        q.append(i[1])
    else:
        do = i[0]
        if do == "front":
            print(q[0])
        elif do == "back":
            print(q[-1])
        elif do == "size":
            print(len(q))
        elif do == "empty":
            if not q:
                print(1)
            else:
                print(0)
        elif do == "pop":
            if q:
                print(q.pop())
            else:
                print(-1)