import bisect

arr = [1, 2, 3, 5, 5, 8, 10]
a, b = 3, 8

left = bisect.bisect_left(arr, a)
print(left)
right = bisect.bisect_right(arr, b)
print(right)
print(right - left)