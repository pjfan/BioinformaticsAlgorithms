from P2FuncSuite import translate


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_2a =open('rosalind_2a.txt','r')


pattern = remove_spec(rosalind_2a.readline())

print translate(pattern)
