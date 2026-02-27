def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    b_idx = 0

    for a in A:
        if B[b_idx] > a:
            answer += 1
            b_idx += 1

    return answer