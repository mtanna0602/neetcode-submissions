class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        l=0
        max_length=0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            curr_length = r-l+1
            max_length= max(curr_length, max_length)
        return max_length