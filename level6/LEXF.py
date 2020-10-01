import common
import itertools

alphabet, n = common.multi_line_reader('LEXF.txt')
alphabet = alphabet.split()

kmers = sorted(list(itertools.product(alphabet, repeat=int(n))))

with open('LEXF_result.txt', 'w') as output_file:
    [print(''.join(elem), file=output_file) for elem in kmers]
