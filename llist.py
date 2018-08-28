
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

    def detect_loop(self):
        slow_p = fast_p = self

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            # If slow_p and fast_p meet at some point then there is a loop
            if slow_p == fast_p:
                # Return slow or fast to indicate that loop is found
                return slow_p

                # Return 0 to indicate that there is no loop
        return None

        # Function to remove loop

    # loop_node --> pointer to one of the loop nodes
    def remove_loop(self, loop_node):
        # Fix one pointer to head
        # And the other pointer to k (# of nodes in the loop) nodes after head
        ptr1 = loop_node
        ptr2 = self.next
        while ptr1.next != loop_node:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1 = self

        # Move both pointers at the same place
        # they will meet at loop starting node
        while ptr2 != ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node
        ptr2 = ptr2.next
        while ptr2.next != ptr1:
            ptr2 = ptr2.next

        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None

    # Function to insert a new node at the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self
        return new_node

    # Utility function to print the linked LinkedList
    def print_list(self):
        temp = self
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    tail = Node(0)
    head = tail
    for i in range(1,20):
        head = head.push(i)

    # Create a loop for testing
    tail.next = head.next.next.next.next.next
    loop_node = head.detect_loop()
    print("Loop node: " + str("none" if loop_node is None else loop_node.data))
    head.remove_loop(loop_node)
    print("Linked List after removing loop")
    head.print_list()
