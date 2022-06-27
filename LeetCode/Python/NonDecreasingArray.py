from typing import List


class NonDecreasingArray:

    def __init__(self):
        res = self.checkPossibility([3, 2, 3])
        print(res)

    # @staticmethod
    # def checkPossibility(nums: List[int]) -> bool:
    #     count = 0
    #     n = len(nums) - 1
    #
    #     if nums[0] > nums[1]:
    #         count += 1
    #     if nums[n] < nums[n - 1]:
    #         count += 1
    #
    #     for i in range(n):
    #         if 0 < i < n - 1:
    #             if nums[i] > nums[i + 1]:
    #                 count += 1
    #                 if i + 2 < n or i + 2 == n:
    #                     if nums[i] > nums[i + 2]:
    #                         count += 1
    #
    #     if count > 1:
    #         return False
    #     else:
    #         return True

    @staticmethod
    def checkPossibility(nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if count > 1:
                break
            if i > 0:
                if nums[i - 1] > nums[i]:
                    count += 1
                    if i > 1:
                        if nums[i - 2] > nums[i]:
                            nums[i] = nums[i - 1]
                        else:
                            nums[i - 1] = nums[i]

            print(nums)

        if count > 1:
            return False
        else:
            return True
