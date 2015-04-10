from P1FuncSuite import freq_words


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1a =open('rosalind_1a.txt','r')


text = remove_spec(rosalind_1a.readline())
k = remove_spec(rosalind_1a.readline())

for word in freq_words(text,k):
   print word


