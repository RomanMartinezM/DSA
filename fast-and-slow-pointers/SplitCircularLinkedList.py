# Time complexity: O(n), where n is the number of nodes in the circular linked list
# Space complexity: O(1), because no extra space is required

from circular_linked_list_utils.LinkedList import LinkedList
from circular_linked_list_utils.PrintList import print_circular_linked_list
from circular_linked_list_utils.LinkedList import linked_list_to_array

def split_circular_linked_list(head):
    slow = fast = head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    head1 = head
    head2 = slow.next
    slow.next = head1

    fast = head2
    while fast.next != head:
        fast = fast.next
    
    fast.next = head2

    return [head1, head2]

def main():
    lists =  [[1, 5, 7],         
            [2, 6, 1, 5],      
            [3, 1, 4, 2, 5],   
            [8, 10, 12, 14, 16, 18],  
            [9, 10]]

    for i in range(len(lists)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(f"{i + 1}.\tLinked list: ", end="")
        print_circular_linked_list(input_linked_list.head)
        # Get the split lists
        head1, head2 = split_circular_linked_list(input_linked_list.head)
        split_list_1 = linked_list_to_array(head1)
        split_list_2 = linked_list_to_array(head2)
        print(f"\n\tSplit Lists: [{split_list_1}, {split_list_2}]")
        print("-" * 100)


if __name__ == "__main__":
    main()