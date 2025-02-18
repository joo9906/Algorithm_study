T = int(input())
stack = []
check = '+-*/'
last = []
def forth():
    arr = list(map(str, input().split()))

    for i in arr:
        if arr[i] not in check:
            arr[i] = int(arr[i])
    
    for i in range(len(arr)):
        if arr[i] == '.':
            stack.append('.')
            if len(arr) == 2:
                return arr[i-1]

        if arr[i] == '+' and arr[i-1] not in check :
            result = arr[i-2] + arr[i-1]
            stack.append(result)
            arr.pop(i-1)
            arr.pop(i-1)

        if arr[i] == '-' and arr[i-1] not in check:
            result = arr[i-2] - arr[i-1]
            stack.append(result)
            arr.pop(i-1)
            arr.pop(i-1)
            stack.append('-')
            

        if arr[i] == '*' and arr[i-1] not in check:
            result = arr[i-2] * arr[i-1]
            stack.append(result)
            arr.pop(i-1)
            arr.pop(i-1)
            stack.append('*')

        if arr[i] == '/' and arr[i-1] not in check :
            result = arr[i-2] / arr[i-1]
            stack.append(result)
            arr.pop(i-1)
            arr.pop(i-1)
            stack.append('/')

            