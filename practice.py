T = int(input())

def check():
    full, part = map(str, input().split())
    check = full.replace(part, '*', len(full))
    return len(check)

for i in range(1, T+1):
    print(f'#{i} {check()}')