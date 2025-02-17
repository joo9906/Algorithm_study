

def sugar():
    n = int(input())
    sugar_bag = [5, 3]
    cnt = 0

    for i in sugar_bag:
        if n >= i:
            cnt += n//i
            n = n % i



    if n != 0:
        return print(-1)
    else:
        return print(cnt)

sugar()