class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        
        for i in range(len(candies)):
            total=candies[i]+extraCandies
            res.append(total>=max(candies))
        return res
        
