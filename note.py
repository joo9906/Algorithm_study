class tree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)
        self.build(1)

    def build(self, i=1):
        print(i)
        if i > self.n:
            return

        self.tree[i] = i
        self.build(i * 2)
        self.build(i * 2 + 1)

    def check(self):
        print(self.tree)

tree = tree(6)
tree.check()