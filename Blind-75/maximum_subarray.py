from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the subarray with the largest sum.

        Args:
            nums (List[int]): An integer array.

        Returns:
            int: The sum of the subarray with the largest sum.
        """

        # Handle the edge case where the array has only one element
        if len(nums) == 1:
            return nums[0]
        
        # Initialize variables to track current sum and maximum sum
        curr_sum = res = nums[0]

        # Iterate through the array, updating current sum and maximum sum
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)  # Update current sum
            res = max(res, curr_sum)  # Update maximum sum

        # Return the maximum sum found
        return res

    """
    Time Complexity: O(n), where n is the length of the input array nums.
    The algorithm iterates through the array once, performing constant-time operations.

    Space Complexity: O(1).
    The algorithm uses only a constant amount of extra space regardless of the input size.
    """
