from typing import List


class NonDecreasingArray:

    def __init__(self):
        res = self.checkPossibility([3, 2, 3])
        print(res)

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
