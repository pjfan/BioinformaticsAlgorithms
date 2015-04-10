"""
Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

#hint: Draw out the 5 months, 3 offspring case on paper. The number of rabbits
#in a given month = rabbits in previous month + 3*rabbits from 2 months ago.
#Base cases set to 1 and 2 instead of 0 and 1 because setting to 0 and 1 has the
#effect of adding on an extra month.

def rabbit(n,k):
    """
    recursive function to solve rabbits and reccurence relations problem.

    n = number of months as an integer
    k = number of offspring from each mating as an integer.
    """
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return rabbit(n-1,k) + k*rabbit(n-2,k)


for line in open('rosalind_fib.txt', 'r'):
    nk = line.split()

print rabbit(int(nk[0]), int(nk[1]))