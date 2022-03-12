from queue import PriorityQueue
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        res = [float('inf')]*V
        queue = PriorityQueue()
        
        res[S] = 0
        queue.put([0,S])
        
        while not queue.empty():
            [preCost, preNode] = queue.get()
            for [ver, cost] in adj[preNode]:
                if preCost + cost < res[ver]:
                    res[ver] = preCost + cost
                    queue.put([res[ver], ver])
        return res