"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

"""

#The Translator Code below was taken from the solution to the "Translating RNA to protein problem"##################################
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

########################################################################

########The function below is from the Transcribe DNA to RNA problem######
def TranscribeDNAtoRNA(sequence):
    output_RNA = ''
    for nuc in sequence:
        if nuc == 'T':
            output_RNA += 'U'
        else:
            output_RNA += nuc
    return output_RNA
#############################################################################



class FASTA_reader(object):
    """This class reads FASTA files."""
    def __init__(self, file_name):
        self.first_entry = True
        self.FASTAfile = open(file_name, 'r')
        self.FASTA_dict = dict()

    def process_file(self):
        #This part of the code reads from the FASTA file and adds strands to the GC_content.
        #The remove_spec method is once again used to remove any special characters or spaces.
        blankstr = ""
        FASTA_key_name = ""
        for line in self.FASTAfile:
            if line[0] == '>':
                if self.first_entry == True:
                    self.first_entry = False
                    FASTA_key_name = line
                else:
                    blankstr = self.remove_spec(blankstr)
                    self.FASTA_dict[FASTA_key_name] = blankstr
                    blankstr = ""
                    FASTA_key_name = line
            else:
                blankstr += line
        blankstr = self.remove_spec(blankstr)
        self.FASTA_dict[FASTA_key_name] = blankstr
        
    def remove_spec(self, strand):
        for x in strand:
            if x != 'A' and x != 'G' and x != 'C' and x != 'T':
                strand = strand.replace(x, "")
        return strand

    def getFASTA_dict(self):
        return self.FASTA_dict

class RNAsplicer(object):
    def __init__(self,file_name):
        self.FASTA_reader = FASTA_reader(file_name)
        self.FASTA_reader.process_file()
        self.FASTA_dict = self.FASTA_reader.getFASTA_dict()
        FASTA_file = open(file_name, 'r')
        BreakCounter = 0
        self.Unspliced_seq = ""
        for line in FASTA_file:
            if line[0] == ">":
                if BreakCounter == 1:
                    break
                else:
                    BreakCounter += 1
            else:
                self.Unspliced_seq += line
        FASTA_file.close()
        self.Unspliced_seq = self.FASTA_reader.remove_spec(self.Unspliced_seq)
        self.spliced_seq = self.Unspliced_seq
        self.spliceCheck = False
    def RNASplice(self):
        for key in self.FASTA_dict.keys():
            self.spliced_seq = self.spliced_seq.replace(self.FASTA_dict[key], "")
        self.spliceCheck = True
    def ToProtein(self):
        if self.spliceCheck == False:
            return 'Please run RNASplice() first'
        RNA = TranscribeDNAtoRNA(self.spliced_seq)
        return Translator(RNA)
    def __str__(self):
        if self.spliceCheck == False:
            return "Unspliced Sequence: " + self.Unspliced_seq
        else:
            return "Spliced Sequence: " + self.spliced_seq + " Protein Sequence: " + self.ToProtein()