from typing import List


class RemoveDuplicatesFromSortedArray:

    def __init__(self):
        nums = [0,1,1,0]
        res = self.removeDuplicates(nums)
        print(res)

    def removeDuplicates(self, nums: List[int]) -> int:
        c = len(set(nums))
        i = 0
        j = 0
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                j += 1
            else:
                nums[i - j] = nums[i]
            i += 1
        print(nums)
        return len(nums[:c])
