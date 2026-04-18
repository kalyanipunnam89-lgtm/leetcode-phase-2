class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror=int(str(n)[::-1])
        return abs(n-mirror)  
        