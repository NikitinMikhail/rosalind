import common

fasta_dict = common.fasta_parser('SPLC.txt')
raw_seq = fasta_dict[list(fasta_dict.keys())[0]]

for key in fasta_dict.keys():
    if fasta_dict[key] != raw_seq:
        start_position = raw_seq.index(fasta_dict[key])
        raw_seq = raw_seq[:start_position] + raw_seq[start_position + len(fasta_dict[key]):]

print(common.translate_rna(raw_seq.replace('T', 'U')))
