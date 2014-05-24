#FreqKmer function was modified/taken from Problem 1A.
def FreqKmer(Text, k):
    """
    Input: A string (Text) and a k-mer length (k).
    Output: A dictionary containing with keys corresponding to each Kmer
    present in the string Text and values equal to the frequency of that
    particular Kmer key in Text.
    """
    KmerDic = dict()
    for i, x in enumerate(Text):
        Kmer = Text[i:i+int(k)]
        if i+int(k) > len(Text):
            break
        elif Kmer not in KmerDic:
            KmerDic[Kmer] = 1
        else:
            KmerDic[Kmer] += 1
    return KmerDic

def ClumpFind(Genome, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    ClumpSeq = []
    ClumpSeqFinal = {}
    for i, x in enumerate(Genome):
        window = Genome[i:i+L]
        KmerDic = FreqKmer(window, k)
        #Two lists are created, one with KmerDic Keys and the other with the values.
        KmerDicKeys = KmerDic.keys()
        KmerDicValues = [KmerDic[x] for x in KmerDicKeys]
        for i, z in enumerate(KmerDicValues):
            if z >= t:
                ClumpSeq.append(KmerDicKeys[i])
    #This last for loop (shown below) is used to remove repeats.
    for x in ClumpSeq:
        ClumpSeqFinal[x] = 1
    return ClumpSeqFinal.keys()
                
