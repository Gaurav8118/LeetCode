class Solution(object):
    def findLongestChain(self, pairs):
        # Step 1: Sort pairs by their right endpoint
        pairs.sort(key=lambda x: x[1])
        
        # Step 2: Greedy selection
        curr_end = float('-inf')
        chain_length = 0
        
        for left, right in pairs:
            if left > curr_end:
                chain_length += 1
                curr_end = right
        
        return chain_length


# Example 1
print(Solution().findLongestChain([[1,2],[2,3],[3,4]]))  # Output: 2

# Example 2
print(Solution().findLongestChain([[1,2],[7,8],[4,5]]))  # Output: 3

        