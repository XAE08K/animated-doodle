class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        i = 0
        while i < length:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n

        
