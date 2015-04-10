from P2FuncSuite import prot_decode


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_2b =open('rosalind_2b.txt','r')


text = remove_spec(rosalind_2b.readline())
peptide = remove_spec(rosalind_2b.readline())

for seq in prot_decode(text, peptide):
	print seq
