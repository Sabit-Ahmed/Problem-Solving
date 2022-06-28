from typing import List


class LongestCommonPrefix14:

    def __init__(self):
        res = self.longestCommonPrefixWithBST(["ab","a"])
        # print(res)

    def longestCommonPrefixBruteForce(self, strs: List[str]) -> str:
        minLength = 999999999999
        indexOfMinElement = -1
        for (i, v) in enumerate(strs):
            if len(v) < minLength:
                minLength = len(v)
                indexOfMinElement = i
        outputStr = ""
        for k in range(len(strs[indexOfMinElement])):
            for i in range(len(strs)):
                if str.lower(strs[indexOfMinElement][k]) == str.lower(strs[i][k]):
                    if i == len(strs) - 1:
                        outputStr = outputStr + strs[indexOfMinElement][k]
                else:
                    return outputStr

        return outputStr

    def longestCommonPrefixWithBST(self, strs: List[str]) -> str:


        outputStr = ""
        strs.sort(key=len)
        minElement = strs[0]
        strs = strs[1:]
        mid = int(len(minElement) / 2)
        left = strs[0:mid]
        right = strs[mid + 1:len(minElement) - 1]

        while(left != right):
            for i in strs:
                if left is in i:


    # def findCommonPrefix(self, index, strs):

