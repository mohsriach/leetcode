class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculate the number of possible unique paths for a robot to reach the bottom-right corner of a grid.

        Args:
            m (int): An integer representing the number of rows in the grid.
            n (int): An integer representing the number of columns in the grid.

        Returns:
            int: The number of possible unique paths for the robot to reach the bottom-right corner.
        """

        # Initialize a 2D array to store the number of unique paths for each cell
        dp_val = [[1 for c in range(n)] for r in range(m)]
        
        # Calculate the number of unique paths for each cell using dynamic programming
        for r in range(1, m):
            for c in range(1, n):
                dp_val[r][c] = dp_val[r - 1][c] + dp_val[r][c - 1]
        
        # Return the number of unique paths for the bottom-right corner
        return dp_val[m - 1][n - 1]

    """
    Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
    The nested loops iterate through each cell in the grid, performing constant-time operations.
    Space Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
    The space complexity is dominated by the dp_val 2D array, which stores the number of unique paths for each cell.
    """
