"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def subStringLocator(s, t):
    """Returns all locations of t as a substring of s"""
    
    substrlen = len(t)
    substrloc = []

    for i, nuc in enumerate(s):
        if nuc == t[0]:
            if i+substrlen > len(s):
                break
            elif s[i:(i+substrlen)] == t:
                substrloc.append(i+1)

    #i+1 is appended instead of i because python counts from 0 while DNA
    #sequences count starting from 1.
    return substrloc


subs = open('rosalind_subs.txt', 'r')

s = subs.readline().rstrip('\n')
t = subs.readline().rstrip('\n')

for x in subStringLocator(s,t):
    print x