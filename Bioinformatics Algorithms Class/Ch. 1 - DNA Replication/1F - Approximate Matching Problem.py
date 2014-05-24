
def CheckMatch(Pattern, TextFrag):
    """
    Input: Two strings, Pattern and TextFrag.
    Output: The number of mismatches between the two strings.
    """
    mismatchcount = 0
    for i, x in enumerate(TextFrag):
        if x != Pattern[i]:
            mismatchcount += 1
    return mismatchcount

def PatMatch(Pattern, Text, d):
    """
    Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
     Input: Two strings Pattern and Text along with an integer d.
     Output: All positions where Pattern appears in Text with at most d mismatches.
    """
    substrlength = len(Pattern)
    substrlocation = []
    for i, x in enumerate(Text):
        if i+substrlength > len(Text):
            break
        mismatch = CheckMatch(Pattern, Text[i:(i+substrlength)])
        if mismatch <= d:
            substrlocation.append(i)
    return substrlocation


#for x in substrlocation:
#   print str(x)
