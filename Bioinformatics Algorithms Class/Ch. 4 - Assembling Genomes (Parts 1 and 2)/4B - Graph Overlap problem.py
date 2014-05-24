
datafile = open('dataset_52_7.txt', 'r+')
seqlist = []
for line in datafile:
    seqlist.append(line[0:-1])
datafile.close()

def Prefix(Pattern):
    """
    Input: A string Pattern of length k.
    Output: The first k-1 digits of Pattern.
    """
    return Pattern[0:(len(Pattern)-1)]

def Suffix(Pattern):
    """
    Input: A string Pattern of length k.
    Output: The last k-1 digits of Pattern.
    """
    return Pattern[-(len(Pattern)-1):len(Pattern)]

def Overlap(Patterns):
    """
    Input: A list of strings named Patterns of length k.
    Output: The overlap graph of all strings in the list Patterns.
    """
    Graph = []
    for seq in Patterns:
        for seq2 in Patterns:
            if seq == seq2:
                pass
            elif Suffix(seq) == Prefix(seq2):
                Graph.append(seq + ' -> ' + seq2)
    AnswerFile = open('4B Answers.txt', 'w+')
    for seq in sorted(Graph):
        AnswerFile.write(seq + '\n')
    AnswerFile.close()
        
        

        
