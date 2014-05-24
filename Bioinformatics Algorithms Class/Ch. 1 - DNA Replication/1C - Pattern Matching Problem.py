def PatMatch(Pattern, Text):
    """
    Pattern Matching Problem: Find all occurrences of a pattern in a string.
     Input: Two strings, Pattern and Text.
     Output: All starting positions where Pattern appears as a substring of Text.
    """
    substrlength = len(Pattern)
    substrlocation = []
    for i, x in enumerate(Text):
        if x == Pattern[0]:
            if i+substrlength > len(Text):
                break
            elif Text[i:(i+substrlength)] == Pattern:
                substrlocation.append(i)
    return substrlocation



#for x in substrlocation:
#   print str(x)
