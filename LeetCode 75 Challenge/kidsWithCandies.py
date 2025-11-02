class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        Determine which kids will have the greatest number of candies 
        if they receive all extra candies.
        
        Approach: 
        1. Find the current maximum candies any kid has
        2. For each kid, check if their candies + extraCandies >= maximum
        
        Time Complexity: O(n) where n is number of kids
        Space Complexity: O(n) for the result array
        
        Example: candies=[2,3,5,1,3], extraCandies=3
        Max = 5, so results: [True,True,True,False,True]
        """
        
        # Step 1: Find the current maximum number of candies any kid has
        highest = max(candies)
        
        # Step 2: Create result array to store boolean answers
        result = []
        
        # Step 3: Check each kid
        for i in range(len(candies)):
            # If this kid gets all extra candies, will they have >= highest?
            if (candies[i] + extraCandies) >= highest:
                result.append(True)   # Yes, they'll have the most (or tied for most)
            else:
                result.append(False)  # No, they still won't have the most
            
        return result    