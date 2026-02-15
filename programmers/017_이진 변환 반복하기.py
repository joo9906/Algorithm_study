def solution(s):
    answer = [0, 0]
    target = s
    print(target)
    while target != "1":
    # for _ in range(1):
        nxt = ""
        for i in target:
            if i == "0":
                answer[1] += 1
            else:
                nxt += i

        answer[0] += 1

        target = str(bin(len(nxt)))[2:]
    print(answer)
    return answer

solution("01110")