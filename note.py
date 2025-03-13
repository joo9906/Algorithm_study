from collections import deque
data = deque([[1, 1, 7, 1], [2, 1, 3, 2], [1, 1, 5, 2]])

# x와 y가 같은 데이터를 찾고, 그 데이터의 2번 자리 값을 더함
def check(state):
    dict = {}
    result = deque([])
    for _ in range(len(state)):
        x, y, head, direction = state.popleft()
        key = (x, y)

        if key in dict:
            if dict[key][0] < head:
                dict[key][1] = direction
            dict[key][0] += head
        else:
            dict[key] = [head, direction]

    for i in dict:
        x, y = i
        v= dict[i][0]
        d = dict[i][1]
        print(dict[i], v, d)

    return print(dict)


check(data)