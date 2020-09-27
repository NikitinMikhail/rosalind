import common

fasta_dict = common.fasta_parser('TRAN.txt')

seq1, seq2 = (fasta_dict[key] for key in fasta_dict.keys())
transitions = [set(['A', 'G']), set(['C', 'T'])]
transitions_num, transfections_num = 0, 0

for index in range(len(seq1)):
    if seq1[index] != seq2[index]:
        if set([seq1[index], seq2[index]]) in transitions:
            transitions_num += 1
        else:
            transfections_num += 1

print(round(transitions_num/transfections_num, 3))