from P1FuncSuite import min_skew


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1e =open('rosalind_1e.txt','r')


genome = remove_spec(rosalind_1e.readline())


for skew in min_skew(genome):
   print skew

