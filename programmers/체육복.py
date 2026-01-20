def solution(n, lost, reserve):
    answer = 0
    full = lost + reserve
    full.sort()
    
    cnt = set()
    for i in range(1, n+1):
        if i not in full:
            cnt.add(i)
    
    for j in lost:
        for _ in range(2):
            try:
                target = reserve.pop(0)
                if target == j + 1 or target == j-1:
                    cnt.add(j)
                cnt.add(target)
            except:
                break
    print(cnt)
    return answer

solution(	3, [3], [1])