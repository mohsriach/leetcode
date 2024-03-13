class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string of brackets is valid.

        Args:
            s (str): The input string containing just the characters '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the input string is valid, False otherwise.
        """

        # Lists of open and close brackets for easy indexing
        open_b = ['(', '{', '[']
        close_b = [')', '}', ']']

        # Stack to keep track of open brackets
        res = []

        # Iterate through each character in the input string
        for i in s:
            # If the character is an open bracket, push it onto the stack
            if i in open_b:
                res.append(i)
            else:
                # If the stack is empty or the current close bracket doesn't match the last open bracket, return False
                if not res or close_b.index(i) != open_b.index(res[-1]):
                    return False
                else:
                    # Pop the last open bracket from the stack
                    res.pop()

        # If the stack is empty, all open brackets have been properly closed
        return len(res) == 0

    """
    Time Complexity: O(n), where n is the length of the input string.
    The algorithm iterates through each character of the input string exactly once.

    Space Complexity: O(n), in the worst case, all characters are open brackets, 
    and we push all of them onto the stack before starting to pop.
    """
