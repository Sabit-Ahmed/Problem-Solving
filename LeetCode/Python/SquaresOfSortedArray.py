from typing import List


class SquaresOfSortedArray:

    def __init__(self):
        res = self.sortedSquares([-3, 2, 3])
        print(res)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
