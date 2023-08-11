class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0;

        j = 0 ;
        for i in range(len(nums)):
            if nums[i]:
                tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                j=j+1;