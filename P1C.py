from P1FuncSuite import patt_match


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1c =open('rosalind_1c.txt','r')


pattern = remove_spec(rosalind_1c.readline())
genome = remove_spec(rosalind_1c.readline())

for index in patt_match(pattern,genome):
   print index

