from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum amount of water a container can store.

        Args:
            height (List[int]): An integer array representing the heights of vertical lines.

        Returns:
            int: The maximum amount of water that can be stored by a container.
        """

        # Initialize pointers for the left and right boundaries of the container
        left = 0
        right = len(height) - 1
        max_area = 0

        # Continue until left pointer crosses right pointer
        while left < right:
            # Calculate the current area formed by the container
            curr_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is greater
            max_area = max(max_area, curr_area)
            # Move the pointer of the shorter vertical line towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    """
    Time Complexity: O(n), where n is the length of the input height array.
    The algorithm iterates through the array using two pointers which move towards each other.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
