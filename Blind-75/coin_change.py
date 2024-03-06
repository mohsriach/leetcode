import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Calculate the fewest number of coins needed to make up a given amount of money.

        Args:
            coins (List[int]): A list of integers representing coins of different denominations.
            amount (int): An integer representing the total amount of money.

        Returns:
            int: The fewest number of coins needed to make up the given amount of money. 
                 If the amount of money cannot be made up by any combination of the coins, return -1.
        """

        # If the amount is in the coins list, return 1 as the only coin is needed
        if amount in coins:
            return 1

        # Initialize a queue with the remaining amount and the number of coins used
        queue = collections.deque([(amount, 0)])
        # Initialize a set to keep track of visited amounts
        visit = set()
        # Add the initial amount to the visited set
        visit.add(amount)

        # BFS traversal to find the fewest number of coins needed
        while queue:
            # Pop the amount and number of coins used from the queue
            amount_rem, coins_used = queue.popleft()
            # If the remaining amount is 0, return the number of coins used
            if amount_rem == 0:
                return coins_used

            # Iterate through each coin denomination
            for coin in coins:
                # Check if subtracting the current coin doesn't result in negative amount
                # and if the resulting amount hasn't been visited before
                if amount_rem - coin >= 0 and (amount_rem - coin) not in visit:
                    # Add the resulting amount to visited set
                    visit.add(amount_rem - coin)
                    # Append the new remaining amount and updated number of coins used to the queue
                    queue.append((amount_rem - coin, coins_used + 1))
        
        # If no combination of coins can make up the given amount, return -1
        return -1

    """
    Time Complexity: O(N * amount), where N is the number of coins and amount is the given total amount.
    Each amount can be visited once for each coin denomination, resulting in a maximum of O(N * amount) iterations.
    Space Complexity: O(amount), where amount is the given total amount.
    The space complexity is dominated by the queue and the visited set, both of which can grow up to the size of the amount.
    """
