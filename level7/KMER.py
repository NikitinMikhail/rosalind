import common

kmer_len = 4

def get_kmer_count(string, kmer):
    return len(common.substring_positions(string, kmer))

fasta_dict = common.fasta_parser('KMER.txt')
sequence = fasta_dict[list(fasta_dict.keys())[0]]

all_kmers = common.get_kmers(["A", "T", "G", "C"], kmer_len)
print(' '.join(map(str, [get_kmer_count(sequence, kmer) for kmer in all_kmers])))

