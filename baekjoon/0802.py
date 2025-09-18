from itertools import combinations

n = [1, 2, 3]

for i in combinations(n, 2):
    print(i)
print(combinations(n, 2))