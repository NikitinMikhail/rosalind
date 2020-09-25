import common
import numpy as np

fasta_dict = common.fasta_parser('CONS.txt')
letter_dict = dict()
base_list = ['A', 'C', 'G', 'T']
for base in base_list:
    letter_dict[base] = [0] * len(fasta_dict[list(fasta_dict.keys())[0]])

for key in fasta_dict.keys():
    count = 0
    for letter in fasta_dict[key]:
        letter_dict[letter][count] += 1
        count += 1

cons_seq = ''
counter = 0
for _ in range(len(fasta_dict[list(fasta_dict.keys())[0]])):
    value_list = [letter_dict[base][counter] for base in letter_dict.keys()]
    cons_seq += base_list[np.argmax(value_list)]
    counter += 1

print(cons_seq)
with open('CONS_result.txt', 'w') as f:
    print(cons_seq, file=f)
    for key in letter_dict.keys():
        print('{}: {}'.format(key, ' '.join(map(str, [item for item in letter_dict[key]]))), file=f)

