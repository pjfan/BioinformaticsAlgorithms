"""
Given: An RNA string s corresponding to a strand of mRNA
(of length at most 10 kbp).

Return: The protein string encoded by s.
"""

def U_translate(codon):
    if codon[0:2] == 'UC':
        return 'S'
    if codon[0:2] == 'UA':
        if codon[2] == 'C':
            return 'Y'
        if codon[2] == 'U':
            return 'Y'
        else:
            return 'stop'
    if codon[0:2] == 'UG':
        if codon[2] == 'A':
            return 'stop'
        if codon[2] == 'G':
            return 'W'
        else:
            return 'C'
    if codon[0:2] == 'UU':
        if codon[2] == 'C':
            return 'F'
        if codon[2] == 'U':
            return 'F'
        else:
            return 'L'
        
def C_translate(codon):
    if codon[0:2] == 'CC':
        return 'P'
    if codon[0:2] == 'CA':
        if codon[2] == 'A':
            return 'Q'
        if codon[2] == 'G':
            return 'Q'
        else:
            return 'H'
    if codon[0:2] == 'CG':
        return 'R'
    if codon[0:2] == 'CU':
        return 'L'

def G_translate(codon):
    if codon[0:2] == 'GC':
        return 'A'
    if codon[0:2] == 'GA':
        if codon[2] == 'C':
            return 'D'
        if codon[2] == 'U':
            return 'D'
        else:
            return 'E'
    if codon[0:2] == 'GG':
        return 'G'
    if codon[0:2] == 'GU':
        return 'V'

def A_translate(codon):
    if codon[0:2] == 'AC':
        return 'T'
    if codon[0:2] == 'AA':
        if codon[2] == 'C':
            return 'N'
        if codon[2] == 'U':
            return 'N'
        else:
            return 'K'
    if codon[0:2] == 'AG':
        if codon[2] == 'A':
            return 'R'
        if codon[2] == 'G':
            return 'R'
        else:
            return 'S'
    if codon[0:2] == 'AU':
        if codon[2] == 'G':
            return 'M'
        else:
            return 'I'
        
def Translator(RNA_seq):
    """Input: RNA sequence Output: Protein sequence"""
    codon_dividers = xrange(0,len(RNA_seq),3)  
    RNA_codon_list = []
    for index in codon_dividers:
        RNA_codon_list.append(RNA_seq[index:(index+3)])
    product = ''

    for codon in RNA_codon_list:
        if codon[0] == 'A':
            product += A_translate(codon)
        if codon[0] == 'U':
            product += U_translate(codon)
        if codon[0] == 'G':
            product += G_translate(codon)
        if codon[0] == 'C':
            product += C_translate(codon)
    return product


