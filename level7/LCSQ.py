import common

print
fasta_dict = common.fasta_parser('LCSQ.txt')
seq1, seq2 = (fasta_dict[key] for key in fasta_dict.keys())
print(seq1, seq2)