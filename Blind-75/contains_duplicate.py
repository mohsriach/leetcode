from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determine if any value appears at least twice in the integer array.

        Args:
            nums (List[int]): An integer array.

        Returns:
            bool: True if any value appears at least twice, False otherwise.
        """

        # Dictionary to store the frequency of each number
        num_dict = {}

        # Iterate through the array
        for num in nums:
            # If the number is already in the dictionary, return True
            if num in num_dict:
                return True
            else:
                # Otherwise, add the number to the dictionary
                num_dict[num] = 1

        # If no number appears at least twice, return False
        return False

    """
    Time Complexity: O(n), where n is the length of the input array nums.
    The algorithm iterates through each element of the array once.

    Space Complexity: O(n), where n is the length of the input array nums.
    The space complexity is dominated by the dictionary, which can store up to n elements.
    """
