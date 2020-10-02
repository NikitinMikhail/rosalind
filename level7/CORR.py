import common


def read_count(read_list, sequence):
    return read_list.count(sequence) + read_list.count(common.reverse_comp(sequence))


def get_correct_reads(read_list):
    return [read for read in read_list if read_count(read_list, read) > 1]


def hamming_distance(seq1, seq2):
    mismatch_count = 0
    for index in range(len(seq1)):
        mismatch_count += 1 * (seq1[index] != seq2[index])
    return mismatch_count


if __name__ == '__main__':
    fasta_dict = common.fasta_parser('CORR.txt')
    fasta_list = [fasta_dict[key] for key in fasta_dict.keys()]
    correct_reads = get_correct_reads(fasta_list)
    print(fasta_list)
    print(correct_reads)
    used_for_correction = list()
    with open('CORR_result.txt', 'w') as outfile:
        for item in fasta_list:
            if item not in correct_reads and item not in used_for_correction:
                for correct_item in correct_reads:
                    if hamming_distance(item, correct_item) == 1:
                        print('{}->{}'.format(item, correct_item), file=outfile)
                        used_for_correction.append(item)
                        break
                    elif hamming_distance(item, common.reverse_comp(correct_item)) == 1:
                        print('{}->{}'.format(item, common.reverse_comp(correct_item)), file=outfile)
                        used_for_correction.append(item)
                        break

