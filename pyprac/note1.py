def merge(left, right): # 병합 부분
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result

def merge_sort(arr): # 찢는 부분
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merged_list = merge(left_list, right_list)

    return merged_list


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)