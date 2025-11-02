class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Find the maximum average of any subarray of length k.
        
        Approach: Sliding Window Technique
        - Calculate sum of first k elements
        - Slide the window by removing leftmost element and adding rightmost element
        - Keep track of maximum sum found
        
        Time Complexity: O(n) where n is length of nums
        Space Complexity: O(1)
        """
        
        # Step 1: Calculate sum of first k elements (initial window)
        # Example: nums=[1,12,-5,-6,50,3], k=4
        # First window: [1,12,-5,-6] = sum = 2
        total = sum(nums[:k])
        
        # Step 2: Initialize maxVal with the first window's sum
        maxVal = total
        
        # Step 3: Slide the window from position k to end of array
        for i in range(k, len(nums)):
            # Sliding window technique:
            # - Add new element (nums[i]) entering the window
            # - Remove old element (nums[i-k]) leaving the window
            # 
            # Example at i=4: 
            # Old window: [1,12,-5,-6], New window: [12,-5,-6,50]
            # total = 2 + 50 - 1 = 51
            total += nums[i] - nums[i-k]
            
            # Step 4: Update maximum sum if current sum is larger
            if total > maxVal:
                maxVal = total
        
        # Step 5: Return maximum average (convert to float for precision)
        return maxVal / float(k)