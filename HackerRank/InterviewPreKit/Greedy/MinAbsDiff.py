def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    mindiff = abs(arr[0]-arr[1])
    for i in range(1,len(arr)-1):
            mindiff = min(mindiff, abs(arr[i]-arr[i+1]))    
    return mindiff