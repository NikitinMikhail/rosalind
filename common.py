CODON_TABLE_PATH = r'C:\Users\mishn\PycharmProjects\rosalind\codon_table.txt'
PROTEIN_MASS_FILE = r'C:\Users\mishn\PycharmProjects\rosalind\protein_mass_table.txt'
import re


def one_line_reader(filepath):
    """

    :param filepath: path to a task file with one line of text
    :return: that line without EOL element
    """
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


def translate_rna(strand):
    cod_dict = codon_dict()
    prot_strand = ''
    inner_strand = strand
    while len(inner_strand) > 1 and cod_dict[inner_strand[0:3]] != 'Stop':
        prot_strand += cod_dict[inner_strand[0:3]]
        inner_strand = inner_strand[3:]
    return prot_strand


def translate_dna(strand):
    return translate_rna(strand.replace('T', 'U'))


def get_protein_mass(protein):
    mass_dict = dict()
    with open(PROTEIN_MASS_FILE, 'r') as f:
        mass_lines = f.readlines()
        for line in mass_lines:
            mass_dict.update({line.split()[0]: float(line.split()[1])})
    return mass_dict[protein]


def substring_positions(string, substring):
    positions = [m.start() for m in re.finditer('(?={})'.format(substring), string)]
    return positions


def find_orf_dna(sequence):
    start_codon_positions = substring_positions(sequence, 'ATG')
    stop_codon_positions = substring_positions(sequence, 'TAA')
    stop_codon_positions.extend(substring_positions(sequence, 'TAG'))
    stop_codon_positions.extend(substring_positions(sequence, 'TGA'))
    coord_list = []
    for item in start_codon_positions:
        for inner_item in stop_codon_positions:
            if inner_item > item and item % 3 == inner_item % 3:
                coord_list.append((item, inner_item))
                break
    orf_list = [sequence[start:stop] for (start, stop) in coord_list]
    return orf_list
