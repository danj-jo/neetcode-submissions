class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsArr = list(nums)
        for item in nums:
            numsArr.append(item)
        return numsArr    