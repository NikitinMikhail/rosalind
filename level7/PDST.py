import common

def get_dist_table(fastlist):

fasta_dict = common.fasta_parser('PDST.txt')
fasta_list = [fasta_dict[item] for item in fasta_dict.keys()]


