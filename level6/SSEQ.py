import common

fasta_dict = common.fasta_parser('SSEQ.txt')
ref_seq = fasta_dict[list(fasta_dict.keys())[0]]
search_seq = fasta_dict[list(fasta_dict.keys())[1]]
print(ref_seq, search_seq)
indices_list = [common.substring_positions(ref_seq, letter) for letter in search_seq]
#print(indices_list)
spliced_motif = list()
for item in indices_list:
    if spliced_motif == []:
        spliced_motif.append(item[0])
        continue
    for index in item:
        if spliced_motif[0] == index:
            continue
        elif index > spliced_motif[-1]:
            spliced_motif.append(index)
            break

print(' '.join(map(lambda x: str(x+1), spliced_motif)))