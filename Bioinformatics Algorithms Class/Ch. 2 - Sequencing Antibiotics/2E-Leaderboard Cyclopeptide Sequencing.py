# Could have used sets (data type) for the comparisons... instead of np.any/np.all
#Also knowing about list comprehensions and the map(), filter(), and reduce() tools
#would have been helpful....
import itertools
import copy
import math
import numpy as np


def Cyclosplit(CycPeptide):
    frags = []
    PepLen = len(CycPeptide)
    FragLen = 0
    empt = ''
    for x in xrange(PepLen):
        FragLen+=1
        #The if conditional below was added in order to prevent repetion of the
        #full peptide's mass in the theoretical spectrum (causes a wrong answer.)
        if FragLen == PepLen:
            frags.append(CycPeptide)
            break
        for i, x in enumerate(CycPeptide):
            if (i+FragLen) > PepLen:
                diff = (i+FragLen)-PepLen
                empt += CycPeptide[i:PepLen]
                empt += CycPeptide[0:diff]
                frags.append(empt)
                empt=''
            else:
                frags.append(CycPeptide[i:i+FragLen])
    return frags


def LinCyclosplit(CycPeptide):
    frags = []
    PepLen = len(CycPeptide)
    FragLen = 0
    empt = ''
    for x in xrange(PepLen):
        FragLen+=1
        #The if conditional below was added in order to prevent repetion of the
        #full peptide's mass in the theoretical spectrum (causes a wrong answer.)
        if FragLen == PepLen:
            frags.append(CycPeptide)
            break
        for i, x in enumerate(CycPeptide):
            if (i+FragLen) > PepLen:
                break
            else:
                frags.append(CycPeptide[i:i+FragLen])
    return frags


def WeighIn(Peptide):
    Mass = 0
    for x in Peptide:
        if x == 'G':
            Mass += 57
        if x == 'A':
            Mass += 71
        if x == 'S':
            Mass += 87
        if x == 'P':
            Mass += 97
        if x == 'V':
            Mass += 99
        if x == 'T':
            Mass += 101
        if x == 'C':
            Mass += 103
        if x == 'I' or x == 'L':
            Mass += 113
        if x == 'N':
            Mass += 114
        if x == 'D':
            Mass += 115
        if x == 'K' or x == 'Q':
            Mass += 128
        if x == 'E':
            Mass += 129
        if x == 'M':
            Mass += 131
        if x == 'H':
            Mass += 137
        if x == 'F':
            Mass += 147
        if x == 'R':
            Mass += 156
        if x == 'Y':
            Mass += 163
        if x == 'W':
            Mass += 186
    return Mass

def ArrayToString(Array):
    empt = ''
    for x in Array:
        empt += str(x)
    return empt

def Linspectrum(Peptide):
    frags = LinCyclosplit(Peptide)
    #A dictionary was originally used to remove repeats but the answer
    #was counted as wrong when repeats were repeated. So a sorted list was
    #used instead. A mass of 0 must also be present in the theoretical spectrum
    #so it was included in the MassList.
    MassList = [0]
    for IndeFrag in frags:
        MassList.append(WeighIn(IndeFrag))
    return sorted(MassList)

def Cyclospectrum(Peptide):
    frags = Cyclosplit(Peptide)
    #A dictionary was originally used to remove repeats but the answer
    #was counted as wrong when repeats were repeated. So a sorted list was
    #used instead. A mass of 0 must also be present in the theoretical spectrum
    #so it was included in the MassList.
    MassList = [0]
    for IndeFrag in frags:
        MassList.append(WeighIn(IndeFrag))
    return sorted(MassList)


def Expand(List):
    AAList = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I','N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    List = itertools.product(List, AAList)
    Result = []
    for x in List:
        Result.append(ArrayToString(x))
    return Result

def Score(peptide, spectrum):
    ExpSpec = Linspectrum(peptide)
    score = 0
    ExpDict = dict()
    for x in ExpSpec:
        ExpDict[x] = 0
    for x in ExpSpec: #ExpDict:
        if np.any(x in spectrum):
            score +=1
            #spectrum = np.array(list(spectrum).remove(x))
    return score

def Cut(Leaderboard, PepDict, spectrum, N):
    #print len(PepDict)
    if len(PepDict) < N:
        threshold = sorted(PepDict.values())[0]
    else:
        threshold = sorted(PepDict.values())[-N]
    #print threshold
    for peptide in PepDict.keys():
        if PepDict[peptide] < threshold:
            Leaderboard.remove(peptide)            
    return Leaderboard
    
    
def commaput(string):
    List1 = list(string)
    List2 = copy.deepcopy(List1)
    empt = ''
    for i, x in enumerate(List1):
        if x == ' ':
            List2[i] = ','
    for x in List2:
        empt += x
    return empt

def LeaderboardCPSequencing(N, spectrum):
    spectrum = np.array(spectrum)
    ParentMass = spectrum[-1]
    AAList = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I','N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W'] 
    LeaderBoard = ['']
    LeaderPeptide = ''
    while LeaderBoard:
        LeaderBoard = Expand(LeaderBoard)
        PepDict = {}
        SecondBoard = copy.deepcopy(LeaderBoard)
        print len(LeaderBoard)
        for peptide in LeaderBoard:
            score = Score(peptide, spectrum)
            BigMass = Linspectrum(peptide)[-1]
            PepDict[peptide] = score
            if BigMass == ParentMass:
                #print peptide
                if score > Score(LeaderPeptide, spectrum):
                    #print 'HAHA'
                    LeaderPeptide = peptide
            elif BigMass > ParentMass:
                del PepDict[peptide]
                SecondBoard.remove(peptide)
        if not PepDict:
            break
        LeaderBoard = Cut(SecondBoard, PepDict, spectrum, N)
        #print LeaderPeptide
    return LeaderPeptide

def write2file(AnsArray):
    f = open('2D Theoretical Spectrum.txt', 'w')
    for x in AnsArray:
        for y in x:
            f.write(str(WeighIn(y)) + '-')
        f.write('\n')
    f.close()

#Not sure if cyclospectrum works for all datasets, worked for sample input/output
#but linspectrum has worked for all of them
#strategy - Use CyclopeptideSequencing to find the answer then use,
#write2file to convert it into numbers and write it to a text file with dashes.


