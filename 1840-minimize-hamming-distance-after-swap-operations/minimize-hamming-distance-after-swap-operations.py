class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent=list(range(len(source)))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        for a,b in allowedSwaps:
            parent[find(a)]=find(b)
        groups=defaultdict(Counter)
        for i in range(len(source)):
            groups[find(i)][source[i]]+=1
        ans=0
        for i in range(len(target)):
            root=find(i)
            if groups[root][target[i]]>0:
                groups[root][target[i]]-=1
            else:
                ans+=1
        return ans            
        