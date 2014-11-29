from P1FuncSuite import freq_words_mismatches_alt


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1g =open('rosalind_1g.txt','r')


text = remove_spec(rosalind_1g.readline())
kd = remove_spec(rosalind_1g.readline())

for word in freq_words_mismatches_alt(text, kd.split()[0], kd.split()[1]):
	print word
