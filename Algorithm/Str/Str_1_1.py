# GNS
T = int(input())

def sorting(test_case):
    test_case = test_case
    op = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    sortlist = []
    final = []
    for i in test_case:
        sortlist.append(op.index(i))
    sortlist.sort()

    for j in sortlist:
        final.append(op[j])

    return final

for u in range(1, T+1):
    nums = list(map(str, input().split()))
    N = int(nums[1])
    test_case = list(map(str, input().split()))
    print(f'#{u}')
    print(*sorting(test_case))
# ------------------------------------------------------------------
# 세로로 말해요
T = int(input())

def col_txt():
    txt_list = [list(map(str, input())) for _ in range(5)]
    test_case = []

    for i in range(15):
        for j in range(15):
            try:
                test_case.append(txt_list[j][i])
            except IndexError:
                continue
    result = ''.join(test_case)

    return result

for i in range(1, T+1):
    print(f'#{i} {col_txt()}')
# ----------------------------------------------------------------------
#  알파벳 개수
T = int(input())

for j in range(1, T+1):
    txt = input()
    dat = [0] * 26
    for i in txt:
        dat[ord(i) - 97] += 1
    result = ' '.join(map(str,dat))
    print(f'#{j}', end = ' ')
    print(*dat)
# -------------------------------------------------------------------
# 문자열의 거울상
T = int(input())

for i in range(1, T+1):
    txt1 = input()
    txt = txt1[::-1]
    result = []
    for j in range(len(txt)):
        if txt[j] == 'b':
            result.append('d')
        elif txt[j] == 'd':
            result.append('b')
        elif txt[j] == 'p':
            result.append('q')
        elif txt[j] == 'q':
            result.append('p')
    mirror = ''.join(result)

    print(f'#{i} {mirror}')
# -----------------------------------------------------------------
# 쇠막대기 자르기 - 레이저가 나올 때 len(cnt)만큼 더해주는게 중요!
# 막대기가 끝날 때 1씩 더해주는 것도 중요
T = int(input())
def razor():
    test = input()
    cnt = []
    result = 0

    for i in range(len(test)):
        if test[i] == '(' and test[i+1] != ')':
            cnt.append('(')
        elif test[i] == '(' and test[i+1] == ')':
            result += len(cnt)
        elif test[i] == ')' and test[i-1] != '(':
            try:
                cnt.pop()
            except IndexError:
                continue
            result += 1

    return result

for i in range(1, T+1):
    print(f'#{i} {razor()}')
