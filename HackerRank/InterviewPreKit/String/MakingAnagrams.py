def makeAnagram(a, b):
    # Write your code here
    hashmap = {}
    count = 0
    for letter in a:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    for letter in b:
        if letter in hashmap:
            count += 2
            if hashmap[letter] == 1:
                hashmap.pop(letter)
            else:
                hashmap[letter] -= 1
    return (len(a)+len(b))-count