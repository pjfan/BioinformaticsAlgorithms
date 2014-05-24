#FindAllKmers function is basically the FreqKmer function from problem 1A.

import copy

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

def Count(Pattern, Text, d):
    """
    Input: Two strings, Pattern and Text, and an integer, d, that represents the
    maximum number of allowable mismatches.
    Output: The number of times Pattern occurs in Text with d or fewer mismatches
    """
    substrlength = len(Pattern)
    PatCount = 0
    for i, x in enumerate(Text):
        if i+substrlength > len(Text):
            break
        mismatch = CheckMatch(Pattern, Text[i:(i+substrlength)])
        if mismatch <= d:
            PatCount += 1
    return PatCount


def GenerateMutant(FreqKmers):
    """
    Input: A list of strings, FreqKmers, which represent the most frequent kmers THAT APPEAR in a particular genome.
    Output: A list of strings which includes the original FreqKmers as well as all sequences that are only different by one mismatch.
    """
    AllVariants = []
    AllVariantStrings = []
    AllVariantDict = dict()
    for sequence in FreqKmers:
        Modsequence = list(sequence)
        #Each string is converted to a list because lists are mutable while strings are immutable.
        for ind, nuc in enumerate(Modsequence):
            AMod = copy.deepcopy(Modsequence)
            TMod = copy.deepcopy(Modsequence)
            GMod = copy.deepcopy(Modsequence)
            CMod = copy.deepcopy(Modsequence)
            AMod[ind] = 'A'
            AllVariants.append(AMod)
            TMod[ind] = 'T'
            AllVariants.append(TMod)
            CMod[ind] = 'C'
            AllVariants.append(CMod)
            GMod[ind] = 'G'
            AllVariants.append(GMod)
    #The for loop shown below converts all lists back into strings.
    for sequence in AllVariants:
        BlankStr = ''
        for nuc in sequence:
            BlankStr = BlankStr + nuc
        AllVariantStrings.append(BlankStr)
    #The for loop shown below removes repeats.
    for x in AllVariantStrings:
        AllVariantDict[x] = 1
    return AllVariantDict.keys()

def FindAllKmers(Text, k):
    """
    Input: A string, Text, and an integer k representing Kmer length.
    Output: A list of strings representing all kmers of length k that are present in Text.
    """
    KmerDic = dict()
    #A dictionary is used in order to prevent repeat Kmers from showing up.
    for i, x in enumerate(Text):
        if i+int(k) > len(Text):
            break
        KmerDic[Text[i:i+int(k)]] = 1
    return KmerDic.keys()

def SecondGuess(Text, k, d):
    """
    Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
    """
    TextKmers = FindAllKmers(Text, k)
    AllKmers = GenerateMutant(TextKmers)
    if d == 2:
        AllKmers = GenerateMutant(AllKmers)
    if d == 3:
        AllKmers = GenerateMutant(GenerateMutant(AllKmers))
    CurrentMaxCount = 0
    FreqKmers = []
    for Kmer in AllKmers:
        KmerCount = Count(Kmer, Text, d)
        if KmerCount < CurrentMaxCount:
            pass
        elif KmerCount > CurrentMaxCount:
            CurrentMaxCount = KmerCount
            FreqKmers = []
            FreqKmers.append(Kmer)
        else:
            FreqKmers.append(Kmer)
    return FreqKmers

#My first approach to this problem was incorrect because I assumed the
#real most frequent k-mer with mismatches was going to be a "mutant" of one of the
#most frequent k-mer with mismatches that actually appears in the genome
#(a mutant of something that could be found using the sliding window approach).
#However, this isn't necessarily true.
#In the example where 'AAAAA' was the most frequent 5-mer with one mismatch,
#the most frequent k-mer with 1 mismatch found using the sliding window approach
#was 'TTAAA'. If I had used GenerateMutant on 'TTAAA' just once it would have been impossible to get
#'AAAAA' as a possible answer. 'AAAAA' could be found by using GenerateMutant
#twice but this approach was shown to not work all that well with longer sequences.

#My Solution (similar to a Brute Force approach) - Generate every possible K-mer that appears in this sequence. (TextKmers)
#Find all K-mers that are d-mismatches away from the set of all K-mers by using the GenerateMutant function. (AllKmers)
#Then use Count on this set to find the most frequent K-mers with at most d-mismatches. (FreqKmers)


#for x in FinalMaximizers:
#   print str(x)
