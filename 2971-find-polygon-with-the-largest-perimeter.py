class Solution:
    def largestPerimeter(self, nums) -> int:
        if len(nums) < 3:
            return -1
        largest_ele = 0
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if nums[i] < sum(nums[(i+1):]):
                largest_ele = nums[i]
                return sum(nums[(i):])
        return -1




nums = [1,12,1,2,5,50,3]
nums = [5,5,50]
S = Solution()
print(S.largestPerimeter(nums))