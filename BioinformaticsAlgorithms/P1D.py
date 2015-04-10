from P1FuncSuite import clump_find


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1d =open('rosalind_1d.txt','r')


genome = remove_spec(rosalind_1d.readline())
klt = remove_spec(rosalind_1d.readline())

klt = klt.split()

for kmer in clump_find(genome, klt[0], klt[1], klt[2]):
   print kmer

