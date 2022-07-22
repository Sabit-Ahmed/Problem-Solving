from typing import List


class ValidMountainArray:

    def __init__(self):
        res = self.validMountainArray([3,5,6])
        print(res)

    def validMountainArray(self, arr: List[int]) -> bool:
        mid = arr.index(max(arr))
        # print(mid)
        i = j = mid
        left = mid - 1
        right = mid + 1

        if mid == 0 or mid == len(arr) - 1:
            return False

        if len(arr) <= 2:
            return False

        while i > 0:
            # print(f"i:: {i}")
            # print(f"left:: {left}")

            if arr[left] >= arr[i]:
                return False
            if arr[left] < arr[i]:
                left -= 1
                i -= 1

        while j < len(arr) - 1:
            # print(f"j:: {j}")
            # print(f"right:: {right}")

            if arr[right] >= arr[j]:
                return False

            if arr[right] < arr[j]:
                right += 1
                j += 1

        return True
