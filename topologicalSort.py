class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        inDegree = [0]*V
        res = []
        queue = []
        
        for i in range(V):
            for ver in adj[i]:
                inDegree[ver] += 1
                
        for i in range(V):
            if inDegree[i] == 0:
                queue.append(i)
        while(queue):
            x = queue.pop(0)
            res.append(x)
            for ver in adj[x]:
                inDegree[ver] -= 1
                if inDegree[ver] == 0:
                    queue.append(ver)
                 
       
        return res