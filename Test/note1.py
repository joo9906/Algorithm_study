def solution(info, n, m):
    answer = 10000000
    k = len(info)
    visited = [False] * k
    a_cnt = 0
    b_cnt = 0
    
    def search(a_cnt, b_cnt, l = 0):   
        nonlocal answer, n
        if l==k and a_cnt < n and b_cnt < m:
            answer = min(answer, a_cnt)
            
        for i in range(l, k):
            if a_cnt + info[i][0] <= n and visited[i] == False:
                visited[i] = True
                search(a_cnt+info[i][0], b_cnt, l + 1)
                search(a_cnt, b_cnt + info[i][1], l + 1)
                visited[i] = False
    
    search(a_cnt, b_cnt)
    if a_cnt == n or answer == 1000000:
        return -1
    else:
        return answer

info = [[1, 2], [2, 3], [2, 1]]
n, m = 4, 4
print(solution(info, n, m))  # Expected output: 2