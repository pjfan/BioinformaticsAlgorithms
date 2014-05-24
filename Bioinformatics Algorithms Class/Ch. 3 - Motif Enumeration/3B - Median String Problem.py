from itertools import product


def CountMisMatch(Pattern, motif):
    count = 0
    for i, nuc in enumerate(motif):
        if nuc != Pattern[i]:
            count += 1
    return count
    
def ArrayToString(Array):
    empt = ''
    for x in Array:
        empt += str(x)
    return empt

def GenAllKmers(SeqList, k):
    NucList = ['A', 'C', 'T', 'G']
    List = product(SeqList, NucList)
    Result = [ArrayToString(x) for x in List]
    return Result

def HamDist(kmer, Dna, k):
    LowestScore = k
    LowScoreList = []
    for motif in Dna:
        for i in xrange(len(motif)-k+1):
            Score = CountMisMatch(kmer,motif[i:i+k])
            if Score < LowestScore:
                LowestScore = Score
        LowScoreList.append(LowestScore)
        LowestScore = k
    ToteScore = sum(LowScoreList)
    return ToteScore
        
            
def MedString(Dna, k):
    AllKmers = ['']
    for x in xrange(k):
        AllKmers = GenAllKmers(AllKmers,k)
    BestKmer = AllKmers[0]
    for kmer in AllKmers:
        if HamDist(kmer, Dna, k) < HamDist(BestKmer, Dna, k):
            BestKmer = kmer
    return BestKmer
        
