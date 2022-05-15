def whatFlavors(cost, money):
    # Write your code here
    hashmap = {}
    
    for i in range(len(cost)):
        if money-cost[i] in hashmap:
            print(hashmap[money-cost[i]]+1, i+1)
            break
        else:
            hashmap[cost[i]] = i
