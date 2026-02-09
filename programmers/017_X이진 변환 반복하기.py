def solution(s):
    answer = [0, 0]

    nxt_s = ""
    while s != "1":
        for i in s:
            if i == "0":
                answer[1] += 1
                continue
            else:
                nxt_s += "1"
        
        s_len = len(nxt_s)
        print(s_len)
        s = nxt_s
        
    return answer