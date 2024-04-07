from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive elements sequence.

        Args:
            nums (List[int]): An unsorted array of integers.

        Returns:
            int: The length of the longest consecutive elements sequence.
        """

        # If the array is empty, return 0
        if len(nums) == 0:
            return 0

        # If the array has only one element, return 1
        if len(nums) == 1:
            return 1

        # Initialize the result variable
        res = 0

        # Create a set to store the numbers for efficient lookup
        num_set = set(nums)

        # Iterate through the numbers in the array
        for num in nums:
            # If num - 1 is not in the set, start counting the consecutive sequence
            if num - 1 not in num_set:
                seq_len = 1
                curr_num = num + 1
                
                # Continue counting consecutive numbers
                while curr_num in num_set:
                    curr_num += 1
                    seq_len += 1
                
                # Update the maximum sequence length
                res = max(res, seq_len)

        return res

    """
    Time Complexity: O(n), where n is the number of elements in the input array.
    The algorithm iterates through the array once, and each lookup in the set takes constant time.

    Space Complexity: O(n), where n is the number of elements in the input array.
    The space complexity is dominated by the set, which can store at most n elements.
    """
