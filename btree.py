from collections import deque
from typing import Deque

class Tree:
    # TODO: encapsulate properties ("private" or "readonly")
    def __init__(self, key, parent=None):
        self.parent: Tree = parent
        self.left: Tree = None
        self.right: Tree = None
        self.key = key

    # insert
    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Tree(key, self)
                return self.left
            else:
                return self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key, self)
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

    def in_order_travers_loop(self, function_ref):
        stack: Deque[Tree] = deque()
        stack.append(self)
        while stack[-1].left:
            stack.append(stack[-1].left)

        while len(stack):
            current = stack.pop()
            function_ref(current)

            if current.right:
                stack.append(current.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)

    def in_order_travers_parent(self, function_ref):
        vector = "down"
        current = self
        while current:
            if vector == "down":
                while current.left:
                    current = current.left
                    vector = "down"

            if vector != "up_from_r":
                function_ref(current)
            if current.right and vector != "up_from_r":
                vector = "down"
                current = current.right
            elif current.parent:
                vector = "up_from_l" if current.parent.left == current else "up_from_r"
                current = current.parent
            else:
                current = None


if __name__ == "__main__":

    root = Tree('100 - Book')
    root.insert('050 - Chapter 1')
    root.insert('040 - Section 1.1')
    root.insert('060 - Section 1.2')
    root.insert('055 - Section 1.2.1')
    root.insert('065 - Section 1.2.2')
    root.insert('150 - Chapter 2')
    root.insert('120 - Section 2.1')
    root.insert('200 - Section 2.2')
    root.insert('180 - Section 2.2.1')
    root.insert('220 - Section 2.2.2')

    print(">>> in order <<<")
    in_order_list = list()
    root.in_order_travers(lambda node: in_order_list.append(node.key[:3]))
    print(in_order_list)

    print(">>> in order loop <<<")
    in_order_list.clear()
    root.in_order_travers_loop(lambda node: in_order_list.append(node.key[:3]))
    print(in_order_list)

    print(">>> in order parent <<<")
    in_order_list.clear()
    root.in_order_travers_parent(lambda node: in_order_list.append(node.key[:3]))
    print(in_order_list)


"""
    print(">>> BFS <<<")
    root.travers_breadth_first_by_level(lambda nodes: print(','.join([str(x.key[6:]) for x in nodes])))

    # pre-order
    # example:
    #   read book from front to back.
    #   first visit root, then left, left .. then .. right ..,
    #   e.g Book, Chapter 1, Section 1.1, Section 1.2, Section 1.2.1 ..., Chapter 2
    print(">>> pre order <<<")
    pre_order_list = list()
    root.pre_order_travers(lambda node: pre_order_list.append(node.key))
    print(pre_order_list)

    # post-order
    # example:
    #   evaluate expressions. First evaluate its two subtrees (left and right)
    #   and then apply the appropriate binary operator to the results (root)
    #
    root = Tree('100 - *')
    root.insert('050 - +')
    root.insert('040 - 17.5')
    root.insert('060 - /')
    root.insert('055 - 5.0')
    root.insert('065 - X')
    root.insert('150 - -')
    root.insert('120 - Y')
    root.insert('200 - 4.0')
    print(">>> post order <<<")
    post_order_list = list()
    root.post_order_travers(lambda node: post_order_list.append(node.key[6:]))
    print(post_order_list)
"""
