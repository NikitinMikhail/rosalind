import common

cod_dict = common.codon_dict()
strand = open('PROT.txt', 'r').readlines()[0].strip()
prot_strand = ''

while len(strand) > 1 and cod_dict[strand[0:3]] != 'Stop':
	prot_strand += cod_dict[strand[0:3]]
	strand = strand[3:]

print(prot_strand)
