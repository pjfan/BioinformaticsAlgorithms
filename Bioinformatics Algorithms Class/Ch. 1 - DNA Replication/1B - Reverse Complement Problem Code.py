def RevComp(inputDNA):
    """Reverse Complement Problem: Reverse complement a nucleotide pattern.
     Input: A DNA string inputDNA.
     Output: outputDNA, the reverse complement of inputDNA.
    """
    inputDNA = list(inputDNA)
    outputDNA = ''
    for base in inputDNA:
        if base == 'T':
            outputDNA += 'A'
        if base == 'G':
            outputDNA += 'C'
        if base == 'A':
            outputDNA += 'T'
        if base == 'C':
            outputDNA += 'G'
    outputDNA = outputDNA[::-1]
    return outputDNA
