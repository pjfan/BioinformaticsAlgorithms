def U_translate(codon):
    """
    Input: A 3 nucleotide long codon string beginning with U.
    Output: An amino acid.
    """
    if codon[0:2] == 'UC':
        return 'S'
    if codon[0:2] == 'UA':
        if codon[2] == 'C':
            return 'Y'
        if codon[2] == 'U':
            return 'Y'
        else:
            pass
            return 'stop'
    if codon[0:2] == 'UG':
        if codon[2] == 'A':
            return ''
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
    """
    Input: A 3 nucleotide long codon string beginning with C.
    Output: An amino acid.
    """
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
    """
    Input: A 3 nucleotide long codon string beginning with G.
    Output: An amino acid.
    """
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
    """
    Input: A 3 nucleotide long codon string beginning with A.
    Output: An amino acid.
    """
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


def CodonDiv(RNA):
    """
    Input: A string representing a sequence of RNA.
    Output: A list containing strings which represent the codons present in the
    original RNA string. 
    """
    CodonDivider = xrange(0, len(RNA), 3)
    Codons = []
    for x in CodonDivider:
        Codons.append(RNA[x:(x+3)])
    return Codons
  
def Translator(RNAseq):
    """
    Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string RNAseq.
     Output: The translation of RNAseq into an amino acid string Peptide.
     Notes: Don't return stop codon.
    """
    RNAseq = CodonDiv(RNAseq)    
    print RNAseq
    Peptide = ''
    for x in RNAseq:
        if x[0] == 'A':
            Peptide += (A_translate(x))
        if x[0] == 'U':
            Peptide += (U_translate(x))
        if x[0] == 'G':
            Peptide += (G_translate(x))
        if x[0] == 'C':
            Peptide += (C_translate(x))
    return Peptide

