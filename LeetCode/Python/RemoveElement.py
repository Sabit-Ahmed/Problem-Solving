from typing import List


class RemoveElement:

    def __init__(self):
        nums = [3,2,2,3]
        val = 3
        res = self.removeElement(nums, val)
        print(res)

    def removeElement(self, nums: List[int], val: int) -> int:

        c = 0
        for k in nums:
            if k == val:
                c += 1

        if c == 0:
            return len(nums)
        elif c == len(nums):
            nums.clear()
            return len(nums)
        else:
            i = 0
            j = 0
            while i < len(nums) - 1:
                if nums[i] == val:
                    if nums[i + 1] == val:
                        j += 1
                    else:
                        nums[i - j] = nums[i + 1]
                        nums[i + 1] = val
                i += 1

            return len(nums) - c

