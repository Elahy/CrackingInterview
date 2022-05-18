def alternatingCharacters(s):

    delcount, low, hi = 0, 0, 1
    
    while(hi<len(s)):
        if s[low] == s[hi]:
            delcount += 1
            low = hi
            hi += 1
        else:
            low += 1
            hi += 1
            
    return delcount