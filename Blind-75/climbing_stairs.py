class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the distinct ways to climb to the top of a staircase.

        Args:
            n (int): An integer representing the number of steps to reach the top.

        Returns:
            int: The number of distinct ways to climb to the top of the staircase.
        """

        # Initialize a list to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases: if there are 1 or 2 steps, there are 1 and 2 ways respectively
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initial values for 1 and 2 steps
        dp[1] = 1
        dp[2] = 2

        # Calculate the number of ways to reach each step using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the number of ways to reach the top step
        return dp[n]

    """
    Time Complexity: O(n), where n is the number of steps to reach the top.
    The loop iterates through each step from 3 to n, performing constant-time operations.
    Space Complexity: O(n), where n is the number of steps to reach the top.
    The space complexity is dominated by the dp list, which stores the number of ways to reach each step.
    """
