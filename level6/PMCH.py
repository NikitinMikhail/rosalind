import common
import math
'''
Assuming we have the same amount of occurences of A-U and G-C, all possible perfect matches is simply (AU)!*(GC)!
! - cause of number of permutations of size AU from AU list
* - cause of independent states of this pairs
'''

fasta_dict = common.fasta_parser('PMCH.txt')
sequence = fasta_dict[list(fasta_dict.keys())[0]]

AU = 0
GC = 0
AU, GC = (sequence.count(item) for item in ('A', 'G'))

matchings = math.factorial(AU) * math.factorial(GC)
print(matchings)
