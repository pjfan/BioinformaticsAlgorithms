import copy

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
    

def CountMisMatch(Pattern, Text):
    count = 0
    for i, x in enumerate(Text):
        if x != Pattern[i]:
            count += 1
    return count

def GenerateMutant(kmer):
    Mutants = []
    AnswersDict = dict()
    for x in kmer:
        ListMer = list(x)
        for q, nuc in enumerate(ListMer):
            AMod = copy.deepcopy(ListMer)
            TMod = copy.deepcopy(ListMer)
            GMod = copy.deepcopy(ListMer)
            CMod = copy.deepcopy(ListMer)
            AMod[q] = 'A'
            Mutants.append(AMod)
            TMod[q] = 'T'
            Mutants.append(TMod)
            CMod[q] = 'C'
            Mutants.append(CMod)
            GMod[q] = 'G'
            Mutants.append(GMod)
    for nucstr in Mutants:
        Blankstr = ''
        for nuc in nucstr:
            Blankstr = Blankstr + nuc
        AnswersDict[Blankstr] = 0
    return AnswersDict.keys()
        
        
                
        
def MotEnum(DNAList, k, d):
    AllMutants = dict()
    Answers = []
    for seq in DNAList:
        for i, nuc in enumerate(seq):
            if (i+int(k)) > len(seq):
                break
            kmer = [seq[i:(i+int(k))]]
            for x in xrange(d):
                kmer = GenerateMutant(kmer)
            for x in kmer:
                AllMutants[x] = 0
    for mut in AllMutants.keys():
        NumAppear = 0
        for seq in DNAList:
            for i, nuc in enumerate(seq):
                if (i+int(k)) > len(seq):
                    break
                elif CountMisMatch(mut, seq[i:(i+int(k))]) <= d:
                    NumAppear += 1
                    break
        if NumAppear == len(DNAList):
            Answers.append(mut)
    return Answers
            
            
            
        
