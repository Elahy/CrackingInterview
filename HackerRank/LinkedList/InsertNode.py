def insertNodeAtPosition(llist, data, position):
    # Write your code here
    dummy = llist
    for i in range(position-1):
        llist = llist.next
    newNode = SinglyLinkedListNode
    newNode.data = data
    if llist.next:
        newNode.next = llist.next
    else:
        newNode.next = None
    llist.next = newNode
    return dummyS