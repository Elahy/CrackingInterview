def minimumBribes(q,n):
    totalBribe = 0
    for i in range(n-1, -1, -1):
        if q[i] > i+3:
            totalBribe = -1
            break
        for j in range(max(q[i]-2, 0),i):
            if q[j] > q[i]:
                totalBribe += 1
   
    print("Too chaotic") if totalBribe == -1 else print(totalBribe)