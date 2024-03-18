class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if two strings are anagrams of each other.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if t is an anagram of s, False otherwise.
        """

        # If the lengths of the two strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Dictionary to store the frequency of each character in string s
        char_count = {}

        # Count the frequency of each character in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement the frequency of each character in string t
        # If t is an anagram of s, all counts should become zero
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False

        return True

    """
    Time Complexity: O(n), where n is the length of the input strings s and t.
    The algorithm iterates through each character in both strings.

    Space Complexity: O(n), where n is the number of unique characters in string s.
    The space complexity is dominated by the dictionary char_count, which can store at most the unique characters in string s.
    """
