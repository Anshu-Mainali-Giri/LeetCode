class Solution(object):
    def increasingTriplet(self, nums):
        """
        Check if there exists an increasing triplet subsequence (i < j < k and nums[i] < nums[j] < nums[k]).
        
        Approach: Track two smallest values seen so far
        - first: smallest value seen
        - second: smallest value greater than first
        - If we find a value greater than second, we have our triplet
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Example: [1,2,3,4,5] → True (1 < 2 < 3)
        Example: [5,4,3,2,1] → False (no increasing triplet)
        """
        
        # Initialize with infinity (largest possible values)
        first = float('inf')   # Smallest number seen so far
        second = float('inf')  # Second smallest number seen so far

        for num in nums:
            # If current number is smallest or equal to first, update first
            if num <= first:
                first = num
            # If current number is between first and second, update second
            elif num <= second:
                second = num
            # If current number is greater than both first and second
            # We found our increasing triplet: first < second < num
            else:
                return True

        # No increasing triplet found
        return False
 
        