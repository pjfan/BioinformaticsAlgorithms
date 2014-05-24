def findPalindromes(sequence, length):
	PalindromeDict = dict()
	for i, x in enumerate(sequence):
		if (i + length) > len(sequence):
			break
		if isPalindrome(sequence[i:i+length]) == True:
			PalindromeDict[i+1] = length
			#i+1 is used for the key because DNA sequences are indexed
			#starting at 1 while Python is indexed starting at 0.
		else: 
			continue
	return PalindromeDict
	
def isPalindrome(sequence):
	"""
	Input: A DNA sequence as a String or other iterable type.
	Ouput: A boolean indicating whether or not the sequence is a palindrome.
	"""

	if (len(sequence) % 2) != 0:
		return False
	if sequence == reverseComplement(sequence):
		return True
	else:
		return False

def reverseComplement(sequence):
	"""
	Input: a DNA sequence as a String or other iterable type.
	Ouput: the reverse complement of the sequence as a String.
	"""
	empt = ""
	for nuc in sequence:
		if nuc == "A":
			empt += "T"
		if nuc == "T":
			empt += "A"
		if nuc == "C":
			empt += "G"
		if nuc == "G":
			empt += "C"

	return empt[::-1]

