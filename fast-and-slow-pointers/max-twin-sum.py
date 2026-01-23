# Time Complexity: O(n), where n is the number of nodes in the linked list
# Space Complexity: O(1), because no extra space is required
from linked_list_utils.LinkedList import LinkedList
from linked_list_utils.PrintList import print_list_with_forward_arrow

def max_twin_sum(head):
    slow = fast = head 

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    curr = slow
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    curr = head
    max_sum = 0
    while prev is not None:
        if curr.val + prev.val > max_sum:
            max_sum = curr.val + prev.val
        curr = curr.next
        prev = prev.next

    return max_sum

def main():
    test_cases = [[2, 3, 5, 7],
            [81, 144, 64, 121, 25, 49],
            [4, 5, 6, 7],
            [1, 1000],
            [11, 77, 44, 99, 22, 66, 55, 88]]

    for i in range(len(test_cases)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(test_cases[i])
        print(i+1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMaximum twin sum: ", max_twin_sum(input_linked_list.head))
        print("-"*100)

if __name__ == "__main__":
    main()
        