import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal of the binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[List[int]]: The level order traversal of the binary tree.
        """

        # Handle the case where the root is None
        if not root:
            return []
        
        # Initialize a deque to store nodes for level order traversal
        que = collections.deque([root])
        # Initialize a list to store the result of level order traversal
        res = []

        # Perform level order traversal using BFS
        while que:
            curr_level = []
            # Process nodes at the current level
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    # Add node value to the current level
                    curr_level.append(node.val)
                    # Add left and right children of the node to the queue
                    que.append(node.left)
                    que.append(node.right)
            
            # Add the current level to the result if it's not empty
            if curr_level:
                res.append(curr_level)
            
        # Return the result of level order traversal
        return res

    """
    Time Complexity: O(n), where n is the number of nodes in the binary tree.
    The algorithm visits each node once during the level order traversal.

    Space Complexity: O(n), where n is the number of nodes in the binary tree.
    The space complexity is dominated by the queue, which can hold at most all nodes in one level of the tree.
    """
