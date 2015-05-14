import requests 
import bs4
import re

def find_nglycosyl_motif(uniprotID):
	"""This function retrieves the sequence for a given protein by scraping it from the protein's uniprot webpage 
	and then prints out any positions at which the N-glycosylation motif occurs in the sequence."""
	#requests is used to get the raw webpage.
	#BeautifulSoup is used to find the sequence, remove spaces, and remove digits.
	uniprot = requests.get('http://www.uniprot.org/uniprot/' + uniprotID)	
	seq = bs4.BeautifulSoup(uniprot.text).find('pre').text.replace(" ","")
	seq = ''.join([aa for aa in seq if not aa.isdigit()])
	#The re module is used to create an regular expression for the N-glycosylation motif.
	regex = re.compile('(?=N[^P][ST][^P])')
	pos = regex.finditer(seq)
	#The for loop below prints the positions in the protein where the N-glycosylation motif appears
	#The +1 is added because protein seqs start counting at 1 not 0.
	#The try catch statement is used to catch cases where the N-glycosylation motif isn't found in the protein seq.
	try:
		first_pos = pos.next().start() + 1
		print uniprotID
		print first_pos
		for x in pos:
			print x.start() + 1
	except Exception, StopIteration:
		return None

#The lines below open the rosalind file and use the above function to search for
#N-glycosylation motifs.
rosalind = open('rosalind_mprt.txt', 'r')

for uniprotID in rosalind:
	find_nglycosyl_motif(uniprotID.strip())
		
