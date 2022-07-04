from typing import List


class RemoveElement:

    def __init__(self):
        nums = [3, 2, 2, 3]
        val = 3
        res = self.removeElement(nums, val)
        print(res)

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == val:
                nums[i] = nums[i + 1]

        return
