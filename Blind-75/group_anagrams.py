import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together.

        Args:
            strs (List[str]): A list of strings to group anagrams.

        Returns:
            List[List[str]]: A list of grouped anagrams.
        """

        # Initialize a defaultdict to store anagrams based on their character frequency
        freq_dict = collections.defaultdict(list)
        
        # Iterate through each word in the input list
        for word in strs:
            # Initialize a list to store the frequency of each character in the word
            chars = [0] * 26
            # Count the frequency of each character in the word
            for ch in word:
                chars[ord(ch) - ord('a')] += 1
            # Convert the list of character frequencies to a tuple and use it as a key to group anagrams
            freq_dict[tuple(chars)].append(word)

        # Return the values of the frequency dictionary, which represent grouped anagrams
        return freq_dict.values()

    """
    Time Complexity: O(n * k), where n is the number of strings in the input list and k is the maximum length of a string.
    The loop iterates through each string in the list and performs operations proportional to the length of the string.
    
    Space Complexity: O(n * k), where n is the number of strings in the input list and k is the maximum length of a string.
    The space complexity is dominated by the frequency dictionary, which stores anagrams based on their character frequencies.
    """
