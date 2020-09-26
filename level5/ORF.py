import common

fasta_dict = common.fasta_parser('ORF.txt')
sequence = fasta_dict[list(fasta_dict.keys())[0]]
forward_orf = [common.translate_dna(orf) for orf in common.find_orf_dna(sequence)]
reverse_orf = [common.translate_dna(orf) for orf in common.find_orf_dna(common.reverse_comp(sequence))]

print(forward_orf)
print(reverse_orf)

with open('ORF_result.txt', 'w') as f:
    [print(orf, file=f) for orf in set(forward_orf)|set(reverse_orf)]