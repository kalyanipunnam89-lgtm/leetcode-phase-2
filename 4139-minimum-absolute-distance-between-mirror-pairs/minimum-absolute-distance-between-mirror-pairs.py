class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x):
            return int(str(x)[::-1])
        pos={}
        ans=float('inf')
        for i,x in enumerate(nums):
            if x in pos:
                ans=min(ans,i-pos[x])
            pos[reverse_num(x)]=i
        return -1 if ans== float('inf') else ans        


        