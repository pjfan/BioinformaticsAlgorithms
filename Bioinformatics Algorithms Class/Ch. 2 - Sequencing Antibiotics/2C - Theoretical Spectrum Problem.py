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

def Cyclospectrum(Peptide):
    frags = Cyclosplit(Peptide)
    #MassDict = dict()
    #MassDict[0] = 1
    #A dictionary was originally used to remove repeats but the answer
    #was counted as wrong when repeats were repeated. So a sorted list was
    #used instead. A mass of 0 must also be present in the theoretical spectrum
    #so it was included in the MassList.
    MassList = [0]
    for IndeFrag in frags:
        #MassDict[WeighIn(IndeFrag)] = 1
        MassList.append(WeighIn(IndeFrag))
    return sorted(MassList)
    
        
            
        
