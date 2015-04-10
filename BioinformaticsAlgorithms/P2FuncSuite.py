

def translate(pattern):
	patt_length = len(pattern)
	codon_dict = {
	'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 
	'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
	'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
	'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
	'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
	'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
	'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
	'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
	'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
	'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
	'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
	'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
	'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
	'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
	'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
	'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L'
	}
	aa_code = []
	for i in xrange((patt_length/3)):
		aa_code.append(codon_dict[pattern[(i*3):((i*3)+3)]])
	return ''.join(aa_code)

#Two strategies for 2B first is to translate the protein code back into all possible RNA variations.
#Translate that into DNA and then search for the DNA code/it's complement in the sequence provided.

#Second strategy is to translate all of the DNA into RNA then AA code and then identify where the protein
#sequence shows up. Would have to translate both strands and all 3 reading frames.

def rev_dict():
	aa_dict = {'A': ['GCA', 'GCG', 'GCC', 'GCU'], 'C': ['UGU', 'UGC'], 'E': ['GAA', 'GAG'], 
	'D': ['GAC', 'GAU'], 'G': ['GGU', 'GGG', 'GGA', 'GGC'], 'F': ['UUU', 'UUC'], 
	'I': ['AUA', 'AUC', 'AUU'], 'H': ['CAC', 'CAU'], 'K': ['AAG', 'AAA'], 
	'*': ['UGA', 'UAA', 'UAG'], 'M': ['AUG'], 'L': ['CUU', 'CUG', 'CUA', 'CUC', 'UUG', 'UUA'], 
	'N': ['AAC', 'AAU'], 'Q': ['CAG', 'CAA'], 'P': ['CCC', 'CCA', 'CCU', 'CCG'], 
	'S': ['AGC', 'AGU', 'UCU', 'UCG', 'UCC', 'UCA'], 'R': ['AGG', 'AGA', 'CGA', 'CGC', 'CGG', 'CGU'], 'T': ['ACC', 'ACA', 'ACU', 'ACG'], 
	'W': ['UGG'], 'V': ['GUU', 'GUC', 'GUG', 'GUA'], 'Y': ['UAU', 'UAC']}
	return aa_dict

def rev_comp(pattern):
    #Generates the reverse complement of a string 'pattern'.
    pattern_rev = []
    for base in pattern:
        if base == 'A':
            pattern_rev.append('T')
        if base == 'C':
            pattern_rev.append('G')
        if base == 'T':
            pattern_rev.append('A')
        if base == 'G':
            pattern_rev.append('C')
    pattern_rev = pattern_rev[::-1]
    return ''.join(pattern_rev)

def transcribe(dna):
	rna = []
	for base in dna:
		if base == 'T':
			rna.append('U')
			continue
		rna.append(base)
	return ''.join(rna)

def prot_decode(text, peptide):
	text_length = len(text)
	pep_length = len(peptide)
	substrings = []
	for i in xrange(text_length-pep_length+1):
		if translate(transcribe(text[i:(i+(pep_length*3))])) == peptide:
			substrings.append(text[i:(i+(pep_length*3))])
	text = rev_comp(text)
	for i in xrange(text_length-pep_length+1):
		if translate(transcribe(text[i:(i+(pep_length*3))])) == peptide:
			substrings.append(rev_comp(text[i:(i+(pep_length*3))]))
	return substrings			

