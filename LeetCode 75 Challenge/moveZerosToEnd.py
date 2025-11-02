class Solution(object):
    def moveZeroes(self, nums):
        """
        Move all zeros to the end while maintaining relative order of non-zero elements.
        Modify the array in-place.
        
        Approach: Two-pass algorithm
        1. First pass: Move all non-zero elements to the front
        2. Second pass: Fill remaining positions with zeros
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Example: [0,1,0,3,12] → [1,3,12,0,0]
        """
        
        # Pointer to track where to insert the next non-zero element
        insert_pos = 0
        
        # First pass: Move all non-zero elements to the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                # Place non-zero element at insert_pos and move pointer forward
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        # Second pass: Fill remaining positions with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1