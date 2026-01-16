class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self, arr):
        self.head = None
        tail = None
        for v in arr:
            node = Node(v)
            if not self.head:
                self.head = node
                tail = node
            else:
                tail.next = node
                tail = node

    def print_list_with_forward_arrow(self, head):
        cur = head
        parts = []
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        print(' -> '.join(parts))