def findMergeNode(head1, head2):
    dum1 = head1
    dum2 = head2
    hdict = {}
    while(dum1):
        hdict[dum1] = dum1.data
        dum1= dum1.next
    while(dum2):
        if dum2 in hdict:
            return dum2.data
        else:
            dum2 = dum2.next
            
    return None 