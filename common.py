CODON_TABLE_PATH = r'C:\Users\mishn\PycharmProjects\rosalind\codon_table.txt'
PROTEIN_MASS_FILE = r'C:\Users\mishn\PycharmProjects\rosalind\protein_mass_table.txt'


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


def translate_rna(strand):
    cod_dict = codon_dict()
    prot_strand = ''
    while len(strand) > 1 and cod_dict[strand[0:3]] != 'Stop':
        prot_strand += cod_dict[strand[0:3]]
        strand = strand[3:]
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
    positions = [str(m.start() + 1) for m in re.finditer('(?={})'.format(substring), string)]
    return positions