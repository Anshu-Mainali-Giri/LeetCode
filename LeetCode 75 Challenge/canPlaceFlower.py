class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        Determine if n flowers can be planted in flowerbed without violating the rule:
        No two adjacent flowers can be planted.
        
        Approach: Greedy - plant flowers as early as possible
        Time Complexity: O(len(flowerbed))
        Space Complexity: O(1)
        """
        
        # Iterate through each position in the flowerbed
        for i in range(len(flowerbed)):
            # Check if current position is empty (0 means no flower)
            if flowerbed[i] == 0:
                # Check if left neighbor is empty (or we're at the start)
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                # Check if right neighbor is empty (or we're at the end)
                empty_right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                # If both neighbors are empty, we can plant a flower here
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant the flower
                    n -= 1  # Decrease remaining flowers to plant

                    # Early termination: if we've planted all required flowers
                    if n == 0:
                        return True
            
        # Return True if we've planted all flowers (n <= 0)
        return n <= 0
        