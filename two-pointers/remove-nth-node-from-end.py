
#Time O(N). Where N is the number of nodes in the linked list 
#Space O(1). Because only we use constant space to store two pointers 
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


def print_list_with_forward_arrow(head):
    cur = head
    parts = []
    while cur:
        parts.append(str(cur.val))
        cur = cur.next
    print(' -> '.join(parts))


def remove_nth_node_from_end(head, n):
    left = head
    right = head

    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head


def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28],
             [34, 53, 6, 95, 38, 28, 17, 63, 16, 76],
             [288, 224, 275, 390, 4, 383, 330, 60, 193],
             [1, 2, 3, 4, 5, 6, 7, 8, 9],
             [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    ns = [4, 1, 6, 9, 11]

    for i in range(len(ns)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i + 1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print()
        print("n = ", ns[i])
        result = remove_nth_node_from_end(input_linked_list.head, ns[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print()
        print("-" * 100)


if __name__ == '__main__':
    main()