class Solution(object):
    def productExceptSelf(self, nums):
        """
        Return array where each element is the product of all elements except itself.
        Cannot use division and must solve in O(n) time.
        
        Approach: Two-pass with prefix and suffix products
        1. First pass (left to right): Calculate prefix products
        2. Second pass (right to left): Multiply with suffix products
        
        Time Complexity: O(n)
        Space Complexity: O(1) extra space (not counting output array)
        
        Example: [1,2,3,4] → [24,12,8,6]
        For index 0: 2*3*4=24, For index 1: 1*3*4=12, etc.
        """
        
        n = len(nums)
        # Initialize answer array with 1s
        answer = [1] * n

        # Step 1: Calculate prefix products (product of all elements to the left)
        # answer[i] will contain product of all elements before index i
        prefix = 1
        for i in range(n):
            answer[i] = prefix  # Store prefix product before including nums[i]
            prefix *= nums[i]   # Update prefix to include nums[i] for next iteration

        # Step 2: Multiply with suffix products (product of all elements to the right)
        # Now answer[i] contains prefix, multiply it with suffix to get final result
        suffix = 1
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            answer[i] *= suffix  # Multiply existing prefix with suffix
            suffix *= nums[i]    # Update suffix to include nums[i] for next iteration

        return answer
