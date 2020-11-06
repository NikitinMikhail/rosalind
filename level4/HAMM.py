def hamming_distance(strand1, strand2):
    mismatches = 0
    counter = 0

    for letter in strand1:
        if letter != strand2[counter]:
            mismatches += 1
        counter += 1
    return mismatches


if __name__ == '__main__':
    strand_lines = open('HAMM.txt', 'r').readlines()

    strand1 = strand_lines[0].strip()
    strand2 = strand_lines[1].strip()
    print(hamming_distance(strand1, strand2))
