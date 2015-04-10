from P1FuncSuite import approx_patt_match


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1f =open('rosalind_1f.txt','r')


pattern = remove_spec(rosalind_1f.readline())
text = remove_spec(rosalind_1f.readline())
d = remove_spec(rosalind_1f.readline())

P1F_answers = open('P1F_answers.txt', 'w')

for pos in approx_patt_match(pattern, text, d):
    P1F_answers.write(str(pos)+'\n')   

