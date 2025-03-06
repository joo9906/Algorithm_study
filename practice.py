from math import ceil, log

def segment(left, right, i):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]

    mid = (right+left) // 2
    segment_tree[i] = segment(left, mid, i*2) + segment(mid+1, right, i*2+1)

    return segment_tree[i]

arr = [i for i in range(1, 11)]
segment_tree = [0] * (len(arr) * 4)
segment(0, len(arr)-1, 1)
print(segment_tree)