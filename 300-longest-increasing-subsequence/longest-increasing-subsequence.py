import bisect

class Solution:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            # Find position to replace
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
