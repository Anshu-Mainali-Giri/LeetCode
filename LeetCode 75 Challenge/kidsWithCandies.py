class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest = max(candies)
        result = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= highest:
                result.append(True)
            else:
                result.append(False)
            
        return result    