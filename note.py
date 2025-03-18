class Node:
    def __init__(self, n, arr):
        self.node = n
        self.arr = arr

class Put:
    def printing(self, num):
        print(num)



num = 3
arr = [1, 2, 3]
a = Node(num, arr)

print(a.node)
print(a.arr)

solve = Put()
solve.printing(a.node)