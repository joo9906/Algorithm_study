class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]

        cur[ch] = True # 다 끝나고 마지막 ch를 True라고 설정

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur[ch]:
                return False
            cur = cur[ch]

        if cur[ch] == True: # 마지막 ch에서 True라면 단어가 있음
            return True
        else:
            return False # 마지막 ch의 값이 True가 아니라면 해당 단어는 없는거임(더 길거나 짧음)

    def remove(self, word):
        cur = self.head

        for ch in word:
            cur = cur[ch]
        cur[ch] = False

diction = Trie()

diction.add("hi")
diction.add('hello')
print(diction.search('hi'))
print(diction.search('helldklf'))