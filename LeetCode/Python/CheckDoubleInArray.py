from typing import List


class CheckDoubleInArray:

    def __init__(self):
        arr = [0, 1, 0]
        res = self.checkIfExistOnePass(arr)
        print(res)

    def checkIfExistTwoPass(self, arr: List[int]) -> bool:
        hashmap = {}
        zero_counter = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                product = arr[i] * 2
                hashmap[product] = i
            else:
                zero_counter += 1

        if zero_counter > 1:
            return True

        for i in range(len(arr)):
            # print(hashmap.keys())
            if arr[i] in hashmap.keys():
                return True
        return False

    def checkIfExistOnePass(self, arr: List[int]) -> bool:
        hashmap = {}
        zero_counter = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                product = arr[i] * 2
                dividend = arr[i] / 2
                hashmap[product] = i
                hashmap[dividend] = i + 1
                if arr[i] in hashmap.keys():
                    return True
            else:
                zero_counter += 1

        if zero_counter > 1:
            return True
        else:
            return False
