class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0
        #Move all non 0 at the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        #Move all 0's at the end manually
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1