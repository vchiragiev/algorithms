from collections import deque
from typing import Deque


class Tree:
    # TODO: encapsulate properties ("private" or "readonly")
    def __init__(self, key):
        self.left: Tree = None
        self.right: Tree = None
        self.key = key

    # insert
    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Tree(key)
                return self.left
            else:
                return self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key)
                return self.right
            else:
                return self.right.insert(key)

    # in-order: left, root, right
    def in_order_travers(self, function_ref):
        if self.left:
            self.left.in_order_travers(function_ref)
        function_ref(self)
        if self.right:
            self.right.in_order_travers(function_ref)

    # pre-order: root, left, right
    def pre_order_travers(self, function_ref):
        function_ref(self)
        if self.left:
            self.left.pre_order_travers(function_ref)
        if self.right:
            self.right.pre_order_travers(function_ref)

    # post-order: left, right, root
    def post_order_travers(self, function_ref):
        if self.left:
            self.left.post_order_travers(function_ref)
        if self.right:
            self.right.post_order_travers(function_ref)
        function_ref(self)

    def travers_breadth_first_by_level(self, function_ref_p1_list):
        q1: deque[Tree] = deque()
        q2: deque[Tree] = deque()
        q1.append(self)
        while len(q1) > 0:
            function_ref_p1_list(list(q1))
            while len(q1) > 0:
                node = q1.popleft()
                if node.left is not None:
                    q2.append(node.left)
                if node.right is not None:
                    q2.append(node.right)
            tmp = q1
            q1 = q2
            q2 = tmp

    def travers_breadth_first_by_node(self, function_ref_p1_node):
        q1: deque[Tree] = deque()
        q1.append(self)
        while len(q1) > 0:
            node = q1.popleft()
            function_ref_p1_node(node)
            if node.left is not None:
                q1.append(node.left)
            if node.right is not None:
                q1.append(node.right)


if __name__ == "__main__":
    root = Tree('F')
    root.insert('D')
    root.insert('J')
    root.insert('B')
    root.insert('E')
    root.insert('A')
    root.insert('C')
    root.insert('J')
    root.insert('G')
    root.insert('K')
    root.insert('I')

    print("print in order")
    in_order_list = list()
    root.in_order_travers(lambda node: in_order_list.append(node.key))
    print(in_order_list)
    pre_order_list = list()
    root.pre_order_travers(lambda node: pre_order_list.append(node.key))
    print(pre_order_list)
    post_order_list = list()
    root.post_order_travers(lambda node: post_order_list.append(node.key))
    print(post_order_list)
    # print("print bfs by level")
    # root.travers_breadth_first_by_level(lambda nodes: print(' '.join([str(x.key) for x in nodes])))
    # print("print bfs by node")
    # root.travers_breadth_first_by_node(lambda node: print(str(node.key)))

