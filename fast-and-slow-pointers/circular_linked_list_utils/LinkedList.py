from .ListNode import ListNode


# Template for the circular linked list
class LinkedList:
    # __init__ will be used to make a CircularLinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a circular linked list.
    def insert_node_at_head(self, node):
        if not self.head:
            # If list is empty, the new node will point to itself
            self.head = node
            node.next = node
        else:
            # Insert at head and make last node point to the new head
            last = self.head
            while last.next != self.head:
                last = last.next
            node.next = self.head
            self.head = node
            last.next = self.head  # Update last node to point to new head

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAtHead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = ListNode(x)
            self.insert_node_at_head(new_node)
        
def linked_list_to_array(head):
  if not head:
    return []

  result = []
  current = head
  seen_nodes = set()  

  while current not in seen_nodes:
    result.append(current.val)
    seen_nodes.add(current)
    current = current.next

  return result