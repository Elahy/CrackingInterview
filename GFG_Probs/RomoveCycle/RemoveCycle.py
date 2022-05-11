class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        fast = slow = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                if slow == fast:
                    while fast.next != head:
                        fast = fast.next
                else:
                    while(slow.next != fast.next):
                        slow = slow.next 
                        fast = fast.next 
                fast.next = None
                break
                