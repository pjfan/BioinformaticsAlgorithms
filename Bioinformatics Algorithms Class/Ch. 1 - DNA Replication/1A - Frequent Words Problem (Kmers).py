def FreqKmer(Text, k):
    """Frequent Words Problem: Find the most frequent k-mers in a string.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
    """
    KmerDic = dict()
    for i, x in enumerate(Text):
        Kmer = Text[i:i+int(k)]
        if i+int(k) > len(Text):
            break
        if Kmer not in KmerDic:
            KmerDic[Kmer] = 1
        else:
            KmerDic[Kmer] += 1
    KmerKeys = KmerDic.keys()
    KmerValues = [KmerDic[x] for x in KmerKeys]
    FreqKmerCount = KmerValues.count(max(KmerValues))
    MostFrequentKmers = []
    for x in xrange(FreqKmerCount):
        Kmer = KmerKeys[KmerValues.index(max(KmerValues))]
        KmerValues.pop(KmerValues.index(max(KmerValues)))
        KmerKeys.pop(KmerValues.index(max(KmerValues)))
        MostFrequentKmers.append(Kmer)
    return MostFrequentKmers
    
