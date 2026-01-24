# Template for printing the linked list with forward arrows

def print_circular_linked_list(linked_list_node):
    if not linked_list_node:
        print("List is empty", end=" ")
        return

    temp = linked_list_node
    seen_nodes = set()  # To track nodes we've already printed

    while temp and temp not in seen_nodes:
        print(temp.val, end=" ")  # print node value
        seen_nodes.add(temp)  # Add current node to seen nodes

        temp = temp.next
        if temp == linked_list_node:  # When we come back to the head node
            print("→ (head)", end=" ")
            break
        if temp:
            print("→", end=" ")
    print()  # Move to the next line after printing
