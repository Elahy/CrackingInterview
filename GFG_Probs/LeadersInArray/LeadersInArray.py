class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        lead = [A[N-1]]
        hi = A[N-1]
        
        for i in range(N-2, -1, -1):
            if A[i] >= hi:
                lead.append(A[i])
                hi = A[i]
        start, end = 0, len(lead)-1
        
        while start < end:
            lead[start], lead[end] = lead[end], lead[start]
            start += 1
            end -= 1
            
        return lead