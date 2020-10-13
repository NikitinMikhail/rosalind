import numpy

import common


def hit_matrix(seq1, seq2):
    hit_matrix = numpy.zeros((len(seq1) + 1, len(seq2) + 1))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                hit_matrix[i + 1][j + 1] = hit_matrix[i][j] + 1
            else:
                hit_matrix[i + 1][j + 1] = max(hit_matrix[i + 1][j], hit_matrix[i][j + 1])
    return hit_matrix


def longest_common_subsequence(seq1, seq2):
    M = hit_matrix(seq1, seq2)
    i, j, lcss = len(seq1), len(seq2), ''
    while i * j != 0:
        if M[i][j] == M[i - 1][j]:
            i -= 1
        elif M[i][j] == M[i][j - 1]:
            j -= 1
        else:
            lcss = seq1[i - 1] + lcss
            i -= 1
            j -= 1

    return lcss


if __name__ == '__main__':
    fasta_dict = common.fasta_parser('LCSQ.txt')
    seq1, seq2 = (fasta_dict[key] for key in fasta_dict.keys())
    print(longest_common_subsequence(seq1, seq2))
