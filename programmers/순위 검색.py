class TrieNode:
    def __init__(self):
        self.children = {}
        self.scores = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, info, score):
        node = self.root
        node.scores.append(score)
        for key in info:
            if key not in node.children:
                node.children[key] = TrieNode()
            node = node.children[key]
            node.scores.append(score)

    def sort_scores(self):
        def dfs(node):
            node.scores.sort()
            for child in node.children.values():
                dfs(child)
        dfs(self.root)

    def search(self, query_info, min_score):
        def dfs(node, depth):
            if not node:
                return 0
            if depth == len(query_info):
                # bisect 없이 직접 순회
                count = 0
                for s in node.scores:
                    if s >= min_score:
                        count += 1
                return count

            key = query_info[depth]
            if key == '-':
                total = 0
                for child in node.children.values():
                    total += dfs(child, depth + 1)
                return total
            else:
                return dfs(node.children.get(key), depth + 1)

        return dfs(self.root, 0)


def solution(info, query):
    trie = Trie()

    for record in info:
        data = record.split()
        props, score = data[:-1], int(data[-1])
        trie.insert(props, score)

    trie.sort_scores()

    answer = []
    for q in query:
        q = q.replace('and', '').split()
        query_info, min_score = q[:-1], int(q[-1])
        answer.append(trie.search(query_info, min_score))

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))