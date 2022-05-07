class Solution:
    def print2largest(self,arr, n):
	    if n < 2: return arr[0]
        largest, seclar = arr[0],-1
	    
	    for i in arr:
	        if i > largest:
	            seclar = largest
                largest = i
	        if i < largest and i > seclar:
	            seclar = i
	            
	    return seclar