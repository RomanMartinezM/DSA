# Time: O(n) where n is the number of nodes in the linked list
# Space: O(1) because no extra space is required

from linked_list.linked_list import LinkedList
from linked_list.reverse_linked_list import LinkedListReversal

def compare_two_halves(first_half, second_half): 
    while first_half is not None and second_half is not None:
        if first_half.val != second_half.val:
            return False
        
        first_half = first_half.next
        second_half = second_half.next
        
    return True

def palindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rev = LinkedListReversal.reverse_linked_list(slow)
    is_palindrome = compare_two_halves(head, rev)

    LinkedListReversal.reverse_linked_list(rev)

    if is_palindrome:
        return True
    return False


def main():
    test_cases = (
            [2, 4, 6, 4, 2],
            [0, 3, 5, 5, 0],
            [9, 7, 4, 4, 7, 9],
            [5, 4, 7, 9, 4, 5],
            [5, 9, 8, 3, 8, 9, 5],
        )

    for i in range(len(test_cases)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(test_cases[i])
        print(i+1, ".\tLinked List:", end=" ", sep="")
        input_linked_list.print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
	