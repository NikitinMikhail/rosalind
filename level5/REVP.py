import common

fasta_dict = common.fasta_parser('REVP.txt')
sequence = fasta_dict[list(fasta_dict.keys())[0]]
output_file = open('REVP_result.txt', 'w')
for half_pal_len in [2, 3, 4, 5, 6]:
    for position in range(len(sequence) - half_pal_len):
        if sequence[position:position + half_pal_len] == common.reverse_comp(
                sequence[position + half_pal_len:position + 2 * half_pal_len]):
            print(position + 1, 2 * half_pal_len, file=output_file)
output_file.close()
