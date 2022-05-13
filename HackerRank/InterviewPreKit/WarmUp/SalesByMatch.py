def sockMerchant(n, ar):
    # Write your code here
    socset = set()
    pair = 0
    for sock in ar:
        if sock in socset:
            pair += 1
            socset.remove(sock)
        else:
            socset.add(sock)
    return pair