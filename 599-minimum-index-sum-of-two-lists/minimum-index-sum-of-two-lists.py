class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        for j, word in enumerate(list2):
            if word in index_map:
                s = j + index_map[word]
                if s < min_sum:
                    min_sum = s
                    result = [word]
                elif s == min_sum:
                    result.append(word)
        return result
