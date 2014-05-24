import copy
import numpy as np
def commaput(string):
    List1 = list(string)
    List2 = copy.deepcopy(List1)
    empt = ''
    for i, x in enumerate(List1):
        if x == ' ':
            List2[i] = ','
    for x in List2:
        empt += x
    return empt


def convolution(list1):
    list1 = sorted(list1)
    list2 = copy.deepcopy(list1)
    solutions = []
    for i, x in enumerate(list1):
        for y in list2:
            solutions.append(x-y)
    crit = np.array(solutions) > 0
    solutions = np.array(solutions)[crit] 
    return solutions

            
