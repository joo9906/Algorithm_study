
def make_tree(start, end, i):
    if start == end:
        print(i)
        binary_tree[i] = arr[i]
        return

    mid = (start+end) // 2
    make_tree(start, mid, i*2)
    make_tree(mid+1, end, i*2+1)


T = int(input())

for k in range(1, T+1):
    n = int(input())
    arr = [i for i in range(1, n+1)]
    binary_tree = [0] * (len(arr) + 2)
    make_tree(0, len(arr)-1, 1)
    print(binary_tree)