class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.

        Args:
            list1 (Optional[ListNode]): The head node of the first sorted linked list.
            list2 (Optional[ListNode]): The head node of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head node of the merged sorted linked list.
        """

        # Create a dummy node and point curr to it 
        dummy = ListNode()
        curr = dummy

        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next 

            curr = curr.next 
        
        # Connect the remaining nodes of the non-empty list
        curr.next = list1 or list2 

        # Return the head of the merged sorted linked list
        return dummy.next

    """
    Time Complexity: O(n + m), where n and m are the lengths of the two input linked lists.
    The algorithm traverses both lists once.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
