import common

adj_len = 3
fasta_dict = common.fasta_parser('GRPH.txt')
adj_list = []

for key in fasta_dict.keys():
    for inner_key in fasta_dict.keys():
        if fasta_dict[key][-adj_len:] == fasta_dict[inner_key][:adj_len] and key != inner_key:
            adj_list.append((key, inner_key))

with open('GRPH_result.txt', 'w') as output_file:
    for adj in adj_list:
        print(' '.join(map(str, [item for item in adj])), file=output_file)
