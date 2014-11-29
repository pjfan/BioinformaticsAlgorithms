from P1FuncSuite import rev_comp


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1b =open('rosalind_1b.txt','r')


pattern = remove_spec(rosalind_1b.readline())

print rev_comp(pattern)

