import numpy as np

#Note: To change from Greedy motif search to Greedy motif search with pseudocounts
#simply change Acount, Ccount, Gcount, and Tcount from 0 to a very small number E
#Ex.(0.00000001)
#The way I implemented pseudocounts is not the same as the way the authors
#implemented pseudocounts but it still works. The basic idea is the same though.

def Count(seq):
    Acount = 0.00000001
    Ccount = 0.00000001
    Gcount = 0.00000001
    Tcount = 0.00000001
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

def Profile(MotifArray,k):
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
    return np.array(BestKmer)


def Score(MotifArray,k):
    score = 0
    for x in xrange(k):
        score += (len(MotifArray) - Count(MotifArray[:,x]).max())
    return score

def GreedSearch(Dna, k, t):
    DnaList = [list(x) for x in Dna]
    DnaArray = np.array(DnaList[0])
    for x in DnaList[1:t]:
        DnaArray = np.vstack((DnaArray,x))
    BestMotifs = np.array(DnaArray[0][0:k])
    for seq in DnaArray[1:t]:
        BestMotifs = np.vstack((BestMotifs,seq[0:k]))
    BestScore = Score(BestMotifs,k)
    for i in xrange(len(DnaArray[0])-k+1):
        Motif = DnaArray[0][i:(i+k)]
        for q in xrange((t-1)):
            q = q + 1
            #print Motif
            #print ProfileMProb(Profile(Motif,k),k,DnaArray[q])
            Motif = np.vstack((Motif,ProfileMProb(Profile(Motif,k),k,DnaArray[q])))
        if Score(Motif,k) < BestScore:
            BestMotifs = Motif
            BestScore = Score(Motif, k)
    return BestMotifs
