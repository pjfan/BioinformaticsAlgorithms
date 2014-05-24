
def Composition(k, Text):
    """
    Input: an interger k, and a string Text.
    Output: A list containing all the k-mer strings present in Text.
    """
    f = open('Answers4A.txt', 'w+')
    i = 0
    answers = []
    while i <= (len(Text)-k):
        answers.append(Text[i:(i+k)])
        i+= 1
    answers = sorted(answers)
    for x in answers:
        f.write(x + '\n')
    f.close()
    return 'Done!'




        
