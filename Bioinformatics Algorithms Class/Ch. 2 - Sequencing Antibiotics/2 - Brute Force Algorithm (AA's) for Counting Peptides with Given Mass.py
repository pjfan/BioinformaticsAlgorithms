#Note: The normal brute force algorithm is terribly inefficient SHOULD NEVER be
#used because it causes computer crashes when computing anything that requires more than 2 or 3 AA's in a peptide.

#11/15/2013 - Slightly modified brute force algorithm works better and can safely calculate masses ~600 in around 3 min. 30 seconds.

#AAList = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    

import itertools
import copy
import math
import numpy as np

def WeighIn(Peptide):
    Mass = 0
    for x in Peptide:
        if x == 'G':
            Mass += 57
        if x == 'A':
            Mass += 71
        if x == 'S':
            Mass += 87
        if x == 'P':
            Mass += 97
        if x == 'V':
            Mass += 99
        if x == 'T':
            Mass += 101
        if x == 'C':
            Mass += 103
        if x == 'I' or x == 'L':
            Mass += 113
        if x == 'N':
            Mass += 114
        if x == 'D':
            Mass += 115
        if x == 'K' or x == 'Q':
            Mass += 128
        if x == 'E':
            Mass += 129
        if x == 'M':
            Mass += 131
        if x == 'H':
            Mass += 137
        if x == 'F':
            Mass += 147
        if x == 'R':
            Mass += 156
        if x == 'Y':
            Mass += 163
        if x == 'W':
            Mass += 186
    return Mass

def ArrayToString(Array):
    empt = ''
    for x in Array:
        empt += str(x)
    return empt

def PepMass(m):
    PepMerLen = math.floor(m/50)
    PepMerMin = math.floor(m/186)
    AAList = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I','N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    #L and K were deleted from the amino acid list (I and L have the same molecular mass,
    #and K and Q have the same molecular mass), they increase the runtime
    #of the algorithm but do not add anything substantial to the answer
    #because for all intents in purposes a peptide with I's instead
    #of L's will produce the exact same mass spectrum and total mass
    #as a peptide with L's. (Same idea goes for K's and Q's) 
    Answers = []
    count = 0
    NewPepMers = copy.deepcopy(AAList)
    for x in xrange(int(PepMerLen-1)):
        #If a peptide has mass greater than m, it cannot be the correct answer,
        #If it's not the correct answer, if a peptide has a mass greater than m-57
        #(mass of the lightest peptide) it also cannot be the correct answer.
        CartProdTemp = itertools.product(NewPepMers, AAList)
        NewPepMers = []
        for y in CartProdTemp:
            if WeighIn(ArrayToString(y)) > (m):
                pass
            elif WeighIn(ArrayToString(y)) == m:
                #Answers.append(ArrayToString(y))
                count += 1
            elif WeighIn(ArrayToString(y)) > (m-57):
                pass
            else:
                NewPepMers.append(ArrayToString(y))
    return count #Answers 
        
def ResultPepMass(m):
    #answers = []
    count = 0
    for x in PepMass(m):
        if WeighIn(x) == m:
            #answers.append(x)
            count += 1
    return count #answers
