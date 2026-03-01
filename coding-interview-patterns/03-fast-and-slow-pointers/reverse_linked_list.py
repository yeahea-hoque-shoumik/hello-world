from concept.LinkedList.LinkedList import LinkedList


def palindrome(head):
    # Initialize slow and fast pointers to the head of the linked list
    slow = head
    fast = head

    # Find the middle of the linked list using the slow and fast pointers
    while fast and fast.next:
        # move slow one step forward
        slow = slow.next
        # move fast two steps forward
        fast = fast.next.next
    second_list=LinkedList(slow)
    # Reverse the second half of the linked list starting from the middle node
    revert_data = second_list.__reversed__();

    # Compare the first half of the linked list with the reversed second half of the linked list
    check = compare_two_halves(head, revert_data)

    # Re-reverse the second half of the linked list to restore the original linked list
    second_list.__reversed__()

    # Return True if the linked list is a palindrome, else False
    if check:
        return True
    return False


def compare_two_halves(first_half, second_half):
    # Compare the corresponding nodes of the first and second halves of the linked list
    while first_half and second_half:
        if first_half.val != second_half.val:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True


# Driver code
if __name__ == "__main__":
    input = (
        [2, 4, 6, 4, 2],
        [0, 3, 5, 5, 0],
        [9, 7, 4, 4, 7, 9],
        [5, 4, 7, 9, 4, 5],
        [5, 9, 8, 3, 8, 9, 5],
    )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        print(input_linked_list)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
        j += 1
        print("-" * 100, "\n")

