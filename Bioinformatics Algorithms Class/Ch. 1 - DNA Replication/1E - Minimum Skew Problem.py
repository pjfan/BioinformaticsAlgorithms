import numpy as np

def Skew(Genome):
    """
    Input: A string (Genome).
    Output: A list representing the GC skew at each nucleotide in the Genome.
    """
    Results = []
    Gcount = 0
    Ccount = 0
    for i, x in enumerate(Genome):
        if x == 'G':
            SkewNumber = Gcount - Ccount
            Results.append(SkewNumber)
            Gcount = Gcount + 1
        elif x == 'C':
            SkewNumber = Gcount - Ccount
            Results.append(SkewNumber)
            Ccount = Ccount + 1
        else:
            SkewNumber = Gcount - Ccount
            Results.append(SkewNumber)
    Results.append(Gcount - Ccount)
    #above calculation is necessary so that the final skew calculation is
    #also incorporated in Results.
    return Results

#Didn't include the "prefix" function in the Stepic... Not really sure
#what the point of the prefix function was in the first palce.

def MinSkew(Genome):
    """
    Minimum Skew Problem: Find a position in a genome minimizing the skew.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skew(Genome) among all values of i (from 0 to |Genome|).
    """
    MinValues = []
    DataSkewSet = np.array(Skew(Genome))
    MinValue = np.argmin(DataSkewSet)
    for i, x in enumerate(DataSkewSet):
        if x <= DataSkewSet[MinValue]:
            MinValues.append(i)
    return MinValues
