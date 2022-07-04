from typing import List


class RemoveElement:

    def __init__(self):
        nums = [3, 2, 2, 3]
        val = 3
        res = self.removeElement(nums, val)
        print(res)

    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums) - 1):
            if nums[i] == val:
                c += 1

        for i in range(len(nums) - c):
            if nums[i] == val:
                nums[i] = nums[i + 1]
