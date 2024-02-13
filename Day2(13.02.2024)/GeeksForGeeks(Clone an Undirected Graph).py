Clone an Undirected Graph :

Solution:

import sys
sys.setrecursionlimit(10**6)
class Solution():
    def cloneGraph(self, node):
        d={}
        
        def util(nod):
            if nod.val in d:
                return d[nod.val]
            d[nod.val]=Node(nod.val,[])
            for n in nod.neighbors:
                d[nod.val].neighbors.append(util(n))
            return d[nod.val]
            
        return util(node)
