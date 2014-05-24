import numpy as np
from random import randint

def Count(seq):
    Acount = 0
    Ccount = 0
    Gcount = 0
    Tcount = 0
    for x in seq:
        if x == 'A':
            Acount += 1
        if x == 'C':
            Ccount += 1
        if x == 'G':
            Gcount += 1
        if x == 'T':
            Tcount += 1
    counts = np.array([Acount, Ccount, Gcount, Tcount])
    return counts

#Profile takes an array of kmer motifs as input and generates a profile for these
#kmers. A row of zeroes is stacked on top of the motif array using np.vstack
#because otherwise the code screws up if there's only a single kmer in the motif array
#In the for loop, the count function is applied to each column of the kmer
#motif array in order to count the number of A's, C's, G's, and T's in the column.
#This count is divided by the number of kmers present (minus one to account for
#the row of zeroes) in the motif array to determine the relative proportions.

def ProfileGen(MotifArray,k):
    profile = []
    MotifArray = np.vstack((np.zeros(k),MotifArray))
    for x in xrange(k):
        profile.append(Count(MotifArray[:,x])/float(len(MotifArray)-1))
    return np.array(profile)

#the COLUMNS in the answer are ordered A, C, G, T

#takes a string of Dna, kmer length, and a profile as input and uses
#these to determine the profile most probable kmer in the string Dna.

def ProfileMProb(Profile, k, Text):
    BestProb = 0
    BestKmer = Text[0:k]
    for i in xrange(len(Text)-k+1):
        kmer = Text[i:(i+k)]
        Prob = 1
        for q, x in enumerate(kmer):
            if x == 'A':
                Prob = Prob*Profile[q,0]
            if x == 'C':
                Prob = Prob*Profile[q,1]
            if x == 'G':
                Prob = Prob*Profile[q,2]
            if x == 'T':
                Prob = Prob*Profile[q,3]
        if Prob > BestProb:
            BestKmer = kmer
            BestProb = Prob
    return np.array(list(BestKmer))

def MotifsFind(Profile, DnaArray, k):
    MotifArray = ProfileMProb(Profile, k, str(DnaArray[0]))
    for Text in DnaArray[1:]:
        MotifArray = np.vstack((MotifArray,ProfileMProb(Profile, k, str(Text))))
    return MotifArray

def Score(MotifArray,k):
    score = 0
    for x in xrange(k):
        score += (len(MotifArray) - Count(MotifArray[:,x]).max())
    return score

def RandomizedMotSearch(Dna,k,t):
    StartIndex = randint(1,(len(Dna[0])-k))
    BestMotifs = np.array(list((Dna[0][StartIndex:(StartIndex+k)])))
    for seq in Dna[1:]:
        StartIndex = randint(1,(len(seq)-k))
        BestMotifs = np.vstack((BestMotifs,np.array(list((seq[StartIndex:(StartIndex+k)])))))
    while True:
        Profile = ProfileGen(BestMotifs, k)
        Motifs = MotifsFind(Profile, Dna, k)
        if Score(Motifs,k) < Score(BestMotifs,k):
            BestMotifs = Motifs
        else:
            return BestMotifs

def ThousandRuns(Dna, k, t, Iterations):
    BestScore = k*t
    BestMotifs = []
    for x in xrange(Iterations):
        MotifArray = RandomizedMotSearch(Dna, k, t)
        if Score(MotifArray, k) < BestScore:
            BestMotifs = MotifArray
            BestScore = Score(MotifArray, k)
    return BestMotifs            

def ImportFil(Name):
    f = open(Name + '.txt', 'r+')
    SeqList = []
    SeqList2 = []
    for line in f:
        SeqList.append(line)
    SeqList = SeqList[1:]
    for seq in SeqList:
        SeqList2.append(seq[0:-2])
    f.close()
    return SeqList2
