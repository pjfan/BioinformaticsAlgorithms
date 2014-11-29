from P1FuncSuite import freq_words_mismatches_rev


def remove_spec(txt):
#Removes special characters from the imported strings
    for x in txt:
        if x=="\n":
            txt = txt.replace(x,"")
    return txt

rosalind_1h =open('rosalind_1h.txt','r')


text = remove_spec(rosalind_1h.readline())
kd = remove_spec(rosalind_1h.readline())

for word in freq_words_mismatches_rev(text, kd.split()[0], kd.split()[1]):
	print word
