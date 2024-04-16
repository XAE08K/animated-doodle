class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=max(piles)
        l=1
        r=max(piles)
        while l<=r:
            hrs=0
            mid=l+((r-l)//2)
            for i in range(len(piles)):
                hrs+=math.ceil(piles[i]/mid)
            if hrs>h:
                l=mid+1
            else:
                res=min(res,mid)
                r=mid-1
        return res

