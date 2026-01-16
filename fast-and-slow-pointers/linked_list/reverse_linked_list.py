class LinkedListReversal:
    def reverse_linked_list(slow):
        prev = next = None 
        curr = slow

        while curr is not None:
            next = curr.next
            curr.next = prev 
            prev = curr 
            curr = next
        
        return prev


