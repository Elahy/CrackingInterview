def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    
    ap = 0
    bp = 0
    cp = 0
    
    res = 0
    
    while bp < len(b):
        while ap < len(a) and a[ap] <= b[bp]:
            ap += 1
        
        while cp < len(c) and c[cp] <= b[bp]:
            cp += 1
        
        res += ap * cp
        bp += 1
    
    return res
    