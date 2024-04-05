from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determine the maximum amount of money a robber can rob without alerting the police.

        Args:
            nums (List[int]): An integer array representing the amount of money of each house.

        Returns:
            int: The maximum amount of money that can be robbed.
        """

        # If there are no houses, return 0
        if not nums:
            return 0

        # Iterate through the houses starting from the second one
        for i in range(1, len(nums)):
            # If it's the second house, compare the money of the first two houses
            if i == 1:
                nums[i] = max(nums[i], nums[i - 1])
            else:
                # For subsequent houses, compare the money of robbing the current house
                # with the money of robbing the previous house and the house before the previous one
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])

        # Return the maximum amount of money that can be robbed
        return nums[-1]

    """
    Time Complexity: O(n), where n is the number of houses.
    The algorithm iterates through the houses once.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
