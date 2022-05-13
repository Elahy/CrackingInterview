def activityNotifications(expenditure, d):
    # Write your code here
    def findMedian():
        csum = 0
        med1 = None
        for val,freq in enumerate(counts):
            csum += freq
            if med1 == None and  csum >= d//2:
                med1 = val
            if csum >= d//2+1:
                med2 = val
                break
        median = med2
        if d%2==0:
            median = 0.5*(med1+med2)
        return median
    
    counts = [0]*201
    for val in expenditure[0:d]:
        counts[val] += 1
    notification = 0
    for i in range(d,len(expenditure)):
        if expenditure[i] >= findMedian()*2:
            notification += 1
        counts[expenditure[i-d]] -= 1
        counts[expenditure[i]] += 1
    return notification
        