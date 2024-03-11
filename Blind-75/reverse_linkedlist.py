class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse the singly linked list.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            Optional[ListNode]: The head node of the reversed linked list.
        """

        # Initialize a pointer to track the previous node
        prev = None

        # Iterate through the linked list
        while head:
            # Save the current node
            curr = head
            # Move head pointer to the next node
            head = head.next
            # Reverse the next pointer of the current node to point to the previous node
            curr.next = prev
            # Update the previous node to the current node
            prev = curr

        # Return the new head of the reversed linked list
        return prev

    """
    Time Complexity: O(n), where n is the number of nodes in the linked list.
    The algorithm iterates through each node once to reverse the linked list.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
