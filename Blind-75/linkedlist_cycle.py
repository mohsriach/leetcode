class ListNode:
    def __init__(self, val=0, next=None):
  
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determine if the linked list has a cycle.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            bool: True if there is a cycle in the linked list, False otherwise.
        """

        # Handle the case where the linked list is empty
        if not head:
            return False
        
        # Initialize slow and fast pointers to the head of the linked list
        slow, fast = head, head

        # Move slow pointer by one step and fast pointer by two steps
        # If there's a cycle, they will meet at some point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        # If fast pointer reaches the end of the list, there's no cycle
        return False

    """
    Time Complexity: O(n), where n is the number of nodes in the linked list.
    The algorithm iterates through each node at most once.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
