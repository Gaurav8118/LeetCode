from collections import Counter

class Solution:
    def findLHS(self, nums):
        counts = Counter(nums)
        longest = 0
        for num in counts:
            if num + 1 in counts:
                longest = max(longest, counts[num] + counts[num + 1])
        return longest
