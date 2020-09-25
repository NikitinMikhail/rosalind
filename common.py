CODON_TABLE_PATH = r'C:\Users\mishn\PycharmProjects\rosalind\codon_table.txt'

def one_line_reader(filepath):
    with open(filepath, 'r') as f:
        read_line = f.readline().strip()
    return read_line


def multi_line_reader(filepath):
    with open(filepath, 'r') as f:
        read_lines = f.readlines()
    read_lines = [line.rstrip() for line in read_lines]
    return read_lines


def codon_dict():
    coddict = dict()
    coddict_lines = open(CODON_TABLE_PATH, 'r').readlines()
    for line in coddict_lines:
        codon, letter = [i for i in line.split()]
        coddict.update({codon: letter})
    return coddict


def fasta_parser(filepath):
    fasta_lines = open(filepath, 'r').readlines()
    fasta_dict = dict()
    for line in fasta_lines:
        if line[0] == '>':
            current_header = line.strip()[1:]
            fasta_dict[current_header] = ''
        elif len(line) > 1:
            fasta_dict[current_header] += line.rstrip()
    return fasta_dict


def reverse_comp(strand):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    rev_strand = strand[::-1]
    rev_comp_strand = ''
    for item in rev_strand:
        rev_comp_strand += comp_dict[item]
    return rev_comp_strand
