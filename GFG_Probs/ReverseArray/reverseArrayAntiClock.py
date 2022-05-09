import sys
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int,input().split()))
    
t = inp()
for i in range(t):
    n,d = inlt()
    d = d%n
    arr = inlt()
    
    def reverse(start, end):
        while(start<end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(0,d-1)
    reverse(d,n-1)
    reverse(0,n-1)
    for i in arr:
        print(i, end=' ')
    print("")