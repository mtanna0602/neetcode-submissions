class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for num in nums:
            if num-1 not in s:
                length=1
                next= num+1
                while next in s:
                    length += 1
                    next += 1
                longest = max(longest, length)
        return longest
        