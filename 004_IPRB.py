"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

#hint: Draw out the tree diagram. Three initial branches corresponding to genotype of first organism. Three branches off of EACH of these initial branches representing
#possible genotypes of second organism. Two branches off of EACH of these second branches representing two possible phenotypes (dominant or recessive) of offspring.



class ProbAllele(object):
    #k = number of homozygous dominant, m = number of heterozygotes, n = number of homozygous recessive
    def __init__(self, k, m, n):
        self.k = float(k)
        self.m = float(m)
        self.n = float(n)
        self.total = float(k+m+n)
    def prob_of_dom(self):
        OneLess = self.total - 1
        return 1 - ((self.n/self.total)*((self.n-1)/OneLess) + 0.5*(self.m/self.total)*(self.n/OneLess) + 0.5*(self.n/self.total)*(self.m/OneLess) + 0.25*(self.m/self.total)*((self.m-1)/OneLess))
    def __str__(self):
        return str(self.prob_of_dom())
    
rosalind_iprb = open('rosalind_iprb.txt', 'r')

for line in rosalind_iprb:
    kmn = line.split()
    print kmn

print ProbAllele(int(kmn[0]), int(kmn[1]), int(kmn[2]))