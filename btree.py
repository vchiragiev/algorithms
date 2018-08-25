from collections import deque
from typing import Deque


class Tree:
    # TODO: encapsulate properties ("private" or "readonly")
    def __init__(self, key, data=None, parent=None):
        self.parent: Tree = parent
        self.left: Tree = None
        self.right: Tree = None
        self.key: float = key
        self.orders: Deque[data] = deque()
        if data is not None:
            self.orders.append(data)

    def insert(self, key, data=None):
        if key < self.key:
            if self.left is None:
                self.left = Tree(key, data, self)
                return self.left
            else:
                return self.left.insert(key, data)
        elif key > self.key:
            if self.right is None:
                self.right = Tree(key, data, self)
                return self.right
            else:
                return self.right.insert(key, data)
        else:
            if data is not None:
                self.orders.append(data)
            return self

    def travers(self, function_ref):
        if self.left:
            self.left.travers(function_ref)
        function_ref(self)
        if self.right:
            self.right.travers(function_ref)

    def travers_reverse(self, function_ref):
        if self.right:
            self.right.travers_reverse(function_ref)
        function_ref(self)
        if self.left:
            self.left.travers_reverse(function_ref)

    def keys_to_list(self):
        result = list()
        self.travers(lambda x: result.append(x.key))
        return result

    def find_leftmost_node(self):
        if self.left is None:
            return self
        else:
            return self.left.find_leftmost_node()

    def find_rightmost_node(self):
        if self.right is None:
            return self
        else:
            return self.right.find_rightmost_node()

    def find(self, key):
        if key < self.key:
            if self.left is None:
                return None
            return self.left.find(key)
        elif key > self.key:
            if self.right is None:
                return None
            return self.right.find(key)
        else:
            return self

    def remove_me(self):
        # node has both left and right children
        # 1. find leftmost node of the right child (leftmost)
        # 2. set self.data = leftmost.data
        # 3. delete leftmost node
        if self.left is not None and self.right is not None:
            leftmost = self.right.find_leftmost_node()
            self.key = leftmost.key
            self.orders = leftmost.orders
            leftmost.remove_me()
            return self

        # node with left child only. link left child directly to self.parent
        elif self.left is not None:
            if self.parent is not None:
                self.left.parent = self.parent
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            return self.left

        # node with right child only. link right child directly to self.parent
        elif self.right is not None:
            if self.parent is not None:
                self.right.parent = self.parent
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            return self.right

        # node with no children. set self.parent.left/right to None
        if self.left is None and self.right is None:
            if self.parent is not None:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            return None
        
    def remove(self, key):
        match = self.find(key)
        if match is None:
            return None
        else:
            match.remove_me()
            return True

    def travers_breadth_first(self, function_ref):
        q1: deque[Tree] = deque()
        q2: deque[Tree] = deque()
        q1.append(self)
        while len(q1) > 0:
            function_ref(q1.copy())
            while len(q1) > 0:
                node = q1.popleft()
                if node.left is not None:
                    q2.append(node.left)
                if node.right is not None:
                    q2.append(node.right)
            tmp = q1
            q1 = q2
            q2 = tmp


if __name__ == "__main__":
    root = Tree(100)
    root.insert(80)
    root.insert(110)
    root.insert(90)
    root.insert(50)
    root.insert(140)
    root.insert(140)
    root.insert(200)

    print(root.keys_to_list())
    root.travers_breadth_first(lambda nodes: print(' '.join([str(x.key) for x in nodes])))

"""
    root.remove(90)
    print(root.keys_to_list())
    root.remove(110)
    print(root.keys_to_list())
    root = root.remove_me()
    print(root.keys_to_list())
    root = root.remove_me()
    print(root.keys_to_list())
    root = root.remove_me()
    print(root.keys_to_list())
    root = root.remove_me()
    print(root.keys_to_list())
"""