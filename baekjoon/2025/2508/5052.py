import sys
input = sys.stdin.readline
# sys.stdin = open("input2508.txt", "r")

class Trie:
    def __init__(self):
        self.head = {}
        self.ans = "YES"

    def insert(self, word):
        cur = self.head
        # word를 돌면서 딕셔너리를 계속 삽입함
        for w in word:
            # 만약 미리 입력해둔 전화번호가 있어서 자동으로 걸려버리게 되면 답을 NO로 바꿔버림
            # 입력해둔 번호가 없어서 새로 입력하면 계속 들어가며 Trie를 작성
            if w not in cur:
                cur[w] = {}

            if True in cur[w].values():
                self.ans = "NO"
                return
            cur = cur[w]
        # 끝 단어에 왔으면 True를 넣고 끝냄(딕셔너리도 들어가있고, True도 함께 들어가있음)

        if cur:
            self.ans = "NO"
            return

        cur['*'] = True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    sol = Trie()
    for _ in range(n):
        numbers = str(input().strip())
        sol.insert(numbers)
    print(sol.ans)


