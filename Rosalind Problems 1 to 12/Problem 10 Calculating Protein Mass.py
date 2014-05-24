"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""

def ProteinMassCalc(prot_seq):
    proteinMass = 0
    AAMWdict = {'A': 71.03711, 'C': 103.00919, 'E': 129.04259, 'D': 115.02694, 'G': 57.02146, 'F': 147.06841, 'I': 113.08406, 'H': 137.05891, 'K': 128.09496, 'M': 131.04049, 'L': 113.08406, 'N': 114.04293, 'Q': 128.05858, 'P': 97.05276, 'S': 87.03203, 'R': 156.10111, 'T': 101.04768, 'W': 186.07931, 'V': 99.06841, 'Y': 163.06333}
    for AA in prot_seq:
        proteinMass += AAMWdict[AA]
    return proteinMass
