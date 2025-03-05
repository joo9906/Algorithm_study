class Trie:
    head = {}
    
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
            if ch not in cur:
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
diction.remove('hi')
print(diction.head)
print(diction.search('hi'))
print(diction.search('hello'))
print(diction.search('hel'))

# 여기에 삭제를 하는 방법이 이게 맞나, head를 꺼내봤을 때 h - i - i:false인건데 이래도 되는건가?

'''
segment tree의 구조를 봤는데 분할정렬이랑 비슷하게 생겼는데 같은 개념으로 푸는건가
아니면 분할 정복이랑 더 비슷한거 같은데 분할 정복의 절반 정도를 가져다가 쓴건가?
이진검색 같기도 하고??
이걸 왜 쓰는지는 모르겠음. 그냥 리스트로 인덱스들을 더하는게 더 나은거 아닌가?
segment tree를 만든다고 미리 더해두나 필요할 때 더하나 거기서 거기 아닌가?
segment tree를 생성하고 부분합 구하는데 O(n+logn) 만큼 걸리는데 리스트는 만들고(O(n)) 찾는(O(n))에서 시간 복잡도 차이가 나는게 맞는지
구간 업데이트에서 왜 차이가 나는지 - 세그먼트의 업데이트는 알겠는데 리스트도 딱히 큰차이가 없는게 아닌가?
'''