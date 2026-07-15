class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements in stack have no next greater
        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1]
