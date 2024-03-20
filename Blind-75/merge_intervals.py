from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals into non-overlapping intervals.

        Args:
            intervals (List[List[int]]): A list of intervals where each interval is represented as [start, end].

        Returns:
            List[List[int]]: A list of non-overlapping intervals.
        """

        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        # Initialize a list to store the merged intervals
        res = [intervals[0]]

        # Iterate through the sorted intervals
        for start, end in intervals[1:]:
            # Get the end time of the last merged interval
            prev_end = res[-1][1]
            # If the current interval overlaps with the last merged interval, merge them
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                # If there's no overlap, add the current interval to the result
                res.append([start, end])
        
        return res

    """
    Time Complexity: O(n log n), where n is the number of intervals in the input list.
    Sorting the intervals takes O(n log n) time, and merging the intervals takes O(n) time.

    Space Complexity: O(n), where n is the number of intervals in the input list.
    The space complexity is dominated by the result list, which can store at most n intervals.
    """
