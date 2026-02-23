n, m = map(int, input().split())

def count_k(n, k):
    result = 0
    temp = k

    while temp <= n:
        result += n // temp
        temp *= k

    return result

two = count_k(n, 2) - count_k(m, 2) - count_k(n-m, 2)
five = count_k(n, 5) - count_k(m, 5) - count_k(n-m, 5)

print(min(two, five))