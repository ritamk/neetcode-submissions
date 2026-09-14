class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsChecked = set()
        for num in nums:
            if num in numsChecked:
                return True
            numsChecked.add(num)
        return False
