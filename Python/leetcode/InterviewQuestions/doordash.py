from collections import deque
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

class Solution:

    def __init__(self, tree1, tree2):
        self.root1 = tree1
        self.root2 = tree2

    def answer(self, node1, node2):
        if not node1 and not node2:
            return 0
        if node1 and node2:
            ans = 0
            if node1.key == node2.key:
                if node1.value == node2.value:
                    print(f"Both nodes exist and have same key values and they are {node1.key}, {node1.value} and {node2.key}, {node2.value}")
                    ans = 0
                else:
                    print(f"Both nodes exist but don't have same values, but have same keys {node1.key}, {node1.value} and {node2.key}, {node2.value}")
                    ans = 1
            else:
                print(f"Both nodes exist but don't have same keys OR values,{node1.key}, {node1.value} and {node2.key}, {node2.value}")
                ans = self.calculate(node1) + self.calculate(node2)
            for i in range(max(len(node1.children), len(node2.children))):
                child1 = node1.children[i] if i < len(node1.children) else None
                child2 = node2.children[i] if i < len(node2.children) else None
                ans += self.answer(child1, child2)
            return ans
        else:
            node = node1 if node1 else node2
            print(f"Only one node exists and it is ,{node.key}, {node.value}")
            return self.calculate(node) # nodes to be deleted
    
    def calculate(self, node):
        ans = 0

        q = deque([node])
        while q:
            curr = q.popleft()
            ans += 1
            for child in curr.children:
                q.append(child)
        return ans
    
# Create the nodes
a = TreeNode("a", 1)
b = TreeNode("b", 2)
c = TreeNode("c", 3)
d = TreeNode("d", 4)
e = TreeNode("e", 5)
f = TreeNode("f", 6)

# Build the tree structure
a.children.append(b)
a.children.append(c)
# b.children.append(d)
# b.children.append(e)
# c.children.append(f)

# Create the nodes
aa = TreeNode("a", 1)
bb = TreeNode("bb", 20)
cc = TreeNode("c", 3)
ff = TreeNode("f", 66)

# Build the tree structure
aa.children.append(bb)
aa.children.append(c)

sol = Solution(a, aa)
print(sol.answer(a, aa))

