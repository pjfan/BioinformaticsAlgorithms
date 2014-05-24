"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""
def HammDist(Sequence1, Sequence2):
    HammingD = 0
    for i, x in enumerate(Sequence1):
        if x != Sequence2[i]:
            HammingD += 1
    return HammingD
        

