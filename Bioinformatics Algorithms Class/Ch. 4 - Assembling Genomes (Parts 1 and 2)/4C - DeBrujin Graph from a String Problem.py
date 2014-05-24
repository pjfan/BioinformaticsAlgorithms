
def Composition(k, Text):
    """
    Input: an interger k, and a string Text.
    Output: A list containing all the k-mer strings present in Text.
    """
    i = 0
    answers = []
    while i <= (len(Text)-k):
        answers.append(Text[i:(i+k)])
        i+= 1
    answers = sorted(answers)
    return answers

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

def DeBrujin(k, Text):
    """
    Input: An integer k, and a string Text.
    Output: The debrujin graph for all strings of length k in Text.
    """
    Graph = []
    Patterns = Composition((k-1), Text)
    for seq in Patterns:
        for seq2 in Patterns:
            if seq == seq2:
                pass
            elif Suffix(seq) == Prefix(seq2):
                Graph.append(seq + ' -> ' + seq2)
    GraphDict = dict()
    for x in Graph:
        GraphDict[x] = 0
    Graph = GraphDict.keys()
    DBGraph = []
    for seq in Graph:
        Temp = []
        Temp.append(seq)
        for i, seq2 in enumerate(Graph):
            if seq == seq2:
                pass
            elif seq[0:(k-1)] == seq2[0:(k-1)]:
                Temp.append(seq2)
                Graph.pop(i)
        if len(Temp) == 1:
            DBGraph.append(seq)
        else:
            JoinNode = Temp[0]
            for seq in Temp[1:]:
                JoinNode = JoinNode + ',' + seq[(len(seq2)-(k-1)):len(seq2)]
            DBGraph.append(JoinNode)
    AnswerFile = open('4C Answers.txt', 'w+')
    for seq in sorted(DBGraph):
        AnswerFile.write(seq + '\n')
    AnswerFile.close()
        
        

        
