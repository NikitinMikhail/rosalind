import numpy as np
from level4.HAMM import hamming_distance
import common


def get_dist_table(fasta_dict):
    fasta_list = [fasta_dict[item] for item in fasta_dict.keys()]
    d = np.zeros((len(fasta_list), len(fasta_list)))
    for i in range(len(fasta_list)):
        for j in range(len(fasta_list)):
            d[i][j] = round(hamming_distance(fasta_list[i], fasta_list[j]) / len(fasta_list[i]), 4)
    return d


if __name__ == '__main__':
    input_fasta_dict = common.fasta_parser('PDST.txt')
    dist_matrix = get_dist_table(input_fasta_dict)
    with open('PDST_result.txt', 'w') as outfile:
        for i in dist_matrix:
            print(' '.join(map(str, i)), file=outfile)
